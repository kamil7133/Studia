import time
import functools
from datetime import datetime


# 1. Napisz dwie funkcje: `calc_total` i `calc_avg`.
# Wersja pierwsza: obie funkcje są na tym samym poziomie.
def calc_total(*args):
    return sum(args)


def calc_avg(*args):
    if not args:
        return 0
    return sum(args) / len(args)


# Wersja druga: `calc_total` jest funkcją zagnieżdżoną wewnątrz `calc_avg`.
def calc_avg_nested(*args):
    def calc_total(numbers):
        return sum(numbers)

    if not args:
        return 0
    return calc_total(args) / len(args)


# 2. Wyjaśnij, kiedy warto używać zagnieżdżonych funkcji zamiast płaskich (niezależnych).
# Odpowiedź: Funkcji zagnieżdżonych warto używać, gdy funkcja pomocnicza jest używana
# tylko wewnątrz jednej konkretnej funkcji (enkapsulacja), gdy chcemy ukryć logikę przed
# globalnym zakresem lub gdy potrzebujemy dostępu do zmiennych funkcji zewnętrznej (domknięcia).

# 3. Napisz funkcję, która przyjmuje funkcję i argument, a następnie wielokrotnie ją
# wywołuje z tym argumentem.
def run_multiple_times(func, arg, times=3):
    for _ in range(times):
        func(arg)


# 4. Napisz dekorator double_args, który mnoży oba argumenty funkcji przez 2.
def double_args(func):
    def wrapper(a, b):
        return func(a * 2, b * 2)

    return wrapper


# 5. Stwórz dekorator `square_args`, który podnosi oba argumenty funkcji do kwadratu
# przed jej wykonaniem. Zastosuj go do funkcji `sum_args(a, b)`.
def square_args(func):
    def wrapper(a, b):
        return func(a ** 2, b ** 2)

    return wrapper


@square_args
def sum_args(a, b):
    return a + b


# 6. Zastosuj dekorator który wypisuje nazwę funkcji i jej argumenty przy każdym wywołaniu.
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"funkcja {func.__name__} została wywołana z argumentami {args} {kwargs}")
        return func(*args, **kwargs)

    return wrapper


# 7. Zbuduj dekorator, który odlicza czas działania funkcji. Użyj modułu time.
def time_execution(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Czas wykonania: {end - start} sek.")
        return result

    return wrapper


# 8. Zastosuj dekorator do funkcji zwracającej iloczyn dwóch liczb.
# Przykładowo, możesz przemnożyć argumenty przez 3 przed wykonaniem mnożenia.
def triple_args(func):
    def wrapper(a, b):
        return func(a * 3, b * 3)

    return wrapper


@triple_args
def multiply(a, b):
    return a * b


# 9. Napisz dekorator `repeat_on_list`, który działa jak pętla dla elementów listy i stosuje
# daną funkcję do każdego z nich.
def repeat_on_list(func):
    def wrapper(lista_elementow):
        for element in lista_elementow:
            func(element)

    return wrapper


# 10. Użyj `repeat_on_list` do wypisywania elementów listy, czyli dekorator ma stosować
# funkcję print do każdego elementu listy.
@repeat_on_list
def print_item(item):
    print(item)


# 11. Napisz dekorator z argumentami (fabrykę dekoratorów), np. @repeat(n=3).
def repeat(n=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


# 12. Napisz klasę `Zawodnik`, która reprezentuje sportowca (wzrost, waga).
# Metoda instancyjna `oblicz_bmi`. Metoda klasowa `from_lbs`.
class Zawodnik:
    def __init__(self, wzrost, waga):
        self.wzrost = wzrost  # metry
        self.waga = waga  # kilogramy

    # 13. Napisz metodę instancyjną `oblicz_bmi`.
    def oblicz_bmi(self):
        return self.waga / (self.wzrost ** 2)

    @classmethod
    def from_lbs(cls, wzrost, waga_lbs):
        waga_kg = waga_lbs * 0.453592
        return cls(wzrost, waga_kg)


# 14. Wydrukuj BMI trzech zawodników, dwóch inicjowanych normalnie, jeden metodą klasową.
z1 = Zawodnik(1.80, 80)
z2 = Zawodnik(1.75, 70)
z3 = Zawodnik.from_lbs(1.90, 200)

print(f"BMI Z1: {z1.oblicz_bmi()}")
print(f"BMI Z2: {z2.oblicz_bmi()}")
print(f"BMI Z3: {z3.oblicz_bmi()}")


# 15. Rozszerz klasę `Zawodnik`, tak aby śledziła liczniki wag kg i funty.
# 16. Dodaj dekorator logujący wywołania metod w klasie `Zawodnik`.
# 17. Użyj dekoratora `functools.wraps`.

def log_method(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Metoda {func.__name__} wywołana z argumentami: {args[1:]} {kwargs}")
        return func(*args, **kwargs)

    return wrapper


class ZawodnikRozszerzony:
    licznik_wag_kg = 0
    licznik_wag_funty = 0

    def __init__(self, wzrost, waga):
        self.wzrost = wzrost
        self.waga = waga
        # Domyślnie zakładamy kg przy init, korekta w from_lbs
        ZawodnikRozszerzony.licznik_wag_kg += 1

    @log_method
    def oblicz_bmi(self):
        """Oblicza BMI zawodnika."""
        return self.waga / (self.wzrost ** 2)

    @classmethod
    def from_lbs(cls, wzrost, waga_lbs):
        waga_kg = waga_lbs * 0.453592
        obj = cls(wzrost, waga_kg)
        # Korekta liczników: init dodał kg, więc odejmujemy i dodajemy lbs
        cls.licznik_wag_kg -= 1
        cls.licznik_wag_funty += 1
        return obj


# 18. Wyświetl nazwę funkcji po zastosowaniu dekoratora oraz .__doc__.
z_test = ZawodnikRozszerzony(1.8, 80)
print(f"Nazwa metody: {z_test.oblicz_bmi.__name__}")
print(f"Docstring: {z_test.oblicz_bmi.__doc__}")


# 19. Zbuduj klasę `Samochod` (przebieg km). Metoda `from_miles`. Metoda `pokaz_przebieg`.
class Samochod:
    def __init__(self, przebieg):
        self.przebieg = przebieg  # km

    @classmethod
    def from_miles(cls, przebieg_miles):
        return cls(przebieg_miles * 1.60934)

    def pokaz_przebieg(self):
        return self.przebieg


# 20. Napisz dekorator `validate_positive_numbers`.
def validate_positive_numbers(func):
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        if any(isinstance(x, (int, float)) and x <= 0 for x in all_args):
            print('Wszystkie argumenty muszą być dodatnimi liczbami')
            return None
        return func(*args, **kwargs)

    return wrapper


# 21. Zbuduj dekorator, który zapisuje historię wywołań funkcji do listy (czas, nazwa, args).
historia_wywolan = []


def save_history(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        czas = datetime.now()
        wpis = (czas, func.__name__, args)
        historia_wywolan.append(wpis)
        return func(*args, **kwargs)

    return wrapper


@save_history
def przykladowa_funkcja(x):
    return x * x


przykladowa_funkcja(5)
przykladowa_funkcja(10)

# 22. Wydrukuj historię użycia dekorowanej funkcji.
print("Historia wywołań:", historia_wywolan)


# 23. Napisz klasę `Student` (imie, nazwisko, wiek, oceny). Metoda `z_csv`.
class Student:
    def __init__(self, imie, nazwisko, wiek, oceny):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.oceny = oceny

    @classmethod
    def z_csv(cls, linia_tekstowa):
        dane = linia_tekstowa.split(',')
        imie = dane[0]
        nazwisko = dane[1]
        wiek = int(dane[2])
        oceny = [int(x) for x in dane[3].split(';')]
        return cls(imie, nazwisko, wiek, oceny)


# 24. Zastosuj dekorator, który automatycznie przelicza oceny ze skali procentowej na 2–5.
def scale_grades(func):
    def wrapper(punkty_procentowe):
        # Prosta skala: <50: 2, 50-65: 3, 66-80: 4, >80: 5
        if punkty_procentowe < 50:
            ocena = 2
        elif punkty_procentowe <= 65:
            ocena = 3
        elif punkty_procentowe <= 80:
            ocena = 4
        else:
            ocena = 5
        return func(ocena)

    return wrapper


@scale_grades
def zapisz_ocene(ocena):
    print(f"Zapisano ocenę: {ocena}")


# 25. Utwórz dekorator, który zapisuje wynik działania funkcji do pliku tekstowego.
def save_to_file(func):
    def wrapper(*args, **kwargs):
        wynik = func(*args, **kwargs)
        with open("wyniki.txt", "a") as f:
            f.write(str(wynik) + "\n")
        return wynik

    return wrapper


# 26. Zbuduj dekorator, który rzuca wyjątek, jeśli funkcja wykonuje się dłużej niż 4 sekundy.
def timeout_limit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        if end - start > 4:
            raise TimeoutError("Funkcja wykonywała się dłużej niż 4 sekundy")
        return result

    return wrapper


# 27. Zaprojektuj trzy niezależne dekoratory: log_calls, validate_args, measure_time.
# Następnie zastosuj wszystkie trzy do jednej funkcji.

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Log: Wywołanie {func.__name__} z {args}")
        return func(*args, **kwargs)

    return wrapper


def validate_args_positive(func):
    def wrapper(*args, **kwargs):
        if any(x <= 0 for x in args if isinstance(x, (int, float))):
            raise ValueError("Argumenty muszą być dodatnie")
        return func(*args, **kwargs)

    return wrapper


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f"Czas: {time.time() - start:.5f}s")
        return res

    return wrapper


@log_calls
@validate_args_positive
@measure_time
def complex_calculation(a, b):
    time.sleep(0.1)
    return a + b


# 28. Stwórz klasę Produkt (cena, ilosc). Metoda `oblicz_utarg`.
# Dekorator sprawdzający czy cena i ilosc > 0 przed wywołaniem metody.

def validate_product_data(func):
    def wrapper(self, *args, **kwargs):
        if self.cena <= 0 or self.ilosc <= 0:
            print("Błąd: Cena i ilość muszą być większe od zera.")
            return 0
        return func(self, *args, **kwargs)

    return wrapper


class Produkt:
    def __init__(self, cena, ilosc):
        self.cena = cena
        self.ilosc = ilosc

    @validate_product_data
    def oblicz_utarg(self):
        return self.cena * self.ilosc