from flask import render_template, redirect, url_for, flash, jsonify, Response, json, request
# import json
from test import app, db, bcrypt #, cipher_suite
from test.forms import RegistrationForm
from test.models import Users, UserPersonal
import os
from collections import OrderedDict
import datetime


@app.route('/')
def home():
    return "<h1>Hello world</h1>"

@app.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(userName = form.UserName.data, phoneNumber = form.phoneNumber.data , email = form.email.data)
        db.session.add(user)
        db.session.commit()
        userpersonal = UserPersonal(user_id = user.userID,
                                     FirstName = form.firstName.data,
                                     MiddleName = form.middleName.data,
                                       LastName = form.lastName.data, 
                                       FullName = str(form.firstName.data)+' '+str(form.middleName.data)+' '+str(form.lastName.data),
                                         DOB = form.DOB.data, Gender=form.Gender.data , 
                                         AadharID = form.Aadhar.data)
        db.session.add(userpersonal)
        db.session.commit()
        flash(f'Account created!, now you can login', 'success')
        return redirect(url_for('register'))    

    return render_template('register.html', title='Register', form=form)


@app.route('/user/<int:id>', methods = ["GET"])
def userdetails(id):
    # print(type(id))
    # print(id)
    user = Users.query.get_or_404(id)
    # if user:
    dic ={
        "id": int(user.userID),
        'userName': user.userName,
        'phoneNumber': user.phoneNumber,
        'email':user.email,
        'userPersonal':{
            "firstName": user.personal.FirstName,
            "middleName": user.personal.MiddleName,
            "lastName": user.personal.LastName,
            'fullName': user.personal.FullName,
            "dob": user.personal.DOB,
            "gender": user.personal.Gender,
            "aadharNo": user.personal.AadharID
        }
    }
    response =  json.dumps(dic, sort_keys = False)
    return response
  
@app.route('/user', methods = ["GET"])
def users():
    allUsers = Users.query.all()
    # if user:
    li =[]
    for user in allUsers:

        dic ={
            'userName': user.userName,
            'phoneNumber': user.phoneNumber,
            'email':user.email,
            'userPersonal':{
                "firstName": user.personal.FirstName,
                "middleName": user.personal.MiddleName,
                "lastName": user.personal.LastName,
                'fullName': user.personal.FullName,
                "dob": user.personal.DOB,
                "gender": user.personal.Gender,
                "aadharNo": user.personal.AadharID
            }
        }
        li.append(dic)
    response =  json.dumps(li, sort_keys = False)
    return response

# update
# delete
@app.route('/user/update', methods = ["PUT"])
def update():
    data = request.json
    # print(data.keys)
    if not data or ('userName' not in data):
        return jsonify({"error": "No input data provided"}), 400
    
    user = Users.query.filter_by(userName = data['userName']).first()
    if not user:
        return jsonify("user not found"), 404
    
    for key in data:
        if key == "userName":
            continue
        if key in ['phoneNumber','dob']:
            if key == 'phoneNumber':
                user.phoneNumber = data[key]
            if key == 'dob':
                # Convert the string to a datetime object
                date_obj = datetime.datetime.strptime(data[key], "%d/%m/%Y")
                user.personal.DOB = date_obj
            db.session.commit()
    return jsonify(f"Updated")

@app.route('/user/delete/<string:username>', methods = ["DELETE"])
def delete(username):
    user = Users.query.filter_by(userName = username).first()
    if not user:
        return jsonify('user not found'), 404
    db.session.delete(user)
    return jsonify(f"{username} is successfully delete")