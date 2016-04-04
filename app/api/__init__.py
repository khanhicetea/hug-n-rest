import hug


@hug.extend_api('/api')
def api():
    from . import v1

    return [v1]
