from falcon import HTTPError, HTTP_NOT_FOUND


class ModelNotFound(HTTPError):
    def __init__(self, model_name, **kwargs):
        super().__init__(status=HTTP_NOT_FOUND, title=model_name, description="not found", **kwargs)
