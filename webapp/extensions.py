from flask.ext.cache import Cache
from flask.ext.login import LoginManager

from webapp.models.user import User

# Setup flask cache
cache = Cache()

login_manager = LoginManager()


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
