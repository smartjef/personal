This web application is built in Django, a python framework.
## Steps taken
1. Modeling the database.
I first designed and modelled the database, i.e., Identifying and noting down the required tables and required fields.
I there after normalized the database.
2. Decided on framework to use:
I there after went into the second phase of choosing the best framework to use for my work. In which I chased Django due to its features such as security, speed and scalability.
3. Started Implementing the app by creating a portfolio app.

- I installed `python` and `pip`, I later used pip to install `virtualenv`.
- Created a virtual environment for my app 
```
virtualenv env
```
- Activated the environment
```
source env/bin/activate
```
- For Windows:
```
.\env\Scripts\activate
```
- Installed django in the environment
`pip install django` and started project portfolio `django-admin startproject portfolio .` then `python manage.py migrate`. thereafter I started working on my web application.

4. Deciding on the database to use on production
- I decided to use postgres database as it is best for production.
- Used sqlite for development environment

5. Deciding on where to deploy the app.
- I used Microsoft azure to deploy my application
