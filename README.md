
# Ayen  
### Documentation:
[AWS-Link] (http://18.219.14.213/)
1. [Django](https://docs.djangoproject.com/en/2.0/releases/2.0/)
2. [Django Rest Framework](https://www.django-rest-framework.org/)


### Installation:

##### System Dependencies:

1. Install git on Linux:  
`sudo apt-get install -y git`
2. Clone or download this repo.
3. Install pip and vitualenv on Linux:  
`sudo apt-get install -y virtualenv`  
`sudo apt-get install -y python3-pip`
4. Create a virtual environment on Linux or Mac:  
`virtualenv -p python3 ~/.virtualenvs/ayen`
5. Activate the virtual environment on Linux or Mac:  
`source ~/.virtualenvs/ayen/bin/activate`
6. Install requirements in the virtualenv:  
`pip3 install -r requirements.txt`

##### Relational database dependencies (PostgreSQL):
1. Install components for Ubuntu:  
`sudo apt-get update`  
`sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib`
2. Switch to **postgres** (PostgreSQL administrative user):  
`sudo -u postgres psql`
3. Log into a Postgres session:  
`psql`
4. Create database with name **ayen**:  
`CREATE DATABASE ayen;`
5. Create a database user which we will use to connect to the database:  
`CREATE USER ayen_user WITH PASSWORD 'ayen_pass';`
6. Modify a few of the connection parameters for the user we just created:  
`ALTER ROLE ayen_user SET client_encoding TO 'utf8';`  
`ALTER ROLE ayen_user SET default_transaction_isolation TO 'read committed';`  
`ALTER ROLE ayen_user SET timezone TO 'UTC';` 
7. Give our database user access rights to the database we created:  
`GRANT ALL PRIVILEGES ON DATABASE ayen TO ayen_user;`
8. Exit the SQL prompt and the postgres user's shell session:  
`\q` then `exit`

9. Activate the virtual environment:  
`source ~/.virtualenvs/ayen/bin/activate`
10. Make Django database migrations:
`python manage.py makemigrations`  
then: `python manage.py migrate`

##### Use admin interface:
1. Run the project locally:  
`python manage.py runserver`
2. Navigate to: `http://localhost:8000/admin/`
 
 
### API Endpoints
##### Register
Method: `POST`  
Endpoint: `/registration/`  
Payload:  
`{  
    "email": "EMAIL",  
    "password1": "PASSWORD",  
    "password2": "PASSWORD",  
}`

##### Login
Method: `POST`  
Endpoint: `auth/login/`  
Payload:  
`{  
    "username": "USERNAME / EMAIL",  
    "password": "PASSWORD"  
}`

##### Logout
Method: `POST`  
Endpoint: `auth/logout/`  
Headers: `Authorization: JWT YOUR_TOKEN_HERE`  
