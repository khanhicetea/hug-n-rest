import hug
from falcon import HTTP_201
from app.models import db, Group
from app.schemas import GroupSchema


@hug.get('/groups')
def get_groups():
    """Get all groups"""
    groups = db.session.query(Group).all()
    return {"data": Group.dumps(groups)}


@hug.post('/groups')
def create_group(body: hug.types.MarshmallowSchema(GroupSchema()), response):
    """Create new group"""
    group = Group(**body)
    group.save_now()
    response.status = HTTP_201

    return group.dump()
