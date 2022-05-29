# from xml.dom import ValidationErr
from email.message import Message
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, URL
from flask_login import current_user
# custom imports 
from app.models import Organization


class OrgRegistrationForm(FlaskForm):
    org_name = StringField('Username',
                           validators=[DataRequired(), Length(min=1, max=50)])
    org_email = StringField('Email',
                        validators=[DataRequired(), Email()])
    org_donations = StringField('Desc or Donations Accepted', 
                                validators=[DataRequired(),Length(min=2)])
    org_city = StringField('City',
                        validators=[DataRequired()])
    org_state = StringField('State',
                        validators=[DataRequired()])
    org_website = StringField('Website Link',
                        validators=[DataRequired()])
    UserPicture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    org_password = PasswordField('Password', validators=[DataRequired()])
    org_confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('org_password')])
    submit = SubmitField('Sign Up')

    # template to add custom validations for forms 
    # def validate_field(self, field):
    #     if condition==True:
    #         raise ValidationError('Validation Message')

    def validate_username(self, org_name):
        org=Organization.query.filter_by(name=org_name.data).first()
        if org:
            raise ValidationError('Username Already Taken. Please choose a different Username')

    def validate_email(self, org_email):
        org=Organization.query.filter_by(email=org_email.data).first()
        if org:
            raise ValidationError('Email Already Taken. Please choose a different email')
    
    def validate_website(self, org_website):
        org=Organization.query.filter_by(website_link=org_website.data).first()
        if org:
            raise ValidationError('Website Already Taken.')