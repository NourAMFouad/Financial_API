# Financial Application programming interface (API)
Using Python, Django, and Django REST framework (DRF) to create financial api to allow users to create and list the finanacial transactions. 

## Installation Guide 
Welcome to the installation guide for financial api. This guide will walk you through the steps to set up and run our Python-based Django project using Django Rest Framework (DRF) on Visual Studio Code (VS Code) or any source code editor .

### Prerequistes:
Before you begin, ensure you download python and make sure it's added to your system's PATH.

-- Create directory in any place on your pc and open it in gitbash and write ##code . ## to open the directory in VS code.

#### In VS code terminal 
Start to install 
1- Virtual environment:
write ## python -m virtualenv venv ## venv --> virtual environment name.
and activate it by ## venv\Scripts\activate ##
To deactivate :
deactivate

Now, you install and set all dependencies in virtual environment not in local device.

2- install Django 
Pip install django

3- Create Django project
django-admin startproject nameofproject .
 
4- create django app
  django-admin startapp <nameofapp>

when you write in terminal:
python manage.py runserver 
you can find this
<img src="D:\My_courses\web_backend\Screenshot 2023-09-21 170734.png">

Now you create your and run the server.

In settings.py In settings.py file in root directory, define your app project by writing project name.
by adding the appname in INSTALLED_APPS 
like this 
<img src="D:\My_courses\web_backend\Screenshot 2023-09-21 170821.png">

START to create the functions of API.

In our project we use ## MVT architecture ## , it is Abbreviation of Model, View, and Template (MVT) approach.
<img src="D:\My_courses\web_backend\Screenshot 2023-09-21 171122.png">

in this approach,  Django application consists of the following components: 
    .URL dispatcher 
    .View 
    .Model 
    .Template 



