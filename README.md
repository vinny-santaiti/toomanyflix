### Deployment

[Django](https://www.djangoproject.com/) application using the Django Rest Framework [DRF](http://www.django-rest-framework.org).

```# clone the repo
git clone https://github.com/vinny-santaiti/toomanyflix.git

# go to folder
cd toomanyflix

# add virtual env
virtualenv --python=python2.7 env

# enter env
source env/bin/activate

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

# create static, only if configured in settings
python manage.py collectstatic

# run tests
python manage.py test

# run django
python manage.py runserver
```



