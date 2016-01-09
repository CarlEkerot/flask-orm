from flask import Blueprint
from flask.ext.login import login_required

from webapp import cache

main = Blueprint('main', __name__)


@main.route('/')
@cache.cached(timeout=1000)
def home():
    return "Hello world"


@main.route("/login", methods=["POST"])
def login():
    # Do login stuff
    return "Logged in"


@main.route("/logout")
def logout():
    # Do logout stuff
    return "Logged out"


@main.route("/restricted")
@login_required
def restricted():
    return "You can only see this if you are logged in!"
