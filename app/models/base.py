from . import db
from marshmallow import Schema


class Base(db.Base):
    __abstract__ = True
    __schema__ = Schema

    def save(self):
        db.session.add(self)

    def delete(self):
        db.session.delete(self)

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)

    def save_now(self):
        db.session.add(self)
        db.session.commit()

    def update_now(self, data):
        self.update(data)
        db.session.commit()

    def delete_now(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def query(cls):
        return db.session.query(cls)

    @classmethod
    def dumps(cls, lists):
        schema = cls.__schema__(many=True)
        return schema.dump(lists).data

    def dump(self, **options):
        schema = self.__class__.__schema__(many=False, **options)
        return schema.dump(self).data
