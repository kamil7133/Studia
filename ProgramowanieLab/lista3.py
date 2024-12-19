#zad 1
import random

for i in range(10):
    ll = random.randint(0, 1000) # liczba losowa w zakresie od 0 do 1000.
    print(ll)

#zad 2
for i in range(1,11):
    print(i)
i = 1
while i != 11:
    print(i)
    i += 1
# zad 3
x = int(input("Podaj liczbe do silni: "))
wynik = 1
for i in range(1, x + 1):
    wynik *= i
# zad 4
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
# zad 5
i = 1
while i != 31:
    if i % 3 == 0:
        print(i)
    i += 1
# zad 6
for i in range(1,31):
    if i % 2 != 0:
        continue
    else:
        print(i)

# zad 7

def sprawdz_alfabet():
    x = input("Podaj literę: ")
    alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    index = 0

    while index < len(alfabet):
        if alfabet[index] != x:
            print(alfabet[index])
            index += 1
        else:
            break
    print(x)
sprawdz_alfabet()

print(x)
# zad 8
i = 1
liczba = 1
x = int(input("Podaj liczbe do zsumowania: "))
while i < x:
    i += 1
    liczba += i
print(liczba)
# zad 9
def zadanie_9():
    x = int(input("Podaj liczbe: "))
    wynik = 0
    for i in range(0, x):
        if i % 2 == 0:
            wynik += i
        else:
            continue
    print(wynik)
zadanie_9()
# zad 10
i = 1
while i > 0:
    for i in reversed(range(1, 100)):
        if i % 3 == 0 and i % 2 != 0:
            print(i)
            i -= 1
        else:
            i -= 1
            continue
# zad 11
for i in reversed(range(-100, 101)):
    if i % 3 == 0:
        continue
    if i % 8 == 0:
        continue
    else:
        print(i)
# zad 12
i = "0"
j = "1"
for i in range(8):
    for j in range(8):
        print((i + j) % 2, end=" ")
    print()
# zad 13
for i in range(1, 6):
    for j in range(1, 6):
        print(j * i, end=" ")
    print()
