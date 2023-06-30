from tg_bot.repository.ContestRepository import ContestRepository


class ContestService():
    @staticmethod
    def find_available_contest(user, contest_name):
        come_contest = ContestRepository.get_contest_by_name(contest_name)
        return come_contest if come_contest in user.available_contests else None
