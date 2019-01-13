import threading, requests, json

from src import db
from src.models import ISSLocation

class ApiPoll:
    """  
        This class is responsible for polling the ISS database and 
        saving a record on a seperate thread using the ISSLocaiton Model
    """

    def __init__(self, poll_delay):
        self.poll_thread = threading.Timer(poll_delay, self.poll)
        self.poll_thread.start()


    def poll(self): 
        try:
            self.poll_api()
            self.poll_thread.run()
        except Exception as err: 
            print('ERROR: Failed to poll ISS api -', err.args )
            self.poll_thread.cancel()

        
    def poll_api(self):
        data = requests.get('http://api.open-notify.org/iss-now.json').json()

        timestamp = data['timestamp']
        longitude = data['iss_position']['longitude']
        latitude = data['iss_position']['latitude']
        
        # Save location record
        try:
            db.session.add(ISSLocation(timestamp=timestamp, lon=longitude, lat=latitude))
            db.session.commit()
        except Exception as err:
            print('ERROR: Failed to save location record - ', err.args)

       
