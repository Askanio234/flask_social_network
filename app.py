from flask import Flask, g, render_template, flash, redirect, url_for
from flask.ext.login import LoginManager
import models
import forms

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = "wqeqwe2134124!3FF..,qa231"


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close connection to the database after each request"""
    g.db.close()
    return response


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        flash("Thank you, for registration!", "success")
        models.User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/')
def index():
    return "Welcome!"


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
