from flask import (
    Blueprint,
)


module = Blueprint('service', __name__)

from .views import *
