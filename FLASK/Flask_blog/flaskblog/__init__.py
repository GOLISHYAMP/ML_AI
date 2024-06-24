from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
# secret key can be created by :
# import secrets
# secrets.token_hex(20)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# important while changing the database
# Only this thing need to be changed while changing database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# creating the instance of the database
db = SQLAlchemy(app)
# For encrpting the password fields
bcrypt = Bcrypt(app)
# For managing the login related things
login_manager = LoginManager(app)
# to enable CROSS ORIGIN RESOURCE SHARING
CORS(app)
# if access unauthorized page then redirect to login page
login_manager.login_view = 'login' # it is a function name of route
# To set the category of the message if raise by the login manager
login_manager.login_message_category = 'info'

from flaskblog import routes
