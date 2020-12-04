# Reactor Labs

Djangofied Bootstrap Template

![featured-image](https://raw.githubusercontent.com/jqn/reactorlabs/master/static/images/djangofy-blog.png)

## Getting Started

### Requirements

- Python 3.8 & up
- Virtual Environment (virtualenv)
- Virtual Environment Wrapper (virtualenvwrapper)

1. Clone this repo

```
$ git clone https://github.com/jqn/reactorlabs.git
```

2. Create Virtual Environment & Install Django

```
$ cd reactorlabs
$ mkvirtualenv reactorlabs
```

3. Add your environment variables to postactivate

```
$ vi ~/.virtualenvs/reactorlabs/bin/postactivate`
```

```
#!/bin/bash
# This hook is sourced after this virtualenv is activated.
export DB_HOSTNAME='localhost'
export DB_NAME='reactorlabs'
export DB_USERNAME='dbuser'
export DB_PASSWORD='dbpass'
export DB_PORT='3306'
```

4. Set up your Database

Create a new database with mysql-cli or application of your choice and name it `reactorlabs`

5. Run your server and test things out

```
$ python manage.py runserver
```
