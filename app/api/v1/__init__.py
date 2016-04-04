import hug


@hug.extend_api('/v1')
def api_v1():
    from . import utils, groups, users

    return [utils, groups, users]
