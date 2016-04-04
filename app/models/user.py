from app.models import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.schemas import UserSchema


class User(Base):
    __tablename__ = 'users'
    __schema__ = UserSchema

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    fullname = Column(String(100))
    email = Column(String(50))
    password = Column(String(64))
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)

    group = relationship('Group')
