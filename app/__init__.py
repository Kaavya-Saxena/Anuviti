from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import PrimaryKeyConstraint
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import flask_whooshalchemyplus as wa
from flask_msearch import Search
import os

app = Flask(__name__)
# setting up a secret key 
app.config['SECRET_KEY'] = '72db111eb42ad709895bc3673307e9e4'
# determines where to store the db 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Anuviti_DB.db"
# setting this to True allows whoosh alchemy to know if something is changed in the db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# storing whoosh base in a folder called whoosh 
app.config['WHOOSH_BASE']='whoosh'
app.config['DEBUG'] = True
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'

# flask msearch and elasticsearch
search = Search()
search.init_app(app)
# configuring msearch 
search.create_index(update=True)
MSEARCH_INDEX_NAME =  os.path.join(app.root_path,'msearch')
MSEARCH_PRIMARY_KEY = 'id'
MSEARCH_ENABLE = True

from app import routes