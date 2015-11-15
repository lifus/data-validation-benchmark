class CerberusWrapper(object):
    def __init__(self, validator):
        self.validator = validator

    def validate(self, data):
        return self.validator.validate(data)
