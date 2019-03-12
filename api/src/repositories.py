import requests as req
from sqlalchemy.sql import func
from .models import User, Message, db


class UserRepository:


    @staticmethod
    def save(user: User):
        db.session.add(user)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return [user for user in User.query.filter(User.pk != 0)]

    @staticmethod
    def is_exist(user: User):
        if User.query.filter_by(pk=user.pk).first():
            return True
        else:
            return False


class MessageRepository:


    @staticmethod
    def save(message: Message):
        db.session.add(message)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id):
        return [message for message in Message.query.filter_by(user_id=user_id)]

    @staticmethod
    def send_message(user_id, text):
        req.post(
            'https://api.telegram.org/bot639381913:AAF2kHmbSvIGGDOJNj1-1alwuJRhEsijeMU/sendMessage',
            data={
                'chat_id': user_id,
                'text': text
            }
        )

    @staticmethod
    def get_last_pk():
        return db.session.query(func.max(Message.pk)).scalar()
