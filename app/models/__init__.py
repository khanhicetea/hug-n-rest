from app import current_app


db = current_app.extensions['db']


from .base import Base
from .group import Group
from .user import User
