from test import db
from datetime import datetime, date

class Users(db.Model):
    userID = db.Column(db.Integer, primary_key = True)
    userName = db.Column(db.String(20), nullable = False, unique = True)
    phoneNumber = db.Column(db.String(10), nullable=False, unique = True)
    email = db.Column(db.String(120), nullable = False, unique = True)
    createdOn = db.Column(db.DateTime, nullable = False, default = datetime.now)
    changedOn = db.Column(db.DateTime, nullable = False, default = datetime.now)

    def __repr__(self):
        return f"User '{self.userName}','{self.email}','{self.phoneNumber}'"

class UserPersonal(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.userID'), nullable=False)
    id = db.Column(db.Integer, primary_key = True)
    FirstName = db.Column(db.String(20), nullable = False)
    MiddleName = db.Column(db.String(20), nullable=False)
    LastName = db.Column(db.String(20), nullable = False)
    FullName = db.Column(db.String(65), nullable = False)
    DOB = db.Column(db.Date, nullable = False, default = date.today)
    Gender = db.Column(db.String(10), nullable = False)
    AadharID = db.Column(db.String(60), nullable = False)
    user = db.relationship('Users', backref=db.backref('personal', uselist=False))

    def __repr__(self):
        return f"UserPersonal '{self.FullName}','{self.DOB}','{self.Gender}'"

    # updated