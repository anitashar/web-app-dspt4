# web-app-dspt4

## Deployed Website Link
https://twitoff-anita.herokuapp.com/

## Installation
TODO: instructions for git clone

## Setup
TODO: instructions for virtual environment

## To install virtual environment
Pipenv install

## To activate virtual env

Pipenv shell

## To install flask
pipenv install Flask Flask-SQLAlchemy Flask-migrate

## set up database:

    FLASK_APP=web_app flask db init #> generates app/migrations dir
    # run both when changing the schema:
    FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
    FLASK_APP=web_app flask db upgrade #> creates the specified tables
## Usage
### Mac:
FLASK_APP=hello.py flask run


after resetting the db fetch the data
http://localhost:5000/users/elonmusk/fetch

