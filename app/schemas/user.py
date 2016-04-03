from marshmallow import Schema, fields
from .group import GroupSchema


class UserSchema(Schema):
    id = fields.Integer(required=False)
    name = fields.Str()
    fullname = fields.Str()
    email = fields.Str()
    password = fields.Str()
    group_id = fields.Integer()
    group = fields.Nested(GroupSchema, required=False)
