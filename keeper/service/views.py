from flask import (
    request,
)

from .app import (
    module,
)
from .enums import (
    HttpStatusCodesEnum as Status,
)
from .notification.validator import (
    validate_incoming_notification,
)
from .notification.writer import (
    CsvNotificationWriter,
)


@module.route('/hook', methods=['POST'])
def hook():
    data = request.get_json()
    is_valid, errors = validate_incoming_notification(data)

    response = {
        'result': 'OK' if is_valid else 'Error',
        'messages': None if is_valid else errors,
    }

    if is_valid:
        CsvNotificationWriter().write(data)

    status_code = Status.OK if is_valid else Status.SERVER_ERROR

    return response, status_code.value
