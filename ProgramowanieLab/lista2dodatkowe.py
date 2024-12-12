# zad 1
i = int(input("Podaj liczbe: "))
if i < 0:
    print("liczba jest ujemna")
elif i > 0:
    print("liczba jest dodatnia")
else:
    print("liczba jest rowna zero")
zad 2
pkt = int(input("Podaj liczbe punktow od 0 do 100: "))
if pkt < 0 or pkt > 100:
    print("liczba jest nieprawidlowa")
elif pkt > 0 and pkt < 50:
    print("Ocena 2.0")
elif pkt > 51 and pkt < 60:
    print("Ocena 3.0")
elif pkt > 61 and pkt < 70:
    print("Ocena 3.5")
elif pkt > 71 and pkt < 80:
    print("Ocena 4.0")
elif pkt > 81 and pkt < 90:
    print("Ocena 4.5")
elif pkt > 91 and pkt < 100:
    print("Ocena 5.0")
else:
    print("Nieprawidlowy ciag znakow")
zad 3
password = "maslo"
pas_uzy = input("Podaj haslo: ")
if password == pas_uzy:
    print("Haslo poprawne")
else:
    print("Haslo niepoprawne")
# zad 4
i = input("Podaj ciag znakow, pamietaj ze zakres to 10: ")
dlugosc = len(i)
zakres = 10
print(f"Dlugosc ciagu znakow: {dlugosc}")
if dlugosc > zakres:
    przekroczenie = dlugosc - zakres
    print(f"Ciag znakow zostal przekroczony o {przekroczenie} liter !")
else:
    print("Poprawne !")
# zad 5
a = input("Podaj liczbe a: ")
b = input("Podaj liczbe b: ")
c = input("Podaj liczbe c: ")
if a < 0 or b < 0 or c < 0:
    print("Niepoprawne !")
elif a**2 + b**2 == c**2:
    print("Spelniaja warunek pitagorasa")
else:
    print("Nie spelniaja warunku pitagorasa")

# zad 6
q = input("Podaj q: ")
p = input("Podaj p: ")
if not(p and q) == (not(p) or not(q)):
    print("Sa takie same")
else:
    print("Nie sa takie same")
# zad 7
liczba_dni = int(input("Podaj liczbe dni: "))
if liczba_dni >= 10:
    print("150zl")
elif liczba_dni < 10 and liczba_dni > 5:
    print("200zl")
elif liczba_dni < 5:
    print("250zl")