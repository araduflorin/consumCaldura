from consumCald import db
from datetime import datetime

class Caldura(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    caloriferSufr = db.Column(db.Integer(), nullable=False)
    caloriferBuc = db.Column(db.Integer(), nullable=False)
    caloriferDormitorMic = db.Column(db.Integer(), nullable=False)
    caloriferDormitorMare = db.Column(db.Integer(), nullable=False)
    caloriferBaie = db.Column(db.Integer(), nullable=False)
    caloriferWC = db.Column(db.Integer(), nullable=False)
    dataConsum = db.Column(db.DateTime, nullable=False, default=datetime.utcnowCal)
