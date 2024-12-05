#zad 1
x = 42
y = 12
z = x%y
print(z) #reszta z dzielenia to 6

#zad 2
x = 43
y = 12
z = x // y
print(z) #wynik dzielenia calkowitego to 3

#zad 3
a = str(input("Podaj nazwę ksiazki: "))
b = int(input("Podaj rok wydania ksiazki: "))
c = float(input("Podaj cene ksiazki: "))
print(f"Nazwa ksiazki to: {a}, jej rok wydania to: {b}, a jej cena to {c} zł")

#zad 4
a = float(input("Podaj liczbę ujemna: "))
b = float(input("Podaj liczbę dodatnia: "))
c = a ** 2
d = b ** 2
print(f"Liczba ujemna podniesiona do kwadratu to: {c}")
print(f"Liczba dodatnia podniesiona do kwadratu to: {d}")

#zad 5
r = float(input("Podaj promien r: "))
h = float(input("Podaj wysokosc h: "))
pi = 3.14
v = (1/3) * h * pi * (r ** 2)
pp = pi * (r ** 2)
print(f"Objetosc wynosi: {v}, pole podstawy wynosi: {pp}")

#zad 6
a = int(input("Podaj liczbe calkowita: "))
if a % 2 == 0:
    print("Liczba jest parzysta")
else:
    print("Liczba nie jest parzysta")

#zad 7
a1 = int(input("Podaj pierwszy wyraz ciagu: "))
r = int(input("Podaj roznice ciagu: "))
auzytkownika = int(input("Podaj ktory wyraz ciagu chcesz obliczyc: "))

an = a1 + ((auzytkownika - 1) * r)
print(f"{auzytkownika} wyraz ciagu arytmetycznego wynosi: {an}")
"""
Podaj pierwszy wyraz ciagu: 2
Podaj roznice ciagu: 2
Podaj ktory wyraz ciagu chcesz obliczyc: 2
2 wyraz ciagu wynosi: 4
"""
#zad 8
a1 = int(input("Podaj pierwszy wyraz ciagu: "))
q = int(input("Podaj iloraz ciagu: "))
auzytkownika = int(input("Podaj ktory wyraz ciagu chcesz obliczyc: "))
an = a1 * q**(auzytkownika-1)
print(f"{auzytkownika} wyraz ciagu geometrycznego wynosi: {an}")