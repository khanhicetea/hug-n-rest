from marshmallow import Schema, fields


class GroupSchema(Schema):
    id = fields.Integer(required=False)
    name = fields.Str()
    max_members = fields.Integer(missing=100)
    alias = fields.Str()
