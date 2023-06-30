class Task:
    def __init__(self, task):
        self.id = task.get('_id')
        self.name = task.get('name')
        self.text = task.get('text')
        self.link = task.get('link')
        self.contest = task.get('contest')
        self.timelimit = task.get('timelimit')

    def get_dict_nid(self):
        return {
            'name': self.name,
            'text': self.text,
            'link': self.link,
            'contest': self.contest,
            'timelimit': self.timelimit,
        }

    def get_dict(self):
        dict_nid = self.get_dict_nid()
        dict_nid['_id'] = self.id
        return dict_nid

    def to_string(self):
        return ''.join('{}{}'.format(key, val) for key, val in self.get_dict_nid().items())
