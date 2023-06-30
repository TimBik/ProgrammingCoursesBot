from aiogram.dispatcher import FSMContext
from aiogram.types import ChatType, ReplyKeyboardRemove

from tg_bot.FSM.ClientUserState import ClientUserState
from tg_bot.loader import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram import types
from tg_bot import config
from tg_bot.models.Contest import Contest
from tg_bot.models.Task import Task

from tg_bot.services.ContestService import ContestService
from tg_bot.services.TaskService import TaskService
from tg_bot.services.UserService import UserService, ClientService, SupportService
from tg_bot.utils import Logging, KeyBoards
from tg_bot.filters.AccessRightsFilters import CustomUserFilter, AnyUserFilter
from tg_bot.utils.Roles import Roles

logger = Logging.get_logging(__name__)


@dp.message_handler(CustomUserFilter([Roles.AUTHORIZED]), Text("Выбрать задачу"), state=ClientUserState.start,
                    chat_type=ChatType.PRIVATE)
async def home(message: types.Message, state: FSMContext):
    try:
        user = UserService.get_user_by_user_tg_id(message.from_user.id)
        keyboard = KeyBoards.get_available_contests(user.available_contests)
        await ClientUserState.choiceContest.set()
        await bot.send_message(message.chat.id,
                               'Доступные контесты',
                               reply_markup=keyboard)
    except Exception as e:
        logger.exception(e)
        pass


@dp.message_handler(CustomUserFilter([Roles.AUTHORIZED]), state=ClientUserState.choiceContest,
                    chat_type=ChatType.PRIVATE)
async def choice_contest(message: types.Message, state: FSMContext):
    try:
        user = UserService.get_user_by_user_tg_id(message.from_user.id)
        contest = ContestService.find_available_contest(user, message.text)
        if contest:
            keyboard = KeyBoards.get_tasks(contest.tasks)
            await state.update_data(work_contest=contest)
            await ClientUserState.choiceTask.set()
            await bot.send_message(message.chat.id,
                                   'Доступные задачи',
                                   reply_markup=keyboard)
        else:
            await bot.send_message(message.chat.id,
                                   'Такого контеста нет')
    except Exception as e:
        logger.exception(e)
        pass


@dp.message_handler(CustomUserFilter([Roles.AUTHORIZED]), state=ClientUserState.choiceTask,
                    chat_type=ChatType.PRIVATE)
async def choice_task(message: types.Message, state: FSMContext):
    try:
        contest = (Contest)(await state.get_data('work_contest'))
        if contest:
            task = TaskService.find_task_in_contest(contest, message.text)
            if task:
                # TODO: поменять название и реализовать кнопки
                keyboard = KeyBoards.get_do()
                await ClientUserState.choceDo.set()
                await bot.send_message(message.chat.id,
                                       'Выберете действие',
                                       reply_markup=keyboard)
            else:
                await bot.send_message(message.chat.id,
                                       'Такой задачи нет')
        else:
            await bot.send_message(message.chat.id,
                                   'Выбранного контеста больше не существует')
    except Exception as e:
        logger.exception(e)
        pass


@dp.message_handler(CustomUserFilter([Roles.AUTHORIZED]), Text='Отправить задачу', state=ClientUserState.choceDo,
                    chat_type=ChatType.PRIVATE)
async def choce_do(message: types.Message, state: FSMContext):
    try:
        task = (Task)(await state.get_data('work_task'))
        if task:
            keyboard = KeyBoards.get_back_keyboard()
            await ClientUserState.send_solve.set()
            await bot.send_message(message.chat.id,
                                   'Отправьте сюда ваше решение',
                                   reply_markup=keyboard)
        else:
            await bot.send_message(message.chat.id,
                                   'Выбранной задачи больше не существует')
    except Exception as e:
        logger.exception(e)
        pass


@dp.message_handler(Roles.AUTHORIZED, content_types=types.ContentType.DOCUMENT,
                    state=ClientUserState.send_solve,
                    chat_type=ChatType.PRIVATE)
async def choce_do(message: types.Message, state: FSMContext):
    try:
        task = (Task)(await state.get_data('work_task'))
        if task:
            keyboard = KeyBoards.get_back_keyboard()
            # TaskService.check_solve(task, message.document)
            await bot.send_message(message.chat.id,
                                   'Отправьте сюда ваше решение',
                                   reply_markup=keyboard)
        else:
            await bot.send_message(message.chat.id,
                                   'Выбранной задачи больше не существует')
    except Exception as e:
        logger.exception(e)
        pass
