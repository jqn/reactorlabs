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

### Resources

**Content**

- [Ipsum generator list](https://www.shopify.com/partners/blog/79940998-15-funny-lorem-ipsum-generators-to-shake-up-your-design-mockups)

**Templates**

https://getbootstrap.com/docs/4.0/examples/blog/

https://github.com/twbs/bootstrap/blob/master/site/content/docs/5.0/examples/blog/index.html

https://github.com/twbs/bootstrap/blob/main/site/content/docs/5.0/examples/cover/index.html

https://getbootstrap.com/docs/4.0/examples/dashboard/

https://github.com/twbs/bootstrap/tree/master/site/content/docs/5.0/examples/dashboard

https://github.com/rhazdon/hugo-theme-hello-friend-ng

**Tutorials**

- [Setup VS Code for Django](https://automationpanda.com/2018/02/08/django-projects-in-visual-studio-code/)

- [Real Python - Getting Started With Django](https://realpython.com/
  get-started-with-django-1/)

- [Categories and list views](https://www.agiliq.com/blog/2017/12/when-and-how-use-django-listview/)

- [Django REST with React](https://www.valentinog.com/blog/drf/)

**Repos**

- [djangoforbeginners](https://github.com/wsvincent/djangoforbeginners)

- [djangoforprofessionals](https://github.com/wsvincent/djangoforprofessionals)

- [Real Python - Personal Portfolio](https://github.com/realpython/materials/tree/4dd5d79634efbffeb8999052a9e94b3dba4b25ba/rp-portfolio)

- [Coding For Entrepreneurs](https://github.com/codingforentrepreneurs)

- [Marked](https://github.com/markedjs/marked/blob/master/docs/demo/quickref.md)
