Keeper
======
The basic app, intended for storing notifications incoming from external system

Install
-------
Installation tutorial assumes you are using any of GNU/Linux distribution,
and you are familiar with CLI.

Clone repo:
```
$ git clone https://git.ivnglkv.ru/ivnglkv/notifications-keeper.git
$ cd notifications-keeper
```

Create a virtualenv and activate it:

```
$ python3 -m venv venv
$ . venv/bin/activate
```

Install project, and it's dependencies to virtualenv:

```
$ pip install '.'
```

Copy configuration file:

```
$ cp hook.conf.example hook.conf
```

Then edit hook.conf. It has only one variable, that contains path
to target file, where program should write all incoming notifications

Run
---
```
$ export FLASK_APP=keeper
$ export FLASK_ENV=development
$ flask run
```

Application will listen on `127.0.0.1:5000`.

Endpoints
---------
```
/service/hook -- open only for POST requests, responsible for
    processing incoming notifications data, validating, and saving it
    in the system
```

Requests formats
----------------
`/service/hook` endpoint accepts data in following format
```
{
  "id": 1,
  "datetime": "2021-07-03T13:00:00.000+03:00",
  "type": "info",
  "message": "Something went well"
}
```
where all fields are required,
 - `id` must be an integer;
 - `datetime` must be RFC3339-compliant date;
 - `type` must be one of `"alert"`, `"error"`, `"warning"`, `"notice"`, `"info"` or `"debug"`;
 - `message` must be a string.

Test
----

```
$ pip install '.[test]'
$ pytest
```

Run with coverage report

```
$ coverage run -m pytest
$ coverage report
```
