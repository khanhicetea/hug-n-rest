import hug
import os
from config import config
from lib.db import Db


class Config(dict):
    """Hug and Rest config class"""
    def from_object(self, obj):
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)


class HugAndRest():
    """Hug and Rest application class"""

    def __init__(self, config):
        self.g = dict()
        self.extensions = dict()
        self.config = config


def create_app(app_env):
    app_config = Config()
    app_config.from_object(config[env])
    app = HugAndRest(app_config)
    app.extensions['db'] = Db(app=app)

    return app


env = os.getenv('APP_ENV', 'development')
current_app = create_app(env)


@hug.extend_api()
def register_blueprint():
    from . import api

    return [api]
