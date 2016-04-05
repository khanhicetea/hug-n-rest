import json
from .hug_and_rest import current_app


def init_app_callback():
    import hug

    @hug.extend_api("/api")
    def register_blueprint():
        from . import api
        return [api]

    @hug.not_found()
    def not_found_handler(request, response):
        response.body = json.dumps({"Endpoint": "not found"})

current_app.init_app(init_app_callback)
