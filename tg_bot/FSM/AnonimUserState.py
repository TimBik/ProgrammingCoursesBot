from aiogram.dispatcher.filters.state import StatesGroup, State


class AnonimUserState(StatesGroup):
    get_number = State()