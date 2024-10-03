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

