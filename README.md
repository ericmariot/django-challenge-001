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

Enter the clonde repo and migrate the tables with:
- ```$ python manage.py migrate```

Run the virtual enviroment:
- ```$ pipenv shell```

Install Pillow:
- ```$ pip install Pillow```

Install packages from Pipfile:
- ```$ pipenv install```

Change the SECRET_KEY on the config/settings.py for a secret key, you can use this webiste [djecrety](https://djecrety.ir/) to generate a key, then copy and paste 
to the 'SECRET_KEY = "secret_key_goes_here"'. Change the SECRET_KEY to run on production.

Run the server:
- ```$ python manage.py runserver```

See if it works [here](http://localhost:8000/api/articles/) if running in port :8000, or making a request in insomnia or some other program of your preference, a list of
endpoints can be found in the 'newsprovider/urls.py', everyone one of them starts with '/api/'

## How to run the application in a Docker container for production
[TODO]

## API collection
Insomnia collection as a file (django-challenge-001-insomnia)

## API documentation
You can access locally, after running ```python manage.py runserver``` from:

Swagger - http://localhost:8000/swagger/ || Redoc - http://localhost:8000/redoc/

## Links that helped me
 - [Classy DRF](https://www.cdrf.co/)
 - [DRF Documentation](https://www.django-rest-framework.org/)
 - [Django Documentation](https://docs.djangoproject.com/en/3.2/)
