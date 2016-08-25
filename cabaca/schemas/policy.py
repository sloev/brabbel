from marshmallow import fields, Schema

class Policy(Schema):
    name = fields.Str(required=True)
    age = fields.Integer(required=True)
