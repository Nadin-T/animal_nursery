class Animal:

    def __init__(self, name, birth_date, commands=None):
        self.__name = name
        self.__birth_date = birth_date
        self.__commands = commands if commands else []

    @property
    def name(self):
        return self.__name

    @property
    def birth_date(self):
        return self.__birth_date

    def add_command(self, command):
        self.__commands.append(command)

    def get_commands(self):
        return self.__commands

    def __str__(self):
        return f"{self.__name} ({self.__birth_date}) умеет выполнять команды: {', '.join(self.__commands)}"


class DomesticAnimal(Animal):
    pass


class PackAnimal(Animal):
    pass


class Dog(DomesticAnimal):
    pass


class Cat(DomesticAnimal):
    pass


class Hamster(DomesticAnimal):
    pass


class Horse(PackAnimal):
    pass


class Camel(PackAnimal):
    pass


class Donkey(PackAnimal):
    pass