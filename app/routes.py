from http.client import responses
from flask import Flask, render_template, flash, redirect, request, url_for
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
import socket
import requests
import geocoder
# custom imports 
from app import app, db, bcrypt
from app.models import User, Organization 
from app.UserForms import RegistrationForm, LoginForm, UpdateAccountForm, SearchForm
from app.OrgForms import OrgRegistrationForm

# API FOR CLIENT IP ADDRESS
host_name = socket.gethostname()    
IPAddress = socket.gethostbyname(host_name) 

# API FOR DETERMINING CITY USING API
g=geocoder.ip(IPAddress)
response=g.city

# FUNCTIONS 

def save_picture(form_picture):
    # making custom file names to store in db to avoid collision with some other picture's name 
    random_hex = secrets.token_hex(8)
    # to save this file with same extension with which it was uploaded 
    # f_name gives filename w/o ext and extension itself 
    f_name, f_ext = os.path.splitext(form_picture.filename)
    # picture_filename is name as what the file will be saved in db 
    picture_filename= random_hex + f_ext
    # making path at which the profile picture shall be stored of uploaded 
    picture_path = os.path.join(app.root_path, f'static/ProfilePics', picture_filename)
    # Actually saving the picture 
    form_picture.save(picture_path)

    return picture_filename

# ROUTES 

@app.route('/')
@app.route('/home')
def hello_world():
    # replace delhi with response when using app 
    orgs = Organization.query.msearch('Delhi',fields=['name','type_of_donations_accepted','state','city'])[:5]
    print(IPAddress)
    orgs_name=[]
    for org in orgs:
        name={'name':org.name,
            'email':org.email, 
            'city':org.city, 
            'state':org.state, 
            'website_link':org.website_link, 
            'org_image_file':org.image_file
            }
        orgs_name.append(name)
    return render_template('index.html', orgs=orgs_name)


@app.route("/register", methods=['GET', 'POST'])
def register():
    # if the user is already authenticated redirect to home page 
    if current_user.is_authenticated:
        return redirect(url_for('hello_world'))
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        # hashing the password entered in the form to store in db 
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # creating and storing user in db 
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        # flash sends 1 time alert 
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('login'))
    return render_template('UserRegistration.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    # if current user is already authenticated redirect to home 
    if current_user.is_authenticated:
        return redirect(url_for('hello_world'))
    
    form = LoginForm()

    if form.validate_on_submit():
        # checking if the entered email exists in db 
        # first because making multiple accounts from same email isnt allowed
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            # if the user tried to access a page that was only accessible to logged in user
            # that is there is some query in url after /login 
            # store that page in var next_page 
            next_page = request.args.get('next')
            # if the query was present take them to that page or return to home 
            return redirect(next_page) if next_page else redirect(url_for('hello_world'))
        else:
            flash('Login Unsuccessful. check Email and Password')
    return render_template('UserLogin.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("hello_world"))

@app.route("/account", methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    # if the form submitted is valid  execute updation
    if form.validate_on_submit():
        # checking if there is any picture uploaded 
        if form.UserPicture.data:
            # saving picture to profile pics by function made above 
            picture_file=save_picture(form.UserPicture.data)
            # updating picture of current user by the picture uploaded 
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account Updated')
        return redirect(url_for('account'))
    # populate the form using current users data is we go to account
    elif request.method=='GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
    image_file= url_for('static', filename='ProfilePics/' + current_user.image_file)
    return render_template('account.html', image_file=image_file, form=form)

@app.context_processor
def base():
    form=SearchForm()
    return dict(form=form)

@app.route('/search/')
@login_required
def search():
    keyword = request.args.get('query',default="")
    orgs = Organization.query.msearch(keyword,fields=['name','type_of_donations_accepted','state','city'])
    return render_template("search.html",title= keyword, orgs=orgs)


@app.route("/register_org", methods=['GET', 'POST'])
def register_org():
    form = OrgRegistrationForm()
    if form.validate_on_submit():

        # hashing the password entered in the form to store in db 
        hashed_password = bcrypt.generate_password_hash(form.org_password.data).decode('utf-8') 
        # saving picture to profile pics by function made above 
        org_picture_file=save_picture(form.UserPicture.data)
        # creating and storing org in db 
        print(form.org_name.data)
        org=Organization(
                        name=form.org_name.data,
                        email=form.org_email.data,
                        password=hashed_password,
                        type_of_donations_accepted=form.org_donations.data,
                        state=form.org_state.data,
                        city=form.org_city.data,
                        website_link=form.org_website.data,
                        image_file=org_picture_file
                        )
        db.session.add(org)
        db.session.commit()
        return redirect(url_for('hello_world'))
    return render_template('OrgRegistration.html', form=form)

