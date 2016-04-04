from app.services.base import BaseService
from app.models import Group


class GroupService(BaseService):
    __model__ = Group
