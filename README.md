# Jungle Devs - Django Challenge #001
## Overview
This is a simplified version of a news provider API. It has a CRUD for 'Authors' and 'Articles', only usable for administrators, sign-up, login, filter by category and
articles by id, showing different responses if the user is authenticated or not.

## How to run the application in development mode
requirements = 'python_version = "3.9"'

Install or upgrade pip
 - ```$ python -m pip install --upgrade pip```

Install pipenv for easier packages installation:
 - ```$ pip install pipenv```

Go into your prefered directory and clone the repo:
- ```$ git clone https://github.com/ericmariot/django-challenge-001.git```

Enter the cloned repo and start the virtual enviroment:
- ```$ pipenv shell```

Install packages from Pipfile:
- ```$ pipenv install```

Create a new SECRET_KEY, it can be done with this wonderful website [djecrety](https://djecrety.ir/), once generated set the SECRET_KEY as an environment variable, likewise:
- ```$ export SECRET_KEY=EXAMPLE_hah4vr21aewaa3ewh*#9@ca2_+houa*a06n7ebb@c@```

___ATTENTION!___ Use a different SECRET_KEY to run on production.

Create another env var for DEBUG:
- ```$ export DEBUG=1```

___ATTENTION!___ To run for production set: ```$ export DEBUG=0```

Migrate the tables with:
- ```$ python manage.py migrate```

Run the server:
- ```$ python manage.py runserver```

See if it works [here](http://localhost:8000/api/articles/), if running in port :8000, or making a request in [insomnia](https://insomnia.rest/) or some other program of your preference.

## How to run the application in a Docker container for production
[TODO]

## API collection
Insomnia collection as a file (django-challenge-001-insomnia).

## API documentation
You can access locally, after running ```python manage.py runserver``` from the [Documentation](http://localhost:8000/swagger/) endpoint.

## Links that helped me
 - [Classy DRF](https://www.cdrf.co/)
 - [DRF Documentation](https://www.django-rest-framework.org/)
 - [Django Documentation](https://docs.djangoproject.com/en/3.2/)
 - [Insomnia](https://insomnia.rest/)
 - [djecrety](https://djecrety.ir/)