import hug
from falcon import HTTP_201
from app.services.group import GroupService
from app.schemas.group import GroupSchema


@hug.get('/groups')
def get_groups():
    """Get all groups"""
    return {"data": GroupService.instance().get_all(dumps=True)}


@hug.get('/groups/{id}')
def get_one_group(id):
    """Get one group"""
    return {"data": GroupService.instance().get_one(id, dump=True)}


@hug.post('/groups')
def create_group(body: hug.types.MarshmallowSchema(GroupSchema()), response):
    """Create new group"""
    group = GroupService.instance().create_one(**body)
    group.save_now()
    response.status = HTTP_201

    return group.dump()
