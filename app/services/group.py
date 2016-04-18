from app.services.base import BaseService
from app.models.group import Group


class GroupService(BaseService):
    __model__ = Group
