class Config():
    SECRET_KEY = '2902992a6591ac61edb51110a82d7287'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''  # your email address
    MAIL_PASSWORD = ''  # your password
    SCHEDULER_API_ENABLED = True

    
