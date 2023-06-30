from tg_bot.utils import MongoConnect

bd = MongoConnect.get_mongo_db()


class ContestRepository():

    @staticmethod
    def get_contest_by_name(name):
        return bd.contests.find_one({'name': name})


    @staticmethod
    def add_contest(contest):
        return bd.contests.insert_one(contest.get_dict_nid())
