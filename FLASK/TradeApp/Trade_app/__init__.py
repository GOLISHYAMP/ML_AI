import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
from flask_cors import CORS
# from itsdangerous import URLSafeSerializer as Serializer
from flask_mail import Mail
from Trade_app.config import Config
from flask_apscheduler import APScheduler


db = SQLAlchemy()
bcrypt = Bcrypt()
# login_manager = LoginManager()
# login_manager.login_view = 'users.login' # it is a function name of route
# login_manager.login_message_category = 'info'
# CORS()
mail = Mail()
scheduler = APScheduler()


def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    # login_manager.init_app(app)
    CORS(app)
    mail.init_app(app)
    scheduler.init_app(app)

    from Trade_app.main.routes import main, within_time_range, send_mail
    app.register_blueprint(main)


    @scheduler.task('cron', id='do_job_5mins', minute='*/5', hour='9-23', day_of_week='mon-fri')
    def job():
        with app.app_context():
            if within_time_range():
                send_mail()
    scheduler.start()

    # from flaskblog.users.routes import users
    # from flaskblog.posts.routes import posts
    # from flaskblog.errors.handlers import errors

    # app.register_blueprint(users)
    # app.register_blueprint(posts)
    # app.register_blueprint(errors)

    return app