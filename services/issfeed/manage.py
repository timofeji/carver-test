from flask.cli import FlaskGroup
from src import app, db

cli = FlaskGroup(app)

if __name__  == '__main__':
    cli()