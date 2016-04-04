from app.services.base import BaseService
from app.models import User


class UserService(BaseService):
    __model__ = User
