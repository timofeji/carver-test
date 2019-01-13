from src import db


class ISSLocation(db.Model):
    __tablename__ = "isslocation"
    timestamp = db.Column(db.Integer, nullable=False, primary_key=True)
    lon = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)

    def __init__(self, timestamp, lon, lat):
        self.timestamp = timestamp
        self.lon = lon
        self.lat = lat


    def to_json(self):
        return {
            'timestamp': self.timestamp,
            'lon': self.lon,
            'lat': self.lat
        }

