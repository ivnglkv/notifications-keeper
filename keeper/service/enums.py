from enum import Enum


class NotificationTypeEnum(str, Enum):
    ALERT = 'alert'
    ERROR = 'error'
    WARNING = 'warning'
    NOTICE = 'notice'
    INFO = 'info'
    DEBUG = 'debug'
