import json
import sqlite3

from models.animal import Dog, Cat, Hamster, Horse, Camel, Donkey
from models.pet_counter import PetCounter
from views.pet_view import PetView


class PetRegistry:
    """
    Класс регистрации питомцев
    """

    def __init__(self, db_name='pets.db'):
        self.pets = []
        self.counter = PetCounter()
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS pets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT NOT NULL,
                    name TEXT NOT NULL,
                    birth_date TEXT,
                    commands TEXT
                )
            """)

    def add_pet(self, animal_type, name, birth_date, commands):
        #Создание и добавление экземпляра класса питомца в зависимости от типа
        pet = None
        if animal_type == '1':
            pet = Dog(name, birth_date, commands)
        elif animal_type == '2':
            pet = Cat(name, birth_date, commands)
        elif animal_type == '3':
            pet = Hamster(name, birth_date, commands)
        elif animal_type == '4':
            pet = Horse(name, birth_date, commands)
        elif animal_type == '5':
            pet = Camel(name, birth_date, commands)
        elif animal_type == '6':
            pet = Donkey(name, birth_date, commands)
        else:
            print("Некорректный тип животного.")
            return

        if pet:
            self.pets.append(pet)
            self.counter.add()
            self.save_to_database(pet)  # Сохраняем питомца в БД
            return pet

    def save_to_database(self, db_path):
        with self.conn:
            try:
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS pets (id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, name TEXT, birth_date TEXT, commands TEXT)")
                cursor.execute("DELETE FROM pets")  # Очищаем таблицу перед сохранением
                for pet in self.pets:
                    commands = ', '.join(pet.get_commands())
                    cursor.execute("INSERT INTO pets (type, name, birth_date, commands) VALUES (?, ?, ?, ?)",
                                   (pet.__class__.__name__, pet.name, pet.birth_date, commands))
                conn.commit()
                conn.close()
                print("Данные успешно сохранены в базе данных.")
            except Exception as e:
                print(f"Ошибка при сохранении данных в базу: {e}")

    def load_from_database(self, db_path):
        with self.conn:
            try:
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM pets")
                rows = cursor.fetchall()
                for row in rows:
                    pet_type, name, birth_date, commands = row[1], row[2], row[3], row[4].split(',') if row[4] else []
                    pet = eval(pet_type)(name, birth_date, commands)
                self.pets.append(pet)
                self.counter.add()
            except Exception as e:
                print(f"Ошибка при загрузке данных из базы: {e}")

    def close(self):
        self.conn.close()  # Закрываем соединение с БД

    def find_pet(self, query):
        #Поиск питомца по имени
        found_pets = [pet for pet in self.pets if pet.name == query]
        if found_pets:
            for pet in found_pets:
                print(pet)
        else:
            print("Животное не найдено.")

    def list_pets(self):
        #Вывод списка всех питомцев
        if not self.pets:
            print("Список животных пуст.")
        else:
            for pet in self.pets:
                print(pet)

    def add_command_to_pet(self):
        #Добавление команды выбранному питомцу
        while True:
            pet_name = PetView.get_pet_name_add_com()
            if pet_name == '0':
                return  # Выход в меню

            for pet in self.pets:
                if pet.name == pet_name:
                    command = input(f"Введите команду для питомца '{pet_name}': ")
                    pet.add_command(command)
                    print(f"Команда '{command}' добавлена питомцу '{pet_name}'.")
                    return

            print(f"Данные о питомце с именем '{pet_name}' не найдены. "
                  f"Пожалуйста, попробуйте снова.")

    def remove_pet(self, name):
        #Удаление данных о питомце
        pet_to_remove = next((pet for pet in self.pets if pet.name == name), None)
        if pet_to_remove:
            self.pets.remove(pet_to_remove)
            self.counter.remove()
            print(f'Животное "{name}" успешно удалено.')
        else:
            print(f'Животное с именем "{name}" не найдено.')

    def save_to_file(self, filename):
        #Сохранение списка питомцев в файл
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump([{
                    'type': pet.__class__.__name__,
                    'name': pet.name,
                    'birth_date': pet.birth_date,
                    'commands': pet.get_commands()
                } for pet in self.pets], file)
            print("Данные успешно сохранены.")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")

    def load_from_file(self, filename):
        #Загрузка данных о питомцах из файла
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                pets_data = json.load(file)
                for pet_data in pets_data:
                    name = pet_data.get('name', None)
                    birth_date = pet_data.get('birth_date', None)
                    commands = pet_data.get('commands', [])
                    # Проверка на тип животного
                    animal_type = pet_data.get('type', 'Unknown')
                    if name is None or birth_date is None:
                        print(f"Недостаточно данных для питомца. Пропускаю: {pet_data}")
                        continue
                    pet = eval(animal_type)(name, birth_date, commands)
                    self.pets.append(pet)
                    self.counter.add()  # Увеличиваем счётчик при загрузке данных
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Начинаем с пустого реестра.")
        except json.JSONDecodeError:
            print("Ошибка: неверный формат данных в файле.")
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")