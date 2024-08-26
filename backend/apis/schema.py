from marshmallow import fields, Schema, validate


class CalculateMemorySchema(Schema):
    model_name = fields.Str(required=True, validate=validate.Length(min=1))
    token = fields.Str(missing=None)
