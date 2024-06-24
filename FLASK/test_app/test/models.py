from test import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userName = db.Column(db.String(20), nullable = False, unique = True)
    phoneNumber = db.Column(db.String(10), nullable=False, unique = True)
    email = db.Column(db.String(120), nullable = False, unique = True)
    createdOn = db.Column(db.DateTime, nullable = False, default = datetime.now)
    changedOn = db.Column(db.DateTime, nullable = False, default = datetime.now)

    def __repr__(self):
        return f"User '{self.userName}','{self.email}','{self.phoneNumber}'"

class UserPersonal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userName = db.Column(db.String(20), nullable = False, unique = True)
    phoneNumber = db.Column(db.String(10), nullable=False, unique = True)
    email = db.Column(db.String(120), nullable = False, unique = True)
    createdOn = db.Column(db.DateTime, nullable = False, default = datetime.now)
    changedOn = db.Column(db.DateTime, nullable = False, default = datetime.now)


    # updated