class Config(object):
    SECRET_KEY = 'secret key'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CACHE_TYPE = 'simple'


class DevConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    CACHE_TYPE = 'null'
    CACHE_NO_NULL_WARNING = True


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    LOGIN_DISABLED = False

    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    CACHE_TYPE = 'null'
    CACHE_NO_NULL_WARNING = True
