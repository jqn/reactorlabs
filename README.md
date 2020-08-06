# Reactor Labs

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
export RDS_HOSTNAME='localhost'
export RDS_DB_NAME='reactorlabs'
export RDS_USERNAME='dbuser'
export RDS_PASSWORD='dbpass'
export RDS_PORT='3306'
```

4. Set up your Database

Create a new database with mysql-cli or application of your choice and name it `reactorlabs`

### Resources

**Templates**

https://getbootstrap.com/docs/4.0/examples/blog/

https://github.com/twbs/bootstrap/blob/master/site/content/docs/5.0/examples/blog/index.html

https://getbootstrap.com/docs/4.0/examples/dashboard/

https://github.com/twbs/bootstrap/tree/master/site/content/docs/5.0/examples/dashboard

**Tutorials**

https://github.com/wsvincent/djangoforbeginners

https://realpython.com/get-started-with-django-1/
