import hug


@hug.extend_api('/v1')
def api():
    from . import v1

    return [v1]
