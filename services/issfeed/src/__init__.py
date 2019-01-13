import os 
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy



print('Starting ISSFEED service...')

# Create Flask APP
app_settings = os.getenv('APP_SETTINGS')

app = Flask(__name__)
app.config.from_object(app_settings)

# Create DB 
db = SQLAlchemy(app)

from src.api.location import location_blueprint
app.register_blueprint(location_blueprint)


from src.apipoll import ApiPoll
# Create ISS API poller and start polling
iss_poll = ApiPoll(10)

db.drop_all()
db.create_all()
db.session.commit()


print('ISSFEED service running ...')