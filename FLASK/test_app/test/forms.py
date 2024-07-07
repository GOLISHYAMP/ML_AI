from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, SubmitField, PasswordField, DateField, TelField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from test.models import Users, UserPersonal

class RegistrationForm(FlaskForm):
    firstName = StringField('First name',
                           validators=[DataRequired(), Length(min=1, max=20)])
    middleName = StringField('Middle name',
                           validators=[DataRequired(), Length(min=1, max=20)])
    lastName = StringField('Last name',
                           validators=[DataRequired(), Length(min=1, max=20)])
    UserName = StringField("Username",validators=[DataRequired(), Length(min=1, max = 20)])
    phoneNumber = TelField('PhoneNumber', validators=[DataRequired(), Length(min = 10,max=10)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    DOB = DateField('DOB', validators=[DataRequired()]) 
    # Gender = StringField("Gender", validators=[DataRequired(), Length(min=1, max=10)])
    Gender = SelectField("Gender", validators=[DataRequired()], choices=['Male', 'Female', 'Transgender'])
    Aadhar = StringField("Aadhar Number", validators=[DataRequired(), Length(min=1, max=12)])
    
    # password = PasswordField('Password', validators=[DataRequired()])
    # confirm_password = PasswordField('Confirm Password',
    #                                  validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Syntax for the custom validator
    # def validate_field(self,field):
    #     if True:
    #         raise ValidationError("Validation Message")
    def validate_UserName(self,UserName):
        user = Users.query.filter_by(userName = UserName.data).first()
        if user:
            raise ValidationError("Username is already taken! please take another")
    def validate_email(self,email):
        user = Users.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError("This email is already registered!")
    def validate_phoneNumber(self,phoneNumber):
        user = Users.query.filter_by(phoneNumber = phoneNumber.data).first()
        if user:
            raise ValidationError("PhoneNumber is already taken! please take another")
