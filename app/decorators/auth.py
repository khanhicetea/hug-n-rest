import jwt
from app import current_app
from app.services.user import UserService


def token_verify(token):
    secret_key = current_app.config.get('SECRET_KEY')
    try:
        data = jwt.decode(token, secret_key, algorithm='HS256')
        return UserService.instance().get_one_or_fail(data['id'])
    except jwt.DecodeError:
        return False


def token_generate(data):
    secret_key = current_app.config.get('SECRET_KEY')
    return jwt.encode(data, secret_key, algorithm='HS256')

