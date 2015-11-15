import cerberus
import dateutil.parser


TYPES = {
    'simple': cerberus.Validator(
        {
            'foo': {
                'required': True,
                'type': 'string',
            },
        },
    ),
    'complex': cerberus.Validator(
        {
            'boolean': {
                'required': True,
                'type': 'boolean',
            },
            'integer': {
                'required': True,
                'type': 'integer',
            },
            'list': {
                'required': True,
                'type': 'list',
                'schema': {
                    'type': 'float',
                },
            },
            'nested': {
                'required': True,
                'type': 'dict',
                'schema': {
                    'datetime': {
                        'coerce': dateutil.parser.parse,
                        'required': True,
                        'type': 'datetime',
                    },
                },
            },
            'string': {
                'required': True,
                'type': 'string',
            },
        },
    ),
}
