from controllers.pet_registry import PetRegistry
from views.pet_view import PetView


def main():
    registry = PetRegistry()

    while True:
        PetView.show_menu()
        choice = input("Выберите действие (введите число): ")

        if choice == '1': #Завести новое животное
            animal_type, name, birth_date, commands = PetView.get_pet_info()
            with registry.counter as counter:
                pet = registry.add_pet(animal_type, name, birth_date, commands)
                if pet:
                    counter.add()
                    print(f'Животное "{name}" успешно заведено.')
        elif choice == '2': #Показать всех животных
            registry.list_pets()
        elif choice == '3': #Показать команды животного
            query = PetView.get_find_query()
            registry.find_pet(query)
        elif choice == '4': #Добавить команду
            pet_name = PetView.get_pet_name()
            command = input("Введите команду, которую хотите добавить: ")
            registry.add_command_to_pet(pet_name, command)
        elif choice == '0': #Выход из программы
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте ещё раз: ")
        print('\n')

if __name__ == "__main__":
    main()