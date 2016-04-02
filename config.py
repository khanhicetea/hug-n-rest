import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Hug and Rest'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'database.sqlite'))

    @classmethod
    def get(cls, attr, default=None):
        print(attr)
        return getattr(cls, name=attr, default=default)

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}