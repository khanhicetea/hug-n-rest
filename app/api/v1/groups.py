import hug
from app.models import db, Group


@hug.get('/groups')
def get_groups():
    """Get all groups"""
    return {
        "data": [g.to_json() for g in db.session.query(Group).all()]
    }


@hug.post('/groups')
def create_group(name: hug.types.text, max_members: hug.types.number, alias: hug.types.text):
    """Create new group"""
    group = Group(name=name, max_members=max_members, alias=alias)
    db.session.add(group)
    db.session.commit()

    return {
        "group": group.to_json()
    }