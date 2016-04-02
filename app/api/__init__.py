import hug
from . import v1


@hug.extend_api('/api')
def api():
    return [v1]