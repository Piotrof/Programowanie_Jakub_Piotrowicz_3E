import pickle

students_list = []


class Student:
    def __init__(self, name, surname, index_nmber, rating_list=[]):
        self.__name = name
        self.__surname = surname
        self.__index_number = index_nmber
        self.__rating_list = rating_list[:]

    def show(self):
        print(f"\nStudent: {self.__name} {self.__surname}")
        print(f"  Index Number: {self.__index_number}")
        print(f"  Rating list: {self.__rating_list}")

    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

    def set_index_nmber(self, index_nmber):
        self.__index_number = index_nmber

    def avg_rating(self):
        return {sum(self.__rating_list) / len(self.__rating_list)}


def defense_int_input(text, min_val, max_val):
    value = max_val
    while True:
        value = input(text)
        try:
            if not ((int(min_val) > int(value)) or (int(value) > int(max_val))):
                break
            print('Wartość musi być niemniejsza niż:', min_val,
                  'i nie większa niż:', max_val, sep=' ', end='\n')
        except ValueError:
            print('Błąd! Wartość musi być liczbą całkowitą.')
    return int(value)


def display_menu():
    menu_selection = 0
    print('\nMenu:')
    print('1 - Wyświetl listę studentów')
    print('2 - Edytuj listę studentów')
    print('3 - Wyswietl wybranych studentów')
    print('4 - Odczytaj listę z pliku')
    print('5 - Zapisz listę z pliku')
    print('6 - Koniec programu')

    print('\n')
    menu_selection = defense_int_input("Wybierz operacje: ", 1, 6)

    return menu_selection


def display_menu2():
    menu_selection = 0
    print('\nEdyyuj listę studentów:')
    print('  1 - Dodaj nowego studenta')
    print('  2 - Usuń wybranego studenta')
    print('  3 - Dodaj nową ocenę')
    print('  4 - Wróć')

    print('\n')
    menu_selection = defense_int_input("Wybierz operacje: ", 1, 4)

    return menu_selection


def display_menu3():
    menu_selection = 0
    print('\nWyswietl dane wybranych studentów:')
    print('  1 - Średnia > x')
    print('  2 - Średnia < x')
    print('  3 - Wróć')

    print('\n')
    menu_selection = defense_int_input("Wybierz operacje: ", 1, 3)

    return menu_selection


def load():
    try:
        with open("bin.dat", "rb") as f:
            students_list = pickle.load(f)
            return students_list
    except FileNotFoundError:
        with open("bin.dat", "wb") as f:
            print('\nbin.dat nie został znaleziony, tworzę nowy plik...\n')

    except Exception as identifier:
        print(f'\nWarning: {identifier} podczas czytania pliku\n')
        return []


def save(students_list):
    with open("bin.dat", "wb") as f:
        pickle.dump(students_list, f)


def showStudents(s_list):
    print('\nLista studentów:\n')
    for student in s_list:
        student.show()
        print()


# with open("bin.dat", "rb") as f:
#     s_l = pickle.load(f)
#     print(f"s_l: {s_l}")
#     try:
#         for s in s_l:
#             s.show()
#     except TypeError as identifier:
#         print(f'\nError:\n  {identifier}\n')


menu_selection = display_menu()

while (menu_selection < 6):
    if menu_selection == 1:
        showStudents(students_list)
    elif menu_selection == 2:
        m = display_menu2()
        while (m < 4):
            if m == 1:
                print('(napisz /stop żeby przerwać)')
                name = input("Imię: ")
                if name == '/stop':
                    pass
                else:
                    surname = input('Nazwisko: ')
                    student = Student(name, surname)
                    students_list.append(student)
            elif m == 2:
                showStudents(students_list)
                print('(napisz /stop żeby przerwać)')
                index = input('Wpisz indeks studenta, którego dane chcesz usunąć: ')
                if index == '/stop':
                    pass
                else:
                    flag = False
                    for i in range(len(students_list)):
                        try:
                            if students_list[i].__index_number == index:
                                flag = True
                                del students_list[i]
                                break
                        except Exception:
                            print('W liście studentów wystąpił błąd.')
                            raise
                    if not flag:
                        input('Nie ma takeigo indeksu.')
                        continue
            elif m == 3:
                showStudents(students_list)
                print('(napisz /stop żeby przerwać)')
                index = input('Wprowadź indeks studenta, którego oceny chcesz dodać: ')
                if index == '/stop':
                    pass
                else:
                    flag = False
                    for i in range(len(students_list)):
                        try:
                            if students_list[i].__index_number == index:
                                n0 = input('Wpisz liczbę ocen, jaką chcesz dodać: ')
                                for j in range(n0):
                                    students_list[i].__rating_list.append(defense_int_input('Ocena: ', 1, 6))
                                flag = True
                                break
                        except Exception:
                            print('W liście studentów wystąpił błąd.')
                            raise
                    if not flag:
                        input('Nie ma takiego indeksu.')
                        continue
            m = display_menu2()
    elif menu_selection == 3:
        m = display_menu3()
        while m < 3:
            x = input('x: ')
            try:
                x = float(x)
            except ValueError:
                print('Błąd! Wartość średniej nie jest liczbą')
                print('(Pamiętaj że liczby zmiennoprzcikowe piszemy z ., a nie z ,)\n')
                continue

            try:
                if m == 1:
                    for student in students_list:
                        if Student(student).avg_rating > x:
                            student.show()
                            print()
                if m == 2:
                    for student in students_list:
                        if Student(student).avg_rating < x:
                            student.show()
                            print()
            except Exception:
                print('W liście studentów wystąpił błąd.')
                raise

            m = display_menu3()

    elif menu_selection == 4:
        students_list = load()

    elif menu_selection == 5:
        save(students_list)
        print('Zapisano do pliku.')

    menu_selection = display_menu()