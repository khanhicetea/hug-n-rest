from app.services.base import BaseService
from app.models import User


class UserService(BaseService):
    __model__ = User

    def login(self, email, password):
        result = self.model.query().filter_by(email=email).first()

        return result if result and result.password == password else False

