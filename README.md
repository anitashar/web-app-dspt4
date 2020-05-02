# web-app-dspt4

Installation
TODO: instructions for git clone

Setup
TODO: instructions for virtual environment

To install virtual environment
Pipenv install

To activate virtual env

Pipenv shell

To install flask
pipenv install Flask Flask-SQLAlchemy Flask-migrate

set up database:

    #> generates app/migrations dir
    FLASK_APP=web_app flask db init 

    # run both when changing the schema:
    #> creates the db (with "alembic_version" table)
    FLASK_APP=web_app flask db migrate 

 #> creates the specified tables
    FLASK_APP=web_app flask db upgrade
Usage
# Mac:
FLASK_APP=hello.py flask run


after resetting the db fetch the data
http://localhost:5000/users/elonmusk/fetch

