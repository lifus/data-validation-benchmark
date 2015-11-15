from datavalidation.benchmark.base import BenchmarkBase


class BenchmarkValidData(BenchmarkBase):
    label = 'Validate simple valid data'
    validator = 'simple'
    data = {
        'foo': 'bar',
    }


class BenchmarkInvalidData(BenchmarkBase):
    label = 'Validate simple invalid data'
    valid = False
    validator = 'simple'
    data = {
        'invalid': 'data',
    }


class BenchmarkComplexValidData(BenchmarkBase):
    label = 'Validate complex valid data'
    validator = 'complex'
    data = {
        'boolean': True,
        'integer': 42,
        'list': [
            3.1415
        ],
        'nested': {
            'datetime': '2015-11-15 22:09:23.722591',
        },
        'string': 'foo',
    }
