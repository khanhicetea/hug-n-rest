import jwt
from app import current_app


def token_verify(token):
    secret_key = current_app.config.get('SECRET_KEY')
    try:
        return jwt.decode(token, secret_key, algorithm='HS256')
    except jwt.DecodeError:
        return False


def token_generate(data):
    secret_key = current_app.config.get('SECRET_KEY')
    return jwt.encode(data, secret_key, algorithm='HS256')

