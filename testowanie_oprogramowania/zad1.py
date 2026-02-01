"""
Ten moduł zawiera różne funkcje i klasę do celów demonstracyjnych.
"""

def add_numbers(a, b):
    """
    Dodaj dwie liczby i zwróć wynik.

    Args:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.

    Returns:
        int: Suma a i b.
    """
    return a + b


def check_age(user):
    """
    Sprawdź, czy użytkownik jest dorosły, czy niepełnoletni.

    Args:
        user (str): Imię użytkownika.
    """
    users = {"Alice": 20, "Bob": 17}
    if users.get(user, 0) >= 18:
        print(f"{user} jest dorosły.")
    else:
        print(f"{user} jest niepełnoletni.")


X = 5
Y = 10

if X > Y:
    print("X jest większy od Y")


class MyClass:
    """
    Klasa reprezentująca prostą operację matematyczną.
    """
    def __init__(self, value):
        """
        Inicjalizuj klasę z wartością.

        Args:
            value (int): Wartość do przechowania.
        """
        self.value = value

    def multiply(self, factor: int) -> int:
        """
        Pomnóż przechowywaną wartość przez czynnik.

        Args:
            factor (int): Czynnik do pomnożenia.

        Returns:
            int: Wynik mnożenia.
        """
        return self.value * factor

    def add(self, other: int) -> int:
        """
        Dodaj podaną wartość do przechowywanej wartości.

        Args:
            other (int): Liczba do dodania.

        Returns:
            int: Wynik dodawania.
        """
        return self.value + other


for i in range(10):
    print(i)

my_list = [1, 2, 3]
my_list.append(4)


def bad_indentation():
    """
    Funkcja z poprawionym wcięciem.
    """
    print("Poprawione wcięcie działa poprawnie.")


def sum_arguments(*args):
    """
    Funkcja przyjmująca zmienną liczbę argumentów.

    Args:
        *args (int): Argumenty całkowite.

    Returns:
        int: Suma wszystkich argumentów.
    """
    return sum(args)


def long_line():
    """
    Funkcja z poprawioną długością linii.
    """
    message = (
        "To jest linia kodu, która nic nie wnosi do działania programu, "
        "ale musi zostać."
    )
    print(message)


def unused_variable():
    """
    Funkcja z poprawionym kodem, bez nieużywanej zmiennej.

    Returns:
        int: Przykładowa wartość.
    """
    return 42


def print_message():
    """
    Funkcja, która drukuje wiadomość.
    """
    print("Hello, world!")


if __name__ == "__main__":
    print(add_numbers(2, 3))
    check_age("Alice")
    obj = MyClass(5)
    print(obj.multiply(4))
    print(obj.add(10))
    print(sum_arguments(1, 2, 3, 4, 5))
    long_line()
    print(unused_variable())
    print_message()
