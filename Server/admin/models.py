from flask_sqlalchemy import SQLAlchemy
from routes import app

db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __str__(self):
        return self.name
    
class Conversations(db.Model):
    __tablename__ = 'conversations'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String)
    answer = db.Column(db.String)