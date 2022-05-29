from email.policy import default
from flask_login import UserMixin # has different methods for user such as is_authenticated()
# custom imports 
from app import db, login_manager

# function takes user id as param to load the user from db 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # OOP in python 
    def __repr__(self):
        return f"User('{self.username}','{self.email}', '{self.image_file}')"

class Organization(db.Model):
    # searchable fields 
    __searchable__ = ['name','type_of_donations_accepted','state','city']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(20),nullable=False)
    image_file = db.Column(db.String(20),nullable=False, default='default_org.jpg')
    password = db.Column(db.String(60),nullable=False)
    type_of_donations_accepted = db.Column(db.String(120))
    state = db.Column(db.String(120),nullable=False)
    city = db.Column(db.String(120),nullable=False)
    website_link = db.Column(db.String(120))
    likes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"Organization('{self.name}','{self.type_of_donations_accepted}','{self.city}','{self.state}','{self.website_link}')"
