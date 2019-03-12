from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import time


db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'
    pk = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    language_code = Column(String)
    
    def __init__(self, pk, username=None, first_name=None, last_name=None, language_code=None):
        self.pk = pk
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.language_code = language_code

class Message(db.Model):

    __tablename__ = 'messages'
    pk = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.pk'), nullable=False)
    from_id = Column(Integer, ForeignKey('users.pk'), nullable=False)
    date = Column(DateTime, nullable=False)
    text = Column(String, nullable=False)

    def __init__(self, pk, user_id, from_id, date, text):
        self.pk = pk
        self.user_id = user_id
        self.from_id = from_id
        self.date = time.ctime(date)
        self.text = text
