import os
import tempfile

import pytest

from keeper import (
    create_app,
)


@pytest.fixture
def app():
    output_fd, output_path = tempfile.mkstemp()

    yield create_app({'DST_FILE': output_path})

    os.close(output_fd)
    os.unlink(output_path)


@pytest.fixture
def client(app):
    return app.test_client()
