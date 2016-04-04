import hug
from falcon import HTTP_UNAUTHORIZED
from marshmallow import fields
from app.services import UserService
from app.directives import token_generate, token_required


@hug.post('/auth/login')
def auth_login(email: fields.Email(), password: fields.String()):
    user = UserService.instance().login(email, password)

    if not user:
        raise HTTP_UNAUTHORIZED

    token_data = dict(id=user.id)
    return {"token": token_generate(token_data)}


@hug.get('/me', requires=token_required)
def who_am_i(user: hug.directives.user):
    user = UserService.instance().get_one(user['id'])
    return user.dump()
