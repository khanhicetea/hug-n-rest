import os
from config import config
from libs import Config, Db


class HugAndRest():
    """Hug and Rest application class"""

    def __init__(self, config_obj):
        self.g = dict()
        self.extensions = dict()
        self.config = Config(config_obj)

    def init_app(self, callback):
        self.extensions['db'] = Db(app=self)
        callback()


env = os.getenv('APP_ENV', 'development')
current_app = HugAndRest(config[env])
