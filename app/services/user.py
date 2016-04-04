from app.services.base import BaseService
from app.models import User


class UserService(BaseService):
    __model__ = User

    def login(self, email, password):
        result = self.model.query().filter_by(email=email).first()

        if result:
            if result.password == password:
                return result
        return False
