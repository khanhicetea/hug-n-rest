import hug
from .hug_and_rest import current_app


def init_app_callback():
    @hug.extend_api()
    def register_blueprint():
        from . import api
        return [api]

current_app.init_app(init_app_callback)
