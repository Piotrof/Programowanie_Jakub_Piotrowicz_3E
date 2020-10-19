import os
import msvcrt as m

def menu():
    print("Wybierz co chcesz zrobić:")
    print("1.Tworzenie listy")
    print("2.Wyświetlanie elementów listy")
    print("3.Sortowanie listy")
    print("4.Wyświetl informacje o liście")
    print("5.Usuwanie elementów listy")
    print("6.Zakończ program")


def cont():
    input("Naciśnij klawisz aby kontynuować.")


def refresh():
    os.system('cls' if os.name == 'nt' else 'clear')


def create_table(list):
    print("Ile elementów ma zawierać lista?")
    n_of_elements = int(input())

    for i in range (n_of_elements):
        list.append(int(input(f"Wprowadź {i+1} element:")))


def show_elements(list):
    print(f"Elementy znajdujące się w liście to: {list}")


def sort_list(list):
    choice = input("Czy chcesz tylko zobaczyć posortowaną listę, czy trwale ją posortować? [ZOBACZ/POSORTUJ]")
    if choice.upper() == "ZOBACZ":
        list_sorted = list[:]
        list_sorted.sort()
        print(f"Posortowana lista wygląda tak: {list_sorted}")
    elif choice.upper() == "POSORTUJ":
        list.sort()
        print("Posortowano listę")

def delete_element(list):
    choice = input("Który element chcesz usunąć?")
    del list[choice-1]


def list_info(list):
    print(f"Lista zawiera {len(list)} elementów.")
    print(f"Elementy znajdujące się w liście to: {list}")
    print(f"Największy element to: {max(list)}")
    print(f"Najmniejszy element to: {min(list)}")
    print(f"Suma elementów listy to: {sum(list)}")
    print(f"Średnia elementów znajdujących się w liście wynosi: {sum(list)/len(list)}")


list = []

menu()

while(True):
    menu_choice = int(input())

    if menu_choice == 1:
        create_table(list)
        cont()
        refresh()
        menu()
    elif menu_choice == 2:
        show_elements(list)
        cont()
        refresh()
        menu()
    elif menu_choice == 3:
        sort_list(list)
        cont()
        refresh()
        menu()
    elif menu_choice == 4:
        list_info(list)
        cont()
        refresh()
        menu()
    elif menu_choice == 5:
        delete_element(list)
        cont()
        refresh()
        menu()