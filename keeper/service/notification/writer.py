import csv

from flask import (
    current_app,
)

from ..lib import (
    Singleton,
)


class NotificationWriter:
    """Basic class for implementing notification writers to different destinations"""
    def write(self, notification_data: dict):
        raise NotImplementedError


class CsvNotificationWriter(NotificationWriter, Singleton):
    """
    Use this class to write notifications to csv-file
    defined by application configuration variable `DST_FILE`
    """
    fieldnames = [
        'id',
        'datetime',
        'type',
        'message',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._output_file = open(current_app.config['DST_FILE'], 'a')
        self._writer = csv.DictWriter(self._output_file, fieldnames=self.fieldnames)

    def __del__(self):
        self._output_file.close()

    def write(self, notification_data: dict) -> None:
        self._writer.writerow(notification_data)
        self._output_file.flush()
