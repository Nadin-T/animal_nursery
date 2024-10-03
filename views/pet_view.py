class PetView:
    """Класс для управления интерфейсом с пользователем"""

    @staticmethod
    def show_menu():
        print("Меню:")
        print("1. Завести новое животное")
        print("2. Показать всех животных")
        print("3. Показать команды животного")
        print("4. Добавить команду")
        print("0. Выход")

    @staticmethod
    def get_pet_info():
        print("Выберите тип животного:")
        print("1. Собака")
        print("2. Кошка")
        print("3. Хомяк")
        print("4. Лошадь")
        print("5. Верблюд")
        print("6. Осёл")
        animal_type = input("Введите тип животного (1-6): ")
        name = input("Введите имя животного: ")
        birth_date = input("Введите дату рождения в формате ГГГГ-ММ-ДД: ")
        commands = input("Введите команды, которые знает животное, через запятую: ")
        command_list = [cmd.strip() for cmd in commands.split(',')]
        return animal_type, name, birth_date, command_list

    @staticmethod
    def get_find_query():
        return input("Введите кличку животного для поиска: ")

    @staticmethod
    def get_pet_name():
        return input("Введите имя животного, которому хотите добавить команду: ")

