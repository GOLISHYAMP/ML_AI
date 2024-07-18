from flask import url_for
from flask_mail import Message
from Trade_app import mail


def send_alert_email(users):
    for user in users:
        msg = Message('Alert', sender='noreply@demo.com',
                    recipients=[user])
        msg.body = f'''Be ready to be trade, Bullish candle is formed!!!

    If you do not make this request, this simply ignore this email and no changes will be made.
    '''
        mail.send(msg)