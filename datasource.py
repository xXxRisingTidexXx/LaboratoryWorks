from json import loads, dumps


class DataSource:
    def __init__(self):
        with open('db.json') as stream:
            self.__db = loads(stream.read())

    def add_person(self, person):
        self.__db['persons'].append(person.to_json())

    def get_all_persons(self):
        return self.__db['persons']

    def add_animal(self, animal):
        self.__db['animals'].append(animal.to_json())

    def get_all_animals(self):
        return self.__db['animals']

    def __del__(self):
        with open('db.json', 'w') as stream:
            stream.write(dumps(self.__db))
