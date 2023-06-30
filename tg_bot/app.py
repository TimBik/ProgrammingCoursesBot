import sys, os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + "/..")
from loader import bot, storage
from dotenv import load_dotenv


async def on_startup(dp):
    # import filters
    # filters.setup(dp)
    # from utils.notify_admins import on_startup_notify
    # await asyncio.sleep(10)
    # await create_db()
    # await on_startup_notify(dp)
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    pass


async def on_shutdown(dp):
    await storage.close()
    await bot.close()


if __name__ == '__main__':
    from aiogram import executor, types
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
