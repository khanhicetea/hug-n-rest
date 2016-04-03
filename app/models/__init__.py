from app import current_app
from .base import Base
from .group import Group
from .user import User


db = current_app.extensions['db']
