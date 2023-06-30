import os
import subprocess
from aiogram.types import Document

from tg_bot import config


def check_all_dirs(tg_user_id, contest_name):
    paths = ['solver', tg_user_id, contest_name]
    check_path = f'{config.dir_path}'
    for dir in paths:
        check_path += f'/{dir}'
        if not os.path.exists(check_path):
            os.makedirs(check_path)


class TaskService():
    @staticmethod
    def find_task_in_contest(contest, task_name):
        for task in contest.tasks:
            if task.name == task_name:
                return task
        return None

    @staticmethod
    async def check_solve(user, task, document: Document):
        extension = document.file_name.split('.')[-1]
        solver_file_path = f'{config.dir_path}/{task.contest.name}/{task.name}.{extension}'
        solver = await document.download(
            destination_file=solver_file_path)
        if extension in config.AVAILABLE_EXTENSION_SOLVER and solver:
            check_all_dirs(user.tg_user_id, task.contest.name)
            base_path = f'{config.dir_path}/solver/{user.tg_user_id}/{task.contest.name}'
            input_file = open(f'{base_path}/{task.name}_in.txt')
            out_file = open(f'{base_path}/{task.name}_out.txt')
            completed_process = subprocess.run(f'{config.AVAILABLE_EXTENSION_SOLVER[extension]} {solver_file_path}',
                                               shell=True,
                                               timeout=task.timelimit if task.timelimit else 10000,
                                               capture_output=True,
                                               check=True,
                                               stdin=input_file,
                                               stdout=out_file,
                                               encoding='utf-8')
            if completed_process.returncode == 0:
                return completed_process.stdout
            else:
                return 'Что-то пошло не так'

        # text=True)
