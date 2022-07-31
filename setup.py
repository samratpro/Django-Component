# Creating Invirment
python -m venv env

# Active envirment
Source scripts/env/activate


#Commands---------------------------------------
# Django install..
pip install django

# Django Project Create..
django-admin startproject "projectname"

# Django App Creating..
python manage.py startapp "appname"

# Server Running..
python manage.py runserver


## Commands
# For database update
python manage.py makemigrations
python manage.py migrate

# For Admin
python manage.py create superuser


# Important folders..
templates
static
