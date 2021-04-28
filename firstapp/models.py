from firstapp import db

class User(db.Model):
    id = db.Column(db.Integer())
    name = db.Column(db.String(length=30),primary_key=True, nullable=False, unique=True)
    address = db.Column(db.String(length=100), nullable=False)