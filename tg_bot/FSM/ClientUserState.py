from aiogram.dispatcher.filters.state import StatesGroup, State


class ClientUserState(StatesGroup):
    send_solve = State()
    choceDo = State()
    choiceContest = State()
    choiceTask = State()
    start = State()
