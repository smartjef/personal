## About

This is a personal web applications that has Homepage, About page, Contacts, Resume and Portfolio.
It is built in Django(a python framework) and uses bootstrap 5 and jQuery. The backend and database are fully built and the application is fully dynamic.

### Fields:
#### Homepage
On the homepage we return Reviews dynamically and provides a url that a user can use to add/leave a review.

#### About Page
On this page we dynamically return data from the database with fields {title, description}

#### Contacts Page
Provide contact information such as link to social accounts and a form that can be used to send a feedback.

## How to get started with the app

1. **Install python3**
If you don't have python installed on your machine its recommended you install it. For windows users you can download `.exe` file from the official page.
[https://www.python.org/downloads/](https://www.python.org/downloads/). For linux user, its usually pre-installed or use `sudo apt install python3` to install.

2. **Install pip or pip3**
To install pip run `sudo apt install pip` or `sudo apt install pip3`

3. **Install virtualenv**
Use pip to install virtual environment, i.e `pip install virtualenv`

4. **Create a virtual environment for the app**
To start virtual environment run `virtualenv env`

5. **Activated virtual environment**
To activate your environment run `source env/bin/activate` for linux or `env\Scripts\activate` for windows after that you can clone the app by running `git clone https://github.com/smartjef/personal.git` and `cd` into the project folder.

6. **Install requirements**
 Run `pip install -r requirements.txt`

7. **Make migrations**
   Run `python manage.py makemigrations`

8. **Apply Changes to the database**
   Run `python manage.py migrate`

9. **Create Superuser**
   Run `python manage.py createsuperuser` and fill the required fields such as username, password and email.

10. **Run server/Start the app**
Run `python manage.py runserver` to start the server

11. **Preview**
The default port is 8000, to view your app open [http://127.0.0.1:8000](http://127.0.0.1:8000)


Homepage:
![Homepage](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/07ptmpxjc51bf4ftpl7j.png)

ContactPage:
![Contactpage](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/46r3huxl13b1a94ktq6j.png)
 
Requesting for collaborators on the project below
{% embed https://github.com/smartjef/vstech-academy.git %}