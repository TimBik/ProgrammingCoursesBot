class User:

    def __init__(self, user):
        self.id = user.get('_id')
        self.number = user.get('number')
        self.role = user.get('role')
        self.username = user.get('user_name')
        self.name = user.get('name')
        self.surname = user.get('surname')
        self.tg_user_id = user.get('tg_user_id')
        self.available_contests = user.get('available_contests')

    def get_dict_nid(self):
        return {
            'number': self.number,
            'role': self.role,
            'user_name': self.username,
            'name': self.name,
            'surname': self.surname,
            'tg_user_id': self.tg_user_id,
            'available_contests': self.available_contests
        }

    def get_dict(self):
        dict_nid = self.get_dict_nid()
        dict_nid['_id'] = self.id
        return dict_nid

    def to_string(self):
        return ''.join('{}{}'.format(key, val) for key, val in self.get_dict_nid().items())
