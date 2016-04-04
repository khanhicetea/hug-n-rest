# :open_hands: & :relieved:

![Hug](https://camo.githubusercontent.com/ab5da64e2ce2f330820f29b95a932e3077a09eb6/68747470733a2f2f7261772e6769746875622e636f6d2f74696d6f74687963726f736c65792f6875672f646576656c6f702f617274776f726b2f6c6f676f2e706e67)

## Introduction

`Hug-n-Rest` is a micro framework for RESTful API based on [Hug](https://github.com/timothycrosley/hug).

## Usage

```shell
$ virtualenv -p python3 venv
$ source venv/bin/active
$ pip install -r requirements.txt
$ python manage.py db upgrade head
$ gunicorn --reload app:__hug_wsgi__
```

## Demo

```shell
http POST :8000/api/v1/groups name=Group1 alias=g1 max_members=123
http POST :8000/api/v1/groups name=Group2 alias=g2
http :8000/api/v1/groups

http POST :8000/api/v1/users name="Khanh Ice Tea" fullname="Khanh Nguyen" email="khanhicetea@gmail.com" password="123456" group_id=2
http POST :8000/api/v1/users name="Chuck Norris" fullname="Chuck norris" email="chuck_norris@gmail.com" password="nobody" group_id=1
http :8000/api/v1/users
```
