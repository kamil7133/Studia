
#zad 1

name = input("Podaj imię: ")
age = int(input("Podaj wiek: "))
print("Uzytkownik {name} ma {age} lat!".format(name=name, age=age))

#zad 2

#przykładowy komentarz liniowy
"""
Przykładowy komentarz blokowy
"""


#zad 3
a3 = 5
b3 = 4
c3 = a3 + b3
d3 = a3 - b3
e3 = a3 * b3
f3 = a3 / b3
print(c3) #wynik dodawania wynosi, 9
print(d3) #wynik odejmowania wynosi 1
print(e3) #wynik mnozenia wynosi 20
print(f3) #wynik dzielenia wynosi 1.25

#zad 4
a = 5
b = 7
c = 10
d = a%b%c
print(d) # wynik modulo wynosi 5

# zad 5

a = float(input("Podaj długość a: "))
b = float(input("Podaj długość b: "))
c = a * b
print(f"Pole wynosi: %2.2f"% c)

# zad 6
import math
r = float(input("Podaj promień kuli: "))
v = round((4/3) * math.pi * (r**3), 2)
p = round(4 * math.pi * (r ** 2), 2)
print(f"Objętość wynosi: {v}, a powierzchnia wynosi {p}")
# Podaj promień kuli: 5
# Objętość wynosi: 523.6, a powierzchnia wynosi 314.16

# zad 7
c = float(input("Podaj temperaturę w stopniach Celsujsza: "))
f = 32 + (9.0*c)/5
print(f"W stopniach Fahrenheita ta temperatura wynosi: {f}")

# zad 8
liczba = int(input("Podaj liczbę: "))
if liczba > 100:
    print("Liczba jest większa od 100!")
elif liczba < 0:
    print("Liczba jest mniejsza od 0!")
else:
    print("Liczba jest pomiędzy 0 a 100!")

#zad 9
while True:
    litera = input("Podaj literę: ")
    if litera == "c":
        print("Podałeś litere c, koncze program")
        break
    else:
        litera = input("Podaj literę: ")

