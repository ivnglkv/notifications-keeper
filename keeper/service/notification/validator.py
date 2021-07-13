import json
from jsonschema import (
    Draft7Validator,
    FormatChecker,
)
import pkg_resources

_schema_file = pkg_resources.resource_stream('keeper.service.notification', 'schema.json')
_schema = json.load(_schema_file)

_checker = FormatChecker()
_validator = Draft7Validator(schema=_schema, format_checker=_checker)


def validate_incoming_notification(notification: dict):
    messages = [err.message for err in _validator.iter_errors(notification)]
    is_valid = not bool(messages)

    return is_valid, messages
