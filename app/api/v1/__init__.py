import hug


@hug.get('/health')
def check_health():
    return {"status": "ok"}


@hug.extend_api()
def api_v1():
    from . import utils, auth, groups, users

    return [utils, auth, groups, users]
