import hug
from falcon import HTTP_201
from app.services import UserService
from app.schemas import UserSchema


@hug.get('/users')
def get_users():
    """Get all users"""
    return {"data": UserService.instance().get_all(dumps=True)}


@hug.get('/users/{id}')
def get_one_user(id):
    """Get one user"""
    return {"data": UserService.instance().get_one_or_fail(id, dump=True)}


@hug.post('/users')
def create_user(body: hug.types.MarshmallowSchema(UserSchema()), response):
    """Create new user"""
    user = UserService.instance().create_one(**body)
    user.save_now()
    response.status = HTTP_201

    return user.dump()
