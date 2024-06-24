from flaskblog import db, login_manager
from datetime import datetime
from flask_login import UserMixin
# now this UserMixin extension have the is_authenticated, is_active ,
#  is_anonymous, get_id

# This description is given in the readme file
# Basically it is used by the login manager to find to fetch userdata
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    def __repr__(self):
        return f"user ( '{self.username}', '{self.email}', '{self.image_file}')"
    


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False) 
    # Here smallcase table user and column id, by default model name converts
    # into table name with smallcase.

    def __repr__(self):
        return f"post ( '{self.title}', '{self.date_posted}')"