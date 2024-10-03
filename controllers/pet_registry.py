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
            print("Животное с таким именем не найдено.")