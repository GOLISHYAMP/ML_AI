from flask import render_template, redirect, current_app as app
from flask import Blueprint
from Trade_app.utils import send_alert_email
from Trade_app import scheduler
from datetime import datetime, time
import requests


main = Blueprint('main', __name__)

# from __future__ import print_function
# import time
import upstox_client
from upstox_client.rest import ApiException
from pprint import pprint


def within_time_range():
    now = datetime.now().time()
    start_time = time(9, 20)
    end_time = time(23, 55)
    return start_time <= now <= end_time



@main.route('/')
def home():
    # # create an instance of the API class
    # api_instance = upstox_client.LoginApi()
    # client_id = 'af7ba299-3586-4386-90b7-fea7792ac90e' # str | 
    # redirect_uri = 'https://192.168.0.102:5000/about' # str | 
    # api_version = 'v2' # str | API Version Header
    # state = 'state_example' # str |  (optional)
    # scope = 'scope_example' # str |  (optional)

    # try:
    #     # Authorize API
    #     api_instance.authorize(client_id, redirect_uri, api_version)
    # except ApiException as e:
    #     print("Exception when calling LoginApi->authorize: %s\n" % e)
    response = requests.get('https://api.upstox.com/v2/login/authorization/dialog?client_id=af7ba299-3586-4386-90b7-fea7792ac90e&redirect_uri=https%3A%2F%2F192.168.0.102%3A5000%2Fabout', verify=False)
    print(response)
    return '<h1>Hello Trader</h1>'


@main.route('/about')
def about():
    return '<h1>Hello Trader. This is the about page</h1>'

@main.route('/send')
def send_mail():
    # users = ['shyamgoli3105@gmail.com', 'golishyamgolisai@gmail.com']
    users = ['shyamgoli3105@gmail.com']
    send_alert_email(users)
    return '<h1>mail sent successfully!!!</h1>'
