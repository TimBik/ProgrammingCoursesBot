import pymongo

from tg_bot.config import DATABASE, DB_URL

if 'username' in DATABASE:
    auth = {'username': DATABASE['username'],
            'password': DATABASE['password'],
            'authSource': DATABASE['name'],
            'authMechanism': 'SCRAM-SHA-1'}
    client = pymongo.MongoClient(DB_URL, port=int(DATABASE['port']), **auth)
else:
    client = pymongo.MongoClient(DB_URL, port=int(DATABASE['port']))

botDb = client[DATABASE['name']]

def get_mongo_db():
    return botDb
