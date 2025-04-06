###Implementation Steps for Scenario 2 

1.Set up virtual environment
python -m venv s2vm
.\s2vm\Scripts\activate

2.Package Installation

#Install django & djangorestframework
pip install django 
pip install django djangorestframework 

3. Create Django Project
django-admin startproject s2api

4.Create Django Web App in s2api project
python manage.py startapp s2app

5. Register s2api App in s2api/settings.py
INSTALLED_APPS = [
    ...,
    'rest_framework',
    's2app',
]

6. Setup Database Connection (in s2api/setting.py) 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', #'django.db.backends.sqlite3',
        'NAME': 'dbs2projectcatalog', #Create 'dbs2projectcatalog' in PgAdmin4
        'USER': 'userone', 	          #Input the db username
        'PASSWORD': 'Luckymnmyo',     #Input the db password
        'HOST': 'localhost',
        'PORT': '5432',

    }
}

7.Install the db connector to postgresql
pip install psycopg2	


8.Model Development
-Model for Project Information (mdlProject)
-Geographic Model of Projects (mdlGeo)
-Project Type (mdlPType)
-Project Charter Model (mdlPCharter)
-Project Deliverable (mdlPDeliverable)

9.Update database by creating model instance tables via s2api
python manage.py makemigrations
python manage.py migrate

10.Develop Model Serializers & View for Data Handling
11.Specify URL Patterns
12.Test API successfully
python manage.py runserver
