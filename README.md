# Deployment

[Django](https://www.djangoproject.com/) application using the Django Rest Framework [DRF](http://www.django-rest-framework.org).

```# clone the repo
git clone https://github.com/vinny-santaiti/toomanyflix.git

# go to folder
cd toomanyflix

# add virtualenv (supports python 2 or 3: pip install virtualenv)
# .env is the virtual env folder
virtualenv --python=python3.7 .env

# add virtualenv for python 3 only (python 2 is not installed) 
# venv is preinstalled with python3
python3 -m venv .env

# enter virtualenv
source .env/bin/activate

# install apps
pip install -r requirements.txt

# decide which database is needed
# and edit settings file to match your database installed
vi toomanyflix/settings.py

# setup database
python manage.py makemigrations
python manage.py migrate

# create superuser for admin login
python manage.py createsuperuser

# create static, only if configured in settings: STATIC_ROOT = os.path.join(BASE_DIR, "static/")
python manage.py collectstatic

# run tests
python manage.py test

# run django
python manage.py runserver
```



