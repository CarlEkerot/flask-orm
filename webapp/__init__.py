import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from webapp.extensions import cache, login_manager


def create_app(object_name, env="prod"):
    """
    Arguments:
        object_name: the python path of the config object,
                     e.g. webapp.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """

    app = Flask(__name__)

    app.config.from_object(object_name)
    app.config['ENV'] = env

    # init the cache
    cache.init_app(app)

    # init SQLAlchemy
    db.init_app(app)

    login_manager.init_app(app)

    # register our blueprints
    from controllers.main import main
    from controllers.user import user
    app.register_blueprint(main)
    app.register_blueprint(user)

    return app

if __name__ == '__main__':
    # Import the config for the proper environment using the
    # shell var APP_ENV
    env = os.environ.get('APP_ENV', 'prod')
    app = create_app('webapp.settings.%sConfig' % env.capitalize(), env=env)

    app.run()
