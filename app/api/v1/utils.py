import hug
from datetime import datetime


@hug.get('/utils/today')
def get_now():
    return "Now is {}".format(datetime.today().isoformat())
