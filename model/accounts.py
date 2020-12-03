from model.db import db

class Accounts(db.Document):
    name=db.StringField()
    username=db.StringField()
    password=db.StringField()
    address=db.StringField()
    state=db.StringField()
    country=db.StringField()
    email=db.StringField()
    pan=db.StringField()
    contact=db.StringField()
    DOB=db.StringField()
    accounttype=db.StringField()