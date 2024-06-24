import secrets, os
from PIL import Image
from datetime import datetime
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, NewPost
from flaskblog import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

# posts = [
#     {
#         'author': 'Corey Schafer',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 20, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 21, 2018'
#     }
# ]
@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode(
            'utf-8')
        user = User(username = form.username.data, email = form.email.data, 
                    password = hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created!, now you can login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Login Successful !', 'success')
            next = request.args.get('next')
            return redirect(next) if next else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.split(form_picture.filename)
    picture_fn = random_hex + file_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics/', picture_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route("/account",methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            if current_user.image_file != 'default.jpg':
                # Delete the previous profile pic from the database
                # Construct the file path
                file_path = os.path.join(app.root_path, 'static/profile_pics',
                                        current_user.image_file)
                # Check if the file exists before attempting to delete it
                if os.path.exists(file_path):
                    os.remove(file_path)

            picture_file_name = save_picture(form.picture.data)
            current_user.image_file = picture_file_name
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your profile has been updated!",'success')
        return redirect(url_for('account'))
    if request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename = 'profile_pics/'+ current_user.image_file)
    return render_template('account.html',title="Account", image_file = image_file,form = form)

@app.route("/post/new", methods = ["GET", "POST"])
@login_required
def newpost():
    form = NewPost()
    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("newpost.html", title= 'new_post', form = form, legend = 'New Post')

@app.route("/post/<int:post_id>")
def post(post_id):
    # if post_id is found then post object is returned
    #  or else 404 page not found error
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", title= post.title, post = post)

@app.route("/post/<int:post_id>/update", methods = ["GET", "POST"])
def updatepost(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author.username != current_user.username:
        # if it is not authorized then 403 unauthorized error
        abort(403)
    form = NewPost()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.date_posted = datetime.now()
        db.session.commit()
        flash("Post is successfully updated!",'success')
        return redirect(url_for("post", post_id=post.id))
    if request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template("newpost.html", title= post.title, form = form, legend = "Update Post")


@app.route("/post/<int:post_id>/delete", methods = ["POST"])
def deletePost(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author.username != current_user.username:
        # if it is not authorized then 403 unauthorized error
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted successfully!", "success")
    return redirect(url_for("home"))
    