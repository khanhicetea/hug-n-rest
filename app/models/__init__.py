from app import current_app
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


db = current_app.extensions['db']


class User(db.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    email = Column(String)
    password = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)

    group = relationship('Group')


class Group(db.Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    alias = Column(String)
    max_members = Column(Integer, nullable=False, default=0)

    def to_json(self):
        return {
            "name": self.name,
            "max_members": self.max_members,
            "alias": self.alias
        }