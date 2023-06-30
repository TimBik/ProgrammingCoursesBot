import os

import yaml
from aiogram import Bot

dir_path = os.getcwd()

try:
    with open(dir_path + '/settings.yml', encoding='utf-8') as it:
        yml = yaml.load(it, Loader=yaml.FullLoader)
except Exception as e:
    raise (e)

TELEGRAM = yml['telegram']

bot = Bot(TELEGRAM['token'])
BOT_CHAT_ID = bot.id

BOT_TOKEN = TELEGRAM['token']
ASKONA_HELP_CHAT_ID = TELEGRAM['askona_help_chat_id']

# BD_HOST = '10.1.1.10'
# BD_HOST = 'localhost'
# BD_PORT = 27017
# BD_NAME = 'BlogersDB'
# BOT_ID = 5736836132
ADMINS = []

DATABASE = yml['db']

DB_URL = 'mongodb://' + DATABASE['host'] + ''
CLIENT_PATTERNS = yml['client_patterns']
SUPPORT_PATTERNS = yml['support_patterns']
PREDICT_ANSWER = yml['predict_answer']

AVAILABLE_EXTENSION_SOLVER = {'py': f'{dir_path}/bash_scripts/python3_executor.sh'}
