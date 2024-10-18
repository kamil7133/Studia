import time
import math


class Zadanie:
    def silnia(self, n):
        wynik = 1
        for i in range(1, n + 1):
            wynik = wynik * i
        return wynik

    def exp(self, x, epsilon):
        suma = 0
        i = 0
        while True:
            silnia_wynik = self.silnia(i)
            potega = x ** i
            wyraz = potega / silnia_wynik
            suma += wyraz

            if abs(wyraz) < epsilon:
                break

            i += 1

        return suma

    def exp_efektywna(self, x, epsilon):
        suma = 1
        wyraz = 1
        i = 1

        while abs(wyraz) >= epsilon:
            wyraz = wyraz * (x / 1)
            suma += wyraz
            i += 1

        return suma



zadanie = Zadanie()
x = -5.5
epsilon = 1e-10

#pomiar czasu dla exp nieefeektywnej
startowy_czas = time.time()
for _ in range(1000):
    wynik_nieefektywny = zadanie.exp(x, epsilon)
koncowy_czas = time.time()
czas_nieefektywny = koncowy_czas - startowy_czas

#pomiar czasu dla exp efektywnej
startowy_czas = time.time()
for _ in range(1000):
    wynik_efektywny = zadanie.exp(x, epsilon)
koncowy_czas = time.time()
czas_efektywny = koncowy_czas - startowy_czas

#pomiar czasu dla wbudowanej funkcji z bibl math
startowy_czas = time.time()
for _ in range(1000):
    wynik_exp = math.exp(x)
koncowy_czas = time.time()
czas_exp = koncowy_czas - startowy_czas

print(f"Wynik metody nieefektywnej: {wynik_nieefektywny}")
print(f"Wynik metody efektywnej: {wynik_efektywny}")
print(f"Wynik funkcji wbudowanej: {wynik_exp}")
print("                  ")
print(f"Czas metody nieefektywnej: {czas_nieefektywny:.5f} sekund")
print(f"Czas metod efektywnej: {czas_efektywny:.5f} sekund")
print(f"Czas funkcji wbudowanej exp: {czas_exp:.5f} sekund")