from animal import Animal
from datasource import DataSource
from person import Person


class App:
    __options = [
        '0 - Add a new person;',
        '1 - Read all persons;',
        '2 - Add a new animal;',
        '3 - Read all animals;',
        '4 - Quit.'
    ]

    def __init__(self):
        self.__on = True
        self.__actions = [
            self.__add_person,
            self.__get_all_persons,
            self.__add_animal,
            self.__get_all_animals,
            self.__quit
        ]
        self.__datasource = DataSource()

    def main(self):
        print('Welcome, master!')
        while self.__on:
            print('\nOptions:\n' + '\n'.join(self.__options))
            option = int(input('\nEnter your option: '))
            if 0 <= option < len(self.__options):
                try:
                    self.__actions[option]()
                except (ValueError, TypeError):
                    print('\nOops, some error occurred; try again!')

    def __add_person(self):
        print('\nInput person\'s data:')
        self.__datasource.add_person(Person(
            name=input('name: '),
            last_name=input('last_name: '),
            address=input('address: '),
            passport=input('passport: '),
            age=input('age: '),
            phone=input('phone: ')
        ))

    def __get_all_persons(self):
        print('\n' + '\n'.join(map(lambda p: str(p), self.__datasource.get_all_persons())))

    def __add_animal(self):
        print('\nInput animal\'s data:')
        self.__datasource.add_animal(Animal(
            kind=input('kind: '),
            token=input('token: '),
            sound=input('sound: '),
            owner_phone=input('owner_phone: ')
        ))

    def __get_all_animals(self):
        print('\n' + '\n'.join(map(lambda p: str(p), self.__datasource.get_all_animals())))

    def __quit(self):
        self.__on = False
        print('\nGoodbye, master!')


if __name__ == '__main__':
    App().main()
