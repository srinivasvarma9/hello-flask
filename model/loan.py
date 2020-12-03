from model.db import db

class Loan(db.Document):
    loantype=db.StringField()
    loanamount=db.StringField()
    date=db.StringField()
    rateofinterest=db.StringField()
    durationofloan=db.IntField()
    username=db.StringField()