from aiogram.dispatcher import FSMContext
from aiogram.types import ChatType

from tg_bot.FSM.AnonimUserState import AnonimUserState
from tg_bot.FSM.ClientUserState import AuthorizedUserState
from tg_bot.loader import dp, bot
from aiogram.dispatcher.filters import CommandStart
from aiogram import types
from tg_bot.models.User import User
from tg_bot import config
from tg_bot.repository.UserRepository import UserRepository
from tg_bot.services.UserService import UserService
from tg_bot.utils import Logging, KeyBoards, PhoneNumberFormat
from tg_bot.utils.Roles import Roles
from tg_bot.filters.AccessRightsFilters import AnyUserFilter

logger = Logging.get_logging(__name__)


@dp.message_handler(CommandStart(), AnyUserFilter(), state='*', chat_type=ChatType.PRIVATE)
async def cmd_start(message: types.Message, state: FSMContext):
    try:
        user = User(UserRepository.get_user_by_user_tg_id(message.from_user.id))
        if user.role == Roles.INCOGNITA:
            keyboard = KeyBoards.get_start_keyboard()
            await AnonimUserState.get_number.set()
            await bot.send_message(message.chat.id,
                                   'Чтобы продолжить, пожалуйста, предоставьте свои данные.',
                                   reply_markup=keyboard)
        else:
            keyboard = KeyBoards.get_home_user_keyboard(user.role)
            await state.reset_state(with_data=True)
            await AuthorizedUserState.start.set()
            await bot.send_message(message.chat.id,
                                   'Вы уже авторизованы!',
                                   reply_markup=keyboard)
    except Exception as e:
        logger.exception(e)
        pass


@dp.message_handler(AnyUserFilter(), content_types=['contact'], state=AnonimUserState.get_number,
                    chat_type=ChatType.PRIVATE)
async def contact(message: types.Message, state: FSMContext):
    try:
        if message.contact is not None:
            user = User(UserRepository.get_user_by_user_tg_id(message.from_user.id))
            if user.username is not None and user.username in config.ADMINS:
                user.role = Roles.ADMIN
            elif user.role == Roles.INCOGNITA:
                user.role = Roles.AUTHORIZED
            keyboard = KeyBoards.get_home_user_keyboard(user.role)
            user.number = PhoneNumberFormat.number_format(message.contact.phone_number)
            UserService.update_user_by_tg_user_id(user.tg_user_id, user)
            await bot.send_message(message.chat.id,
                                   'Спасибо! Теперь мы можем продолжить',
                                   reply_markup=keyboard)
        await state.reset_state(with_data=False)
        await AuthorizedUserState.start.set()
    except Exception as e:
        logger.exception(e)
        pass
