class MarshmallowWrapper(object):
    def __init__(self, schema):
        self.schema = schema

    def validate(self, data):
        errors = self.schema.validate(data)
        return not errors
