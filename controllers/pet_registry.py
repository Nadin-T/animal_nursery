import json

from models.animal import Dog, Cat, Hamster, Horse, Camel, Donkey
from models.pet_counter import PetCounter


class PetRegistry:

    def __init__(self):
        self.pets = []
        self.counter = PetCounter()

    def add_pet(self, animal_type, name, birth_date, commands):
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
            return pet

    def find_pet(self, query):
        found_pets = [pet for pet in self.pets if pet.name == query]
        if found_pets:
            for pet in found_pets:
                print(pet)
        else:
            print("Животное не найдено.")

    def list_pets(self):
        if not self.pets:
            print("Список животных пуст.")
        else:
            for pet in self.pets:
                print(pet)

    def add_command_to_pet(self, pet_name, command):
        for pet in self.pets:
            if pet.name == pet_name:
                pet.add_command(command)
                print(f"Команда '{command}' добавлена животному '{pet_name}'.")
                return
        print(f"Животное с именем '{pet_name}' не найдено.")

    def remove_pet(self, name):
        pet_to_remove = next((pet for pet in self.pets if pet.name == name), None)
        if pet_to_remove:
            self.pets.remove(pet_to_remove)
            print(f'Животное "{name}" успешно удалено.')
        else:
            print(f'Животное с именем "{name}" не найдено.')

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([{
                'type': pet.__class__.__name__,
                'name': pet.name,
                'birth_date': pet.birth_date,
                'commands': pet.get_commands()
            } for pet in self.pets], file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                pets_data = json.load(file)
                for pet_data in pets_data:
                    pet = eval(pet_data['type'])(pet_data['name'], pet_data['birth_date'], pet_data['commands'])
                    self.pets.append(pet)
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Начинаем с пустого реестра.")
