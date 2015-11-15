import marshmallow


class SimpleSchema(marshmallow.Schema):
    foo = marshmallow.fields.Str(required=True)


class NestedSchema(marshmallow.Schema):
    datetime = marshmallow.fields.DateTime(required=True)


class ComplexSchema(marshmallow.Schema):
    boolean = marshmallow.fields.Boolean(required=True)
    integer = marshmallow.fields.Integer(required=True)
    list = marshmallow.fields.List(marshmallow.fields.Float(), required=True)
    nested = marshmallow.fields.Nested(NestedSchema, required=True)
    string = marshmallow.fields.Str(required=True)


INSTANCES = {
    'simple': SimpleSchema(),
    'complex': ComplexSchema(),
}
