from views.pet_view import PetView


def main():
    while True:
        PetView.show_menu()
        choice = input("Выберите действие (введите число): ")

        if choice == '1': #Завести новое животное
            pass
        elif choice == '2': #Показать всех животных
            pass
        elif choice == '3': #Показать команды животного
            pass
        elif choice == '4': #Добавить команду
            pass
        elif choice == '0': #Выход из программы
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте ещё раз: ")
        print('\n')