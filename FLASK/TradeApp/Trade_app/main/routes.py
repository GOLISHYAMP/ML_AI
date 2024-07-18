from flask import render_template, redirect, current_app as app
from flask import Blueprint
from Trade_app.utils import send_alert_email
from Trade_app import scheduler
from datetime import datetime, time


main = Blueprint('main', __name__)


def within_time_range():
    now = datetime.now().time()
    start_time = time(9, 20)
    end_time = time(23, 55)
    return start_time <= now <= end_time



@main.route('/')
def home():
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
