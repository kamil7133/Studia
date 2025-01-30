import math
import cmath

#1
print("zadanie 1")
r = int(input("Podaj promien: "))
h = int(input("Podaj wysokosc: "))

V = math.pi * pow(r, 2) * h
S = (2 * math.pi * pow(r, 2)) + 2 * math.pi * r * h
print(f"Objętośc to {V:.2f}, a powierzchnia to {S:.2f}")
#2
print("zadanie 2")
liczba_uz = int(input("Podaj liczbe: "))
i = 2
lista = []
while i != liczba_uz:
    liczba = liczba_uz // i
    if liczba not in lista:
        lista.append(liczba)
    i += 1
liczba_cal = sum(lista)
if liczba_cal > liczba_uz:
    print(f"liczba: {liczba_uz} jest obfita, jej suma dzielnikow wynosi {liczba_cal}")
else:
    print("Liczba nie jest obfita")
#3
print("zadanie 3")
v = float(input("Podaj predkosc wiatru: "))
tu = float(input("Podaj temperature otoczenia: "))

to = 13.12 + (0.6215 * tu) - (11.37 * (pow(v, 0.16)) + ((0.3965 * tu) * (pow(v, 0.16))))
print(f"Temperatura odczuwalna to {to:.1f} stopni Celciusza")
#4
print("zadanie 4")
r = 6371
szerokosc1 = 18.4
szerokosc2 = 24.1
dlugosc1 = 55.3
dlugosc2 = 58.7
szerokosc1 = math.radians(szerokosc1)
szerokosc2 = math.radians(szerokosc2)
dlugosc1 = math.radians(dlugosc1)
dlugosc2 = math.radians(dlugosc2)
roznica_szerokosci = szerokosc2 - szerokosc1
roznica_dlugosci = dlugosc2 - dlugosc1
haversine = 2 * r * math.asin(
    math.sqrt(
        math.sin(roznica_szerokosci / 2) ** 2
        + math.cos(szerokosc1) * math.cos(szerokosc2) * math.sin(roznica_dlugosci / 2) ** 2
    )
)
print(f"odlegosc to: {round(haversine, 2)}")
#5
print("zadanie 5")
def wyswietl_wyniki(x, y):
    dodawanie = z1 + z2
    odejmowanie = z1 - z2
    mnozenie = z1 * z2
    dzielenie = z1 / z2
    print(f"Wynik to: dodawanie = {dodawanie}, odejmowanie = {odejmowanie}, mnożenie = {mnozenie}, dzielenie = {dzielenie}")

z1 = complex(input("Podaj liczbe zespolona np: 3+4j -> "))
z2 = complex(input("Podaj liczbe zespolona np: 5+6j -> "))
wyswietl_wyniki(z1, z2)
#6
print("zadanie 6")
zl = [1, 2, 3, 4]
suma1 = sum(zl)
zl_srednia = suma1 / len(zl)

for i in zl:
    lista_roznica = []
    roznica = i - zl_srednia
    pow(roznica, 2)
    lista_roznica.append(roznica)

zesumowana = sum(lista_roznica)
wariancja = zesumowana / len(zl)
print(wariancja)
odchylenie_standardowe = math.sqrt(wariancja)
print(f"odchylenie standardowe: {odchylenie_standardowe}")

