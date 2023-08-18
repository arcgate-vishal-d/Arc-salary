**Note** -

Install python 3.10.4 version

set this version as global 

## install vierualenv

        python3 -m pip install --user virtualenv

## Create virtual enviorment 

        make env
        
## Activate virtual enviorment

        source env/bin/activate




## Python management commands 
    - make run = python manage.py runserver
    - make migrations = python manage.py makemigrations
    - make migrate = pyhton manage.py migrate
    - make superuper
    **NOTE** - All the commands should use from root folder


## environment variable setup

        Keep all non sharable information in .env
        pip install django-environ
        or 
        pip install -r requirement.txt
##### Create .env.example 
        Create a .env.example file in the root directory where requirement.txt resides and add the following key-value pair inside the file.
        
## Sentry setup
        pip install sentry-sdk
        or 
        pip install -r requirement.txt

## Install django and django rest framework

        pip install django
        pip install djangorestframework


## install JWT and cors header

        pip install djangorestframework-simplejwt
        pip install django-cors-headers

## Unit Testing
        view dummy test cases and write accordingly
        
