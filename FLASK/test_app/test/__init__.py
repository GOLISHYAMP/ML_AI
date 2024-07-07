from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from cryptograpy import fernet
# key = fernet.Fernet.generate_key()
# cipher_suite = Fernet(key)

app = Flask(__name__)
app.config['SECRET_KEY']='cb786e806e95b774c1eaa6da9598b355'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from test import routes
