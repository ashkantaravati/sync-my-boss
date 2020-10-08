# Codename : Sync My Boss

## Introduction

Organizational Information Flow Improvement and Agility Companion system

## Objectives

This software aims to empower organization in the following matters:

- Improving information sharing and open communication
- Improving trust
- Continuous Improvement
- Agility
- Managing virtual teams
- Effective Knowledge Management

## Technical Specifications
This web application is a django project, but relies on Vue.js and Axios for its UI especially for its partial refreshing and model binding.

### Software Dependencies

#### Server-side Dependencies
- django
- django-jalali
- djangorestframework

Of course each of these packages have their own dependencies.

#### Client-side Dependencies
- Bootstrap 4
- JavaScript Cookie Library
- Vuejs 3
- Axios


### Recommended/Required Development Tools

- Git ( no kidding :D )
- Black (recommended code formatter)
- Pylama ( recommended code audit tool)
- Visual Studio Code
- Pipenv (required)
- Python 3.8
- Pip (for installing pipenv)
- Pyenv (recommended for switching between python versions)

### Build and Test

There are currently no tests and no CI/CD pipeline.

## Setting Up

### Development Environment

1. Clone the repository
   e.g. :

```sh
git clone https://github.com/ashkantaravati/sync-my-boss
```

2. Get inside cloned project directory

```sh
cd sync-my-boss
```

3. Given you have pipenv installed, use it like this to create a virtual environment and install dependencies:

```sh
pipenv install --dev
```
4. Then activate the virtual environment using the following command:

```sh
pipenv shell
```
5. Now prepare the database using the commands below

```sh
python manage.py migrate # runs migrations, creating the database

python manage.py loaddata db.json # loads the seed data provided in db.json

python manage.py createsuperuser # if you want to create your own admin user
```

6. Now you should be able to run the project and use the admin site.

```sh
python manage.py runserver
```

#### default super user credentials:

`username: ashkan`

`password: 1234`

### Production Environment

This project is absolutely NOT production ready!
In order to prepare this project for porduction, at least the following needs to be done:

- Write some essential tests
- Refactor Vue apps as components
- Install client-side technologies using npm or yarn instead of using CDN sources.

## Releases
No Releases yet!

## Contribute

Pull Requests are welcome.

### Useful Resources for contributers
- [Installing pipenv using pip](https://pipenv-fork.readthedocs.io/en/latest/install.html#pragmatic-installation-of-pipenv)
- [Getting started with Django REST Framework](https://www.django-rest-framework.org/tutorial/quickstart/)
- [JavaScript Cookie Library Documentation](https://github.com/js-cookie/js-cookie/tree/latest#readme)
- [Introduction to Vue.js v3](https://v3.vuejs.org/guide/introduction.html)
- [About Django Cross Site Request Forgery protection](https://docs.djangoproject.com/en/3.1/ref/csrf/#module-django.middleware.csrf)
- [Axios README](https://github.com/axios/axios)
- [About Python virtual environments](https://realpython.com/python-virtual-environments-a-primer/)

### FAQ
1. Q: Why am I getting HTTP 403 58 response?

    A: Are you sure sending CSRF token in your request header? 
