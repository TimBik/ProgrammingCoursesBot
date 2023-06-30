from aiogram import types

from tg_bot.models.User import User
from tg_bot.repository.UserRepository import UserRepository
from tg_bot.utils import PhoneNumberFormat
from tg_bot.utils.Roles import Roles


class UserService:

    @staticmethod
    def find_user_by_application(application):
        user = UserRepository.get_user_by_user_tg_id(application.for_user_tg_id)
        return User(user) if user is not None else None

    @staticmethod
    def get_user_by_user_tg_id(user_tg_id):
        return User(UserRepository.get_user_by_user_tg_id(user_tg_id))

    @staticmethod
    def update_user_by_tg_user_id(tg_user_id, user):
        UserRepository.update_user_by_tg_user_id(tg_user_id, user)

    @staticmethod
    def create_user_without_phone_by_message_if_doesnt_exist(message):
        user = UserRepository.get_user_by_user_tg_id(message.from_user.id)
        if user is None:
            user = UserService.create_anonim_user_by_message_without_number(message)
            UserRepository.add_user(user)
        else:
            user = User(user)
        return user

    @staticmethod
    def create_anonim_user_by_message_without_number(message: types.Message):
        return UserService.create_user_by_message_without_phone(message, Roles.INCOGNITA)

    @staticmethod
    def create_anonim_user_by_message(message: types.Message):
        user = UserService.create_anonim_user_by_message_without_number(message)
        user.number = PhoneNumberFormat.number_format(message.contact.phone_number)
        return user

    @staticmethod
    def create_user_by_message_without_phone(message: types.Message, role):
        return User({
            'number': None,
            'role': role,
            'user_name': message.from_user.username,
            'name': message.from_user.first_name,
            'surname': message.from_user.last_name,
            'tg_user_id': message.from_user.id
        })

    @staticmethod
    def create_user_by_message(message: types.Message, role):
        user = UserService.create_user_by_message_without_phone(message, role)
        user.number = PhoneNumberFormat.number_format(message.contact.phone_number)
        return user

