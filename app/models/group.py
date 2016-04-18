from sqlalchemy import Column, Integer, String
from app.models.base import Base
from app.schemas.group import GroupSchema


class Group(Base):
    __tablename__ = 'groups'
    __schema__ = GroupSchema

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    alias = Column(String(100))
    max_members = Column(Integer, nullable=False, default=0)
