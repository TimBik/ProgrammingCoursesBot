from tg_bot.utils import MongoConnect

bd = MongoConnect.get_mongo_db()


class UserRepository:

    @staticmethod
    def update_user_by_tg_user_id(tg_user_id, user):
        return bd.users.replace_one({'tg_user_id': tg_user_id}, user.get_dict_nid())

    @staticmethod
    def get_user_by_user_tg_id(tg_user_id):
        return bd.users.find_one({'tg_user_id': tg_user_id})

    @staticmethod
    def get_user_by_user_number(phone):
        return bd.users.find_one({'phone': phone})

    @staticmethod
    def add_user(user):
        return bd.users.insert_one(user.get_dict_nid())

