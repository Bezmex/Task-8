from menu_functions import f1, f2, f3
from functions_for_work import is_int

def menu():
    array_palindromes = [] # массив палиндромов
    is_text_input = False
    is_algoritm_done = False

    while 1:
        print("Выберите пункт меню:\n"
              "1. Ввод исходного текста \n"
              "2. Выполнение алгоритма по поиску палиндромов в тексте\n"
              "3. Вывод результата\n"
              "4. Выход из цикла")
        choice = input()
        if is_int(choice):
            choice = int(choice)

        if choice == 1:
            text_input = f1()
            is_text_input = True

        elif choice == 2:
            if is_text_input:
                array_palindromes = f2()
                is_algoritm_done = True
            else:
                print("Ошибка!\nСначала введите текст\n\n")
        elif choice == 3:
            if is_algoritm_done:
                if is_text_input:
                    f3(array_palindromes)
            else:
                print("\nСначала выполните алгоритм\n")
        elif choice == 4:
            break
        else:
            print('error')

if __name__ == "__main__":
    menu()