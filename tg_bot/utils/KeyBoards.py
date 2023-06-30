from aiogram import types

from tg_bot.utils.Roles import Roles


def get_home_authorized_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Выбрать задачу"))
    return keyboard


def get_start_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Отправить телефон", request_contact=True))
    return keyboard


def get_close_chat_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Назад"))
    return keyboard


def get_back_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Назад"))
    return keyboard


home_keyboards = {
    Roles.AUTHORIZED: get_home_authorized_keyboard,
    # Roles.ADMIN: get_home_authorized_keyboard
}


def get_home_user_keyboard(role):
    return home_keyboards[role]()


def get_available_contests(contests):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for contest in contests:
        keyboard.add(types.KeyboardButton(text=contest.name))
    keyboard.add(types.KeyboardButton(text='Назад'))
    return keyboard


def get_tasks(tasks):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for task in tasks:
        keyboard.add(types.KeyboardButton(text=task.name))
    keyboard.add(types.KeyboardButton(text='Назад'))
    return keyboard
