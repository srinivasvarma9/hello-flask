from flask_mongoengine import MongoEngine

db = MongoEngine()

def initilaize_db(app):
    db.init_app(app)