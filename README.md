# Cafe-Management-System-DJANGO
 This Repository consists of  Web Application which is Developed in Django (the framework of python)
 
 # Django Databse Settings
 
 settings.py
 
 ```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_admin_log',
        'USER' : 'root',
        'PASSWORD' : '',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}
```
 
 ## 1) Start XAMP server for MYSQL
following how xamp will looks like

![image](https://user-images.githubusercontent.com/80707427/161841017-8d302d2c-33f5-43b9-826b-38f1a0d86fcb.png)

 ## 2) Creating Database Tables
 
Makemigrations

```
python manage.py makemigrations <app_name>
```

Migrate

```
python manage.py migrate
```


 ## 3) Runserver of Web Application
 
 ```
 python manage.py runsever
 ```
 URL:
 ```
 http://127.0.0.1:8000
 ```
 
