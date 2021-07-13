from keeper import create_app


def test_config():
    assert create_app().config.get('DST_FILE')
