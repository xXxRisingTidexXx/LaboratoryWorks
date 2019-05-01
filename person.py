class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.last_name = kwargs.get('last_name')
        self.address = kwargs.get('address')
        if kwargs.get('passport').isnumeric():
            self.passport = kwargs.get('passport')
        else:
            raise TypeError('Passport should contain only digits')
        self.age = int(kwargs.get('age'))
        if kwargs.get('phone').isnumeric():
            self.phone = kwargs.get('phone')
        else:
            raise TypeError('Phone should contain only digits')

    def __str__(self):
        return f'Person:\n +name: {self.name}\n +last_name: {self.last_name}\n' \
            f' +address: {self.address}\n +passport: {self.passport}\n +age: ' \
            f'{self.age}\n +phone: {self.phone}'

    def to_json(self):
        return {
            'name': self.name,
            'last_name': self.last_name,
            'address': self.address,
            'passport': self.passport,
            'age': self.age,
            'phone': self.phone
        }
