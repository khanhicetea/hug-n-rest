import hug
from . import utils, groups


@hug.extend_api('/v1')
def api_v1():
    return [utils, groups]