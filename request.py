from marshmallow import Schema, fields, validate

valid_cmd = ('filter', 'map', 'unique', 'sort', 'limit')


class RequestSchema(Schema):
    cmd = fields.Str(required=True, validate=validate.OneOf(valid_cmd))
    value = fields.Str(required=True)


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)
    file_name = fields.Str(required=True)
