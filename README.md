# Keeper
The basic app, intended for storing notifications incoming from external system

## Install
### Prerequisites
Installation tutorial assumes you are using any of GNU/Linux distribution,
and you are familiar with CLI.

You should have installed git, python3 and optionally wget on your machine.

#### Installation
```
$ git clone https://git.ivnglkv.ru/ivnglkv/notifications-keeper.git
$ cd notifications-keeper
$ git checkout v0.0.1
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install '.'
```

Copy example configuration file:

```
$ cp conf/keeper.conf.example conf/keeper.conf
```

Then edit `conf/keeper.conf`. It has only one variable, that contains path
to target file, where program should write all incoming notifications.
Just make sure, that your user have correct access write to desired destination.

# Run
```
$ export FLASK_APP=keeper
$ export FLASK_ENV=development
```
This should be full path to real configuration file, you created
on last installation step:
```
$ export HOOK_APP_CONFIG='/etc/keeper/keeper.conf'
$ flask run
```

Application will start on `127.0.0.1:5000`.

# Endpoints
```
/service/hook -- open only for POST requests, responsible for
    processing incoming notifications data, validating, and saving it
    in the system
```

# Requests formats
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

# Test

```
$ pip install '.[test]'
$ pytest
```

Run with coverage report

```
$ coverage run -m pytest
$ coverage report
```
