#!/usr/bin/env python
import os

from flask.ext.script import Manager, Server
from flask.ext.script.commands import ShowUrls, Clean
from webapp import create_app, db
from webapp.models.user import User

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('APP_ENV', 'dev')
app = create_app('webapp.settings.%sConfig' % env.capitalize(), env=env)

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())


@manager.shell
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """

    return dict(app=app, db=db, User=User)


@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
        your Alchemy models
    """

    db.create_all()

if __name__ == "__main__":
    manager.run()
