from keeper.service.enums import (
    HttpStatusCodesEnum as Status,
)


def test_hook(client):
    hook_path = '/service/hook'

    test_data = [
        {
            'data': {'id': 1, 'datetime': '2021-07-03T13:00:00.000+03:00', 'type': 'info', 'message': 'Check-check'},
            'status_code': Status.OK.value,
            'result': 'OK',
            'messages': False,
        },
        {
            'data': {},
            'status_code': Status.SERVER_ERROR.value,
            'result': 'Error',
            'messages': True,
        }
    ]

    for test in test_data:
        post_result = client.post(hook_path, json=test['data'])
        post_result_json = post_result.get_json()

        assert post_result.status_code == test['status_code']
        assert post_result_json.get('result') == test['result']
        assert bool(post_result_json.get('messages')) == test['messages']
