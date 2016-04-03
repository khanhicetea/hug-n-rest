import hug
import os
from config import config
from libs.db import Db


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

    def init_app(self):
        self.extensions['db'] = Db(app=self)

        @hug.extend_api()
        def register_blueprint():
            from . import api

            return [api]


def create_app(app_env):
    app_config = Config()
    app_config.from_object(config[app_env])
    app = HugAndRest(app_config)

    return app


env = os.getenv('APP_ENV', 'development')
current_app = create_app(env)
current_app.init_app()