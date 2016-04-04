import hug


@hug.extend_api('/v1')
def api_v1():
    from . import utils, auth, groups, users

    return [utils, auth, groups, users]
