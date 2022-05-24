# Django-Component
" " quotation has been used for custom variable name, Ignore ""

## Commands---------------------------------------
### Django install...
pip install django

### Django Project Create..
django-admin startproject "projectname"

### Django App Creating...
python manage.py startapp "appname"

### Server Running...
python manage.py runserver

### Database migrate...
python manage.py migrate

### Important folders...
templates
static



## Setting ------------------------------------------
### Template Connection...
BASE_DIR / 'templates'

### App connection...
INSTALLED_APPS = [
    'NewApp',
]

### Static File Connection...
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]


### URL Mapping in Project URL file-------------------
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('NewApp.urls')),
]  # NewApp is App name here...



### URL Mapping in App URL file----------------------
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')  
] #Home is function name here...


## Views File Output-------------------------------
from django.http import HttpResponse # Only for Python Function Output...
from django.shortcuts import render

def function_name(arg):
  operation = arg
  return operation

def home(request):
    template = 'NewApp/home.html'
    
    if request.method == 'GET' and 'city_search' in request.GET:        # Get alternative is POST...
        input_data = request.GET.get('city_search')                     # city_search form name of HTML input...
        result = function_name(input_data)                              # function_name is a function...   
        contex = {'result':result}
    else:
        contex = {}  
    return render(request, template, contex) # Return for Templates
  
  
  
## Templates-----------------------------------
### Extend...
{% extends 'base/dashboardbase.html' %}

### Load static file...
{% load static %}
{% static 'css/style.css' %} # CSS url
{% static 'imgs/name.png' %} # Image Url

### Block content...
{% block content %}
{% endblock content %}

### Daynamic Url...
{% url 'home' %} #Home is Render Function name

### Current URL condition...
{% if request.resolver_match.url_name == "urlname" %} actv {% endif %} # urname is URL's Function name and actv is HTML class or can be anything of HTML

### If condition...
{% if result %} # Result is Context Dictionary Key
{% endif %}

### For Loop list...
https://fedingo.com/how-to-loop-through-list-in-django-template/

## Data input Post Method...
<form action="" method="post" class="d-flex w-75 dashboard-search mt-3">
    {% csrf_token %}
    <input type="search" name="kwfinder" id="" class="form-control w-75 rounded-0 rounded-start" placeholder="{% if not request.POST %}Enter Sheet Keyword{% endif %}{% if request.POST %}{{result.search_box}}{% endif %}">
    <select name="intention" class="form-select rounded-0 border-start-0 " aria-label=".form-select-lg example">
        <option selected>Intention</option>
        <option value="info">Info</option>
        <option value="review">Review</option>
    </select>
    <select class="form-select rounded-0 border-start-0 " aria-label=".form-select-lg example">
        <option selected>Country</option>
        <option value="US">US</option>
    </select>
    <input type="submit" name="Search" value="Search" class="btn btn-success fs-6 rounded-0 rounded-end">
  </form>

### Data input Get Method...
<form action="" method="get"> <input type="submit" value="Search" name='input_name' class="btn btn-success fs-6 rounded-0 rounded-end"> </form>

