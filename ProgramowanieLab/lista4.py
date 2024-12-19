# #zad 2
# def zad2(a,b,c):
#     x = max(a,b,c)
#     print(x)
# zad2(1,4,8)
# # zad 3
# def zad3(a):
#     a = a[::-1]
#     print(a)
# zad3("abc123")
# # zad 4
# def zad4(a):
#     if a > 0 and a < 100:
#         return True
#     else:
#         return False
# print(zad4(5))
# # zad 5
# def silnia(x):
#     wynik = 1
#     for i in range(1, x + 1):
#         wynik *= i
#     return wynik
# x = int(input("Podaj liczbe do silni: "))
# print(silnia(x))
# # zad 6
# def oblicza(a: str):
#     duze = 0
#     male = 0
#     for i in a:
#         if i.islower():
#             male += 1
#         if i.isupper():
#             duze += 1
#     return duze, male
#
# x = input("Podaj ciag znakow: ")
# print(oblicza(x))
# zad 7
def zad7(wartosc):
    wynik = 0
    for i in range(1, wartosc):
        if wartosc % i == 0:
            wynik += i

    if wynik == wartosc:
        print("jest to liczba doskonala")
    else:
        print("nie jest to liczba doskonala")

wartosc = int(input("podaj liczbe: "))
zad7(wartosc)
# zad 8
def palindrom(a):
    b = a[::-1]
    if a == b:
        return "Jest to palindrom"
    else:
        return "Przykro mi, nie jest to palindrom"

print(palindrom("potop"))
#zad 9
import random
import time
def zad9():
    a = random.randint(1,1000)
    pierwiastek = a**(1/2)
    time.sleep(1)
    print(pierwiastek, "<-- Jest to pierwiastek z wylosowanej liczby, a wylosowana liczba to:", a)
zad9()