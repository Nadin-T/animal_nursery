import re


class PetView:
    """Класс для управления интерфейсом с пользователем"""

    @staticmethod
    def show_menu():
        print("Меню:")
        print("1. Завести нового питомца")
        print("2. Показать всех питомцев")
        print("3. Показать команды питомца")
        print("4. Добавить команду")
        print("5. Удалить данные питомца из реестра")
        print("0. Выход")

    @staticmethod
    def get_pet_info():
        while True:
            print("Выберите тип питомца:")
            print("1. Собака")
            print("2. Кошка")
            print("3. Хомяк")
            print("4. Лошадь")
            print("5. Верблюд")
            print("6. Осёл")
            print("0. Вернуться в главное меню")
            animal_type = input("Введите тип питомца (1-6): ")
            if animal_type == '0':
                return None, None, None, None
            if animal_type not in {'1', '2', '3', '4', '5', '6'}:
                print("Некорректный ввод. Пожалуйста, выберите число от 1 до 6 "
                      "или 0 для выхода.")
                continue

            while True:
                name = input("Введите имя питомца: ")
                if name.isalpha():
                    break
                else:
                    print("Некорректный ввод. Имя должно содежрать только буквы."
                          "Попробуйте снова.")
            while True:
                birth_date = input("Введите дату рождения в формате ДД-ММ-ГГГГ: ")
                if re.match(r'\d{2}-\d{2}-\d{4}', birth_date):
                    break
                else:
                    print("Некорректный формат даты. Попробуйте снова.")

            commands = input("Введите команды, которые знает питомец, через запятую: ")
            command_list = [cmd.strip() for cmd in commands.split(',')]
            return animal_type, name, birth_date, command_list

    @staticmethod
    def get_find_query():
        return input("Введите кличку питомца для поиска: ")

    @staticmethod
    def get_pet_name_add_com():
        return input("Введите имя питомца, которому хотите добавить команду "
                             "(или '0' для выхода в меню): ")

    @staticmethod
    def get_pet_name_rem():
        return input("Введите имя питомца для удаления данных из реестра: ")