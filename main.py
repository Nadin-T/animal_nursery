from controllers.pet_registry import PetRegistry
from views.pet_view import PetView


def main():
    registry = PetRegistry()
    database_path = 'pets.db'
    registry.load_from_database(database_path)
    with registry.counter as counter:
        print(counter.get_count())

    while True:
        PetView.show_menu()
        choice = input("Выберите действие (введите число): ")

        if choice == '1': #Завести новое животное
            animal_type, name, birth_date, commands = PetView.get_pet_info()
            pet = registry.add_pet(animal_type, name, birth_date, commands)
            if pet:
                print(f'Питомец "{name}" успешно заведен.')
                print(counter.get_count())
        elif choice == '2': #Показать всех животных
            registry.list_pets()
        elif choice == '3': #Показать команды животного
            query = PetView.get_find_query()
            registry.find_pet(query)
        elif choice == '4': #Добавить команду
            registry.add_command_to_pet()
        elif choice == '5': #Удалить животное из реестра
            name = PetView.get_pet_name_rem()
            registry.remove_pet(name)
            print(counter.get_count())
        elif choice == '6':  # Загрузить данные из файла
            filename = input("Введите имя файла для загрузки: ")
            registry.load_from_file(filename)
        elif choice == '7':  # Сохранить данные в файл
            filename = input("Введите имя файла для сохранения: ")
            registry.save_to_file(filename)
        elif choice == '0': #Выход из программы
            # registry.save_to_file('pets.json')
            print("Выход из программы.")
            registry.close()  # Закрываем соединение с БД
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте ещё раз: ")
        print('\n')

if __name__ == "__main__":
    main()