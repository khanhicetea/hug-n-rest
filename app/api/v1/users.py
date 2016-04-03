import hug
from falcon import HTTP_201
from app.models import db, User
from app.schemas import UserSchema


@hug.get('/users')
def get_users():
    """Get all users"""
    users = db.session.query(User).all()
    return {"data": User.dumps(users)}


@hug.post('/users')
def create_user(body: hug.types.MarshmallowSchema(UserSchema()), response):
    """Create new user"""
    user = User(**body)
    user.save_now()
    response.status = HTTP_201

    return user.dump()
