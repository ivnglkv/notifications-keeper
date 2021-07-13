from keeper.service.notification.validator import (
    validate_incoming_notification,
)


def test_validate_notification():
    valid_id = 1
    invalid_id = '1'
    valid_date = '2021-07-03T13:00:00.000+03:00'
    invalid_date = '2021-07-03'
    valid_type = 'info'
    invalid_type = 'inf'
    valid_message = 'Ff'
    invalid_message = None

    test_data_and_expectations = [
        {
            'data': {'id': valid_id, 'datetime': valid_date, 'type': valid_type, 'message': valid_message},
            'result': True,
            'messages': [],
        },
        {
            'data': {},
            'result': False,
            'messages': [
                "'id' is a required property",
                "'datetime' is a required property",
                "'type' is a required property",
                "'message' is a required property",
            ],
        },
        {
            'data': {'id': invalid_id, 'datetime': invalid_date, 'type': invalid_type, 'message': invalid_message},
            'result': False,
            'messages': [
                "is not of type 'integer'",
                "is not a 'date-time'",
                "is not one of ['alert', 'error', 'warning', 'notice', 'info', 'debug']",
                "is not of type 'string'",
            ]
        }
    ]

    for example_notification in test_data_and_expectations:
        data = example_notification['data']
        expected_result = example_notification['result']
        expected_messages = example_notification['messages']

        result, messages = validate_incoming_notification(data)

        assert result == expected_result
        assert len(expected_messages) == len(messages), "Got wrong number of validation error messages"

        for msg in expected_messages:
            assert any(msg in m for m in messages), f"Can't find error message by pattern {msg}"
