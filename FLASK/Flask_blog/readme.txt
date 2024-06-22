
write like this in the shell 
from flaskblog import app, db
>>> from flaskblog import User, Post
>>> with app.app_context():
...     User.query.all()
User.query.first()
User.query.filter_by(username='sai').all()
User.query.filter_by(username='sai').first()
user = User.query.get(1)   # this is to get the user by id

from flaskblog import app, db
>>> with app.app_context():
...     db.create_all()
...     print("Database tables created.")



write like this in iteractive cli
 with app.app_context():                                               
...     post1 = Post(title="blog1", content="first post content", user_id=user.id)
...     post2 = Post(title="blog2", content="second post content", user_id=user.id)
...     db.session.add(post1) 
...     db.session.add(post2)                                             
...     db.session.commit()   

>>> with app.app_context():       
...     post = Post.query.first()
...     post.author  

 with app.app_context():
...     db.drop_all()       
...


##### This is for hashing the password
##### We cannot store the plain text directly in the database.
#### pip install flask_bcrypt

>>> from flask_bcrypt import Bcrypt
>>> bcrypt = Bcrypt()
hashed_pwd = bcrypt.generate_password_hash("helloworld").decode('utf-8')
bcrypt.check_password_hash(hashed_pwd, "helloworld")


##### flask-login
The load_user function in a Flask application using Flask-Login is essential for handling user sessions and managing user authentication. Here's an in-depth explanation of its components and functionality:

Components and Functionality
Imports and Setup:

python
Copy code
from flaskblog import db, login_manager
from datetime import datetime
from flask_login import UserMixin

db is typically a SQLAlchemy instance for database operations.
login_manager is an instance of LoginManager from Flask-Login, used for session management.
datetime is used for handling date and time, often for timestamps in user models.
UserMixin is a Flask-Login mixin that provides default implementations for methods that Flask-Login expects user objects to have, such as is_authenticated, is_active, is_anonymous, and get_id.
User Model:
Your user model (not shown but implied) should inherit from SQLAlchemy's model class and UserMixin. For example:

python
Copy code
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # other fields such as username, email, password, etc.
The load_user Function:

python
Copy code
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
The @login_manager.user_loader decorator registers the load_user function with Flask-Login.
This function is called by Flask-Login to load a user from the session. Flask-Login uses this to reload the user object from the user ID stored in the session cookie.
How It Works
Session Management:
When a user logs in, their user ID is stored in the session. Flask-Login uses this user ID to retrieve the user's data when needed.

User Loader Function:

When Flask-Login needs to load the user (e.g., for checking authentication status, accessing user-specific data), it calls the load_user function.
The load_user function receives the user ID (as a string) from the session cookie.
It queries the database for the user with that ID using User.query.get(int(user_id)). This converts the user_id to an integer and fetches the user object from the database.
Methods Provided by UserMixin
is_authenticated: Returns True if the user is authenticated, i.e., they have provided valid credentials.
is_active: Returns True if the user's account is active.
is_anonymous: Returns True if the user is not authenticated.
get_id: Returns the unique ID of the user as a string (used to store in the session cookie).