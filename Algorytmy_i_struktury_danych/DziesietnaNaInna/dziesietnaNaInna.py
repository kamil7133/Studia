import string
class Zadanie:
    def zamien(self, n, k):
        if k not in range(2,36):
            raise ValueError("Liczba powinna być w zakresie od 2 do 36")
        elif n == 0:
            return ""
        else:
            char = list(string.digits + string.ascii_uppercase)
            r = n % k
            value = self.zamien(n // k, k)
            result = value + char[r]
            return result

zadanie = Zadanie()

n, k = input("Podaj dwie liczby: ").split()

try:
    n = int(n)
    k = int(k)
    wynik = zadanie.zamien(n, k)
    print(f"{wynik}")
except ValueError as g:
    print(g)

