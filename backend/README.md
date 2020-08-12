## Setup & Install
```
cd school
```
```
virtualenv .env
```
```
source .env/bin/activate
```
```
pip install django==2.2.13 djangorestframework django-cors-headers
```

## Run backend
```
python manage.py runserver
```
API URL: http://127.0.0.1:8000/api/students/