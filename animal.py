from random import randint


class Animal:
    def __init__(self, **kwargs):
        self.kind = kwargs.get('kind')
        self.token = int(kwargs.get('token'))
        self.sound = kwargs.get('sound')
        if kwargs.get('owner_phone').isnumeric():
            self.owner_phone = kwargs.get('owner_phone')
        else:
            raise TypeError('Owner phone should be numeric')

    def __str__(self):
        return f'Animal:\n +kind: {self.kind}\n +token: {self.token}\n' \
            f' +sound: {self.sound}\n +owner_phone: {self.owner_phone}'

    def joy(self):
        for i in range(randint(1, 10)):
            print(self.sound)

    def to_json(self):
        return {
            'kind': self.kind,
            'token': self.token,
            'sound': self.sound,
            'owner_phone': self.owner_phone
        }
