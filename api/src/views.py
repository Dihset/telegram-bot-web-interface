import time
from flask import request
from flask_restful import Resource
from .models import User, Message
from .repositories import UserRepository, MessageRepository
from .utils import row_to_dict


class TelegramHookView(Resource):
    

    def post(self):
        data = request.get_json()
        user_dict = data['message']['chat']
        user = User(
            user_dict.get('id'),
            user_dict.get('username'),
            user_dict.get('first_name'),
            user_dict.get('last_name'),
            user_dict.get('language_code')
        )
        if not UserRepository.is_exist(user):
            UserRepository.save(user)
        message = {
            "pk": data['message']['message_id'],
            "user_id": user_dict['id'],
            "from_id": data['message']['from']['id'],
            "date": data['message']['date'],
            "text": data['message']['text']
        }
        MessageRepository.save(Message(**message))
        return 'ok', 201


class DialogListView(Resource):
    

    def get(self):
        users = UserRepository.get_all()
        users_dict = [row_to_dict(user) for user in users]
        return users_dict, 200


class DialogView(Resource):
    

    def get(self, user_id):
        messages = MessageRepository.get_by_user_id(user_id)
        messages_dict = [row_to_dict(mess) for mess in messages]
        return messages_dict, 200

    def post(self, user_id):
        data = request.get_json()
        text = data['text']
        MessageRepository.send_message(user_id, text)
        pk = MessageRepository.get_last_pk() + 1
        MessageRepository.save(
            Message(
                pk=pk,
                user_id=user_id,
                from_id=0,
                date=int(time.time()),
                text=text
            )
        )
        return 'ok', 201
