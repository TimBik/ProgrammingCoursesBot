import logging

from aiogram import executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config
from aiogram import Bot, Dispatcher

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )

storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)
