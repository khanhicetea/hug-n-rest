from falcon import HTTPNotFound


class BaseService(object):
    __abstract__ = True
    __instance__ = None
    __model__ = None

    def __init__(self, model):
        self.model = model

    @classmethod
    def instance(cls, singleton=True):
        if not singleton:
            return cls(cls.__model__)
        if not cls.__instance__:
            cls.__instance__ = cls(cls.__model__)
        return cls.__instance__

    def get_all(self, dumps=False):
        result = self.model.query().all()
        return self.model.dumps(result) if dumps else result

    def get_one(self, id, dump=False):
        result = self.model.query().get(id)
        return (result.dump() if result else dict()) if dump else result

    def get_one_or_fail(self, id, dump=False):
        result = self.model.query().get(id)
        if not result:
            raise HTTPNotFound()
        return result.dump() if dump else result

    def create_one(self, **data):
        obj = self.model(**data)
        return obj
