from flask import Blueprint, request
from flask.ext.login import login_required, login_user, logout_user

from webapp import cache
from webapp.models.user import User

main = Blueprint('main', __name__, static_folder='../static')


@main.route('/')
@cache.cached(timeout=1000)
def home():
    return main.send_static_file('index.html')


@main.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return "Authentication error", 401

    login_user(user)

    return "Logged in"


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out"


@main.route("/restricted")
@login_required
def restricted():
    return "You can only see this if you are logged in!"
