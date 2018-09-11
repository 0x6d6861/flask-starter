from sqlalchemy.ext.hybrid import hybrid_property

from . import db
# from .User import User

vtypes = {
    'c': "Comfort",
    'b': "Basic",
    'cp': "Comfort Plus",
    'g': "Goods",
    'boda': "Boda Boda"
}

ttypes = {
    'corp': "Corporate",
    'indv': "Individual"
}

class Trip(db.Model):
    __tablename__ = "trips"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    tripid = db.Column(db.String(100))
    from_ = db.Column(db.String(100))
    to_ = db.Column(db.String(100))
    vtype = db.Column(db.String(10))
    ttype = db.Column(db.String(20))
    distance = db.Column(db.Float)
    time = db.Column(db.Float)
    total = db.Column(db.Float)

    user = db.relationship("User")

    @hybrid_property
    def vehicle_type(self):
        return vtypes.get(self.vtype);

    @hybrid_property
    def trip_type(self):
        return ttypes.get(self.ttype);

    def __init__(self, tripid, from_, to_, vtype, ttype, distance, time, user_id):
        self.tripid = tripid
        self.from_ = from_
        self.to_ = to_
        self.vtype = vtype
        self.ttype = ttype
        self.distance = distance
        self.time = time
        self.user_id = user_id

    def __repr__(self):
        return '<Trip: {}>'.format(self.tripid)
