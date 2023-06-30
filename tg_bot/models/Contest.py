class Contest:
    def __init__(self, contest):
        self.id = contest.get('_id')
        self.name = contest.get('name')
        self.tasks = contest.get('tasks')

    def get_dict_nid(self):
        return {
            'name': self.name,
            'tasks': self.tasks,
        }

    def get_dict(self):
        dict_nid = self.get_dict_nid()
        dict_nid['_id'] = self.id
        return dict_nid

    def to_string(self):
        return ''.join('{}{}'.format(key, val) for key, val in self.get_dict_nid().items())
