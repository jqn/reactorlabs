#Migrations

Before doing any inital migrations make sure the users migration is complete.

```
$ python manage.py makemigrations users
$ python manage.py mkigrate users
$ python manage.py makemigrations leads orders pages shop
$ python manage.py migrate
```