import csv

from flask import (
    current_app,
)

from keeper.service.enums import (
    NotificationTypeEnum,
)
from keeper.service.notification.writer import (
    CsvNotificationWriter,
)


def test_notification_write(app):
    with app.app_context():
        writer = CsvNotificationWriter()
        test_data = [
            {'id': '1', 'datetime': '03.07.2021 13:01+03.00', 'type': NotificationTypeEnum.WARNING, 'message': 'Предупреждение'},
            {'id': '2', 'datetime': '03.07.2021 14:01+03.00', 'type': NotificationTypeEnum.INFO, 'message': ''},
        ]

        for notification in test_data:
            writer.write(notification)

        with open(current_app.config['DST_FILE']) as output_file:
            reader = csv.DictReader(output_file, fieldnames=CsvNotificationWriter.fieldnames)
            for row in reader:
                assert row == test_data.pop(0)
