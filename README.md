# Financial Application programming interface (API)
Using Python, Django, and Django REST framework (DRF) to create financial api to allow users to create and list the finanacial transactions. 

## Installation Guide 
Welcome to the installation guide for financial api. This guide will walk you through the steps to set up and run our Python-based Django project using Django Rest Framework (DRF) on Visual Studio Code (VS Code) or any source code editor .

### Prerequistes:
Before you begin, ensure you download python and make sure it's added to your system's PATH.

-- Create directory in any place on your pc and open it in gitbash and write **code .** to open the directory in VS code.

#### In VS code terminal 
Start to install 
1- Virtual environment:
write **python -m virtualenv venv** venv --> virtual environment name.
and activate it by **venv\Scripts\activate**.
To deactivate :
**deactivate**

Now, you install and set all dependencies in virtual environment not in local device.

2- install Django 
Pip install django

3- Create Django project
django-admin startproject nameofproject .
 
4- create django app
  django-admin startapp <nameofapp>

when you write in terminal:
python manage.py runserver 
you can find the webpage with a successful install message is displayed.

<img src="1- runserver.png">


Now you create your the server.

In settings.py In settings.py file in root directory, define your app project by writing project name.
by adding the appname in INSTALLED_APPS 
like this.


<img src="2- app configuration in settings.py file.png">


.
START to create the functions of API.

In our project we use **MVT architecture** , it is Abbreviation of Model, View, and Template (MVT) approach.


<img src="3- MVT architecture .png">


In this approach, a Django application consists of the following components:

- **URL dispatcher**: Responsible for routing incoming HTTP requests to the appropriate view function based on the URL patterns defined in your Django project.

- **View**: Handles the logic for processing requests and returning responses. Views interact with models to retrieve and manipulate data and render templates to generate HTML responses.

- **Model**: Represents the application's data and business logic. Models define the structure of database tables and provide an abstraction layer for database operations.

- **Template**: Defines the structure and layout of the final HTML output sent to the user's browser. Templates include placeholders for dynamic content and are used by views to render HTML responses.

___________________________________________________________________________________
# Endpoints

Endpoint 1: /trans_list/
this endpoint allow users to list all financial transactions.

Endpoint 2: /trans_create/
allow users to create financial transaction, each transaction should have fields:
transaction_date, description, amount, category, user_id, currency_type, location, payment_method.

Endpoint 3: /trans_retrieve/<pk>/
Allow users to retrieve individual financial transactions based on their unique IDs.

Endpoint 4: /trans_update/<pk>/edit/
allow users to update individual financial transactions based on their unique IDs.

Endpoint 5: /list_all_categories/<str:category>/
to list all available transaction categories by writting category name.

Endpoint 6: /user_create/
To create new user and each user should have fields:
user_id, first_name, last_name, phone, email, password.

Endpoint 7: /api/users/
To list all Registered users.

Endpoint 8: /api/users/<user_id>/transactions/
Allow users to retrieve their own transactions based on user ID.

Endpoint 9: /api/reports/<str:user_id>/
Generates monthly financial report summary of transaction for each specific user using ID.

Endpoint 10: /register/
To allow new user to register and enter all his/her information, to store it in database.

Endpoint 11: /login/
Allow user to enter in protected pages after confirming his/her information is in database.

