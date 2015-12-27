import pytest

from sqlalchemy.orm import scoped_session, sessionmaker

from webapp import db, create_app
from webapp.settings import TestConfig


@pytest.yield_fixture(scope="session")
def app():
    _app = create_app(TestConfig)
    db.app = _app
    db.create_all()

    _app.connection = db.engine.connect()

    yield _app

    _app.connection.close()
    db.drop_all()


@pytest.yield_fixture(scope="function")
def session(app):
    app.transaction = app.connection.begin()

    with app.app_context():
        session = scoped_session(sessionmaker(bind=app.connection))
        db.session = session

        yield session

        app.transaction.rollback()
        session.remove()


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()
