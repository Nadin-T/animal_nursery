from controllers.pet_registry import PetRegistry
from views.pet_view import PetView


def main():
    registry = PetRegistry()
    registry.load_from_database()
    with registry.counter as counter:
        print(counter.get_count())

    print("Добро пожаловать в систему учёта питомника.")

    while True:
        print("1. Показать меню")
        print("0. Выход")
        choice = input("Выберите действие (введите число): ")

        if choice == '1':
            PetView.show_menu()
            action_choice = input("Выберите действие (введите число): ")

            if action_choice == '1': #Завести новое животное
                animal_type, name, birth_date, commands = PetView.get_pet_info()
                pet = registry.add_pet(animal_type, name, birth_date, commands)
                if pet:
                    print(f'Питомец "{name}" успешно заведен.')
                    print(counter.get_count())
            elif action_choice == '2': #Показать всех животных
                registry.list_pets()
            elif action_choice == '3': #Показать команды животного
                query = PetView.get_find_query()
                registry.find_pet(query)
            elif action_choice == '4': #Добавить команду
                registry.add_command_to_pet()
            elif action_choice == '5': #Удалить животное из реестра
                name = PetView.get_pet_name_rem()
                registry.remove_pet(name)
                print(counter.get_count())
            elif action_choice == '6':  # Загрузить данные из файла
                filename = input("Введите имя файла для загрузки: ")
                registry.load_from_file(filename)
            elif action_choice == '7':  # Сохранить данные в файл
                filename = input("Введите имя файла для сохранения: ")
                registry.save_to_file(filename)
            elif action_choice == '0': #Выход из программы
                registry.save_to_database()
                return
            else:
                print("Некорректный выбор. Пожалуйста, попробуйте ещё раз: ")
            print('\n')
        elif choice == '0':
            registry.save_to_database()
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте ещё раз.")

if __name__ == "__main__":
    main()