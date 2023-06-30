from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import Filter

from tg_bot.services.UserService import UserService
from tg_bot.utils.Roles import Roles


class AnyUserFilter(Filter):
    async def check(self, message: types.Message) -> bool:
        user = UserService.create_user_without_phone_by_message_if_doesnt_exist(message)
        return user is not None


class IsSupportUserFilter(Filter):
    async def check(self, message: types.Message) -> bool:
        user = UserService.create_user_without_phone_by_message_if_doesnt_exist(message)
        return user is not None and user.role == Roles.SUPPORT


class CustomUserFilter(Filter):
    available: Union[Roles, list]

    def __init__(self, available: Union[Roles, list]):
        self.available = available

    async def check(self, message: types.Message) -> bool:
        user = UserService.create_user_without_phone_by_message_if_doesnt_exist(message)
        if isinstance(self.available, Roles):
            return user.role == self.available
        else:
            return user.role in self.available


class NotIncognitaUserFilter(Filter):
    async def check(self, message: types.Message) -> bool:
        user = UserService.create_user_without_phone_by_message_if_doesnt_exist(message)
        return user is not None and user.role != Roles.INCOGNITA
