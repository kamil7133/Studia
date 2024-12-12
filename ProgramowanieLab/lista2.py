# zad 1
a= int(input("Podaj wartość zmiennej a: "))
b=int(input("Podaj wartość zmiennej b: "))
if a >= 0 and a < 10 and b >= 0 and b < 10:
 il=a*b
 print("Iloczyn wynosi: " , il)
else:
 print("Dane poza zakresem od 0 do 9!")
# zad 2
li = int(input("Podaj liczbę: "))
if li > 0:
    print(li)
elif li < 0:
    li *= -1
    print(li)
# zad 3
i = int(input("Podaj liczbę: "))
if i > 100:
    print("Liczba jest większa od 100!")
elif i > 0 and i < 100:
    print("Liczba jest pomiędzy 0 a 100")
else:
    print("Liczba jest mniejsza od zera!")
# zad 4
i = str(input("Podaj liczbę: "))
match i:
    case "1":
        print(i)
    case "2":
        print(i)
    case "3":
        print(i)
    case "4":
        print(i)
    case "5":
        print(i)
    case "6":
        print(i)
    case "7":
        print(i)
    case "8":
        print(i)
    case "9":
        print(i)
    case _:
        print("Nie podano liczby albo liczba jest za duza! Podaj cyfre od 1-9")
# zad 5
wybor = input("Czy jest dzis sloneczny dzien? (t/n): ").lower()
match wybor:
    case "t":
        print("Piekny dzien!")
    case "n":
        print("Brak slonca")
    case _:
        print("Wprowadzono nieprawidlowe wartosci")
# zad 6
dzien = input("Podaj dzien: ").lower()
match dzien:
    case "poniedzialek":
        print("Poniedzialek")
    case "wtorek":
        print("Wtorek")
    case "sroda":
        print("Sroda")
    case "czwartek":
        print("Czwartek")
    case "piatek":
        print("Piatek")
    case "sobota":
        print("Sobota")
    case "niedziela":
        print("Niedziela")
    case _:
        print("Niepoprawny ciag znakow")
# zad 7
nr_indeksu = int(input("Podaj nr indeksu: "))
plec = ""
rok = ""
if nr_indeksu % 2 == 0:
    plec = "mezczyzna"
elif nr_indeksu % 2 != 0:
    plec = "kobieta"
else:
    print("Podano nieprawidlowa wartosc")

if nr_indeksu >= 10000:
    rok = "2019 albo pozniej"
elif nr_indeksu >= 9000:
    rok = "2018"
elif nr_indeksu >= 8000:
    rok = "2017"
elif nr_indeksu >= 7000:
    rok = "2016"
elif nr_indeksu >= 6000:
    rok = "2015"
elif nr_indeksu >= 5000:
    rok = "2014"
elif nr_indeksu >= 4000:
    rok = "2013"
elif nr_indeksu >= 3000:
    rok = "2012"
elif nr_indeksu >= 2000:
    rok = "2011"
elif nr_indeksu >= 1000:
    rok = "2010"
else:
    rok = "przed 2010 lub niepoprawny"

print(f"Jestes {plec} i zaczales w roku {rok}")

# zad 8
a = float(input("Podaj liczbe a: "))
b = float(input("Podaj liczbe b: "))
c = float(input("Podaj liczbe c: "))
delta = b**2 - 4*a*c
x1 = (-b + (delta**(1/2)) / (2*a))
x2 = (-b - (delta**(1/2)) / (2*a))
if delta < 0:
    print(f"Przy twoich liczbach do a,b,c delta wynosi {delta}. delta jest mniejsza od zera wiec nie ma x1 i x2")
elif delta == 0:
    print(f"Przy twoich liczbach do a,b,c delta wynosi {delta}. delta jest rowna zero wiec x1 jest takie same jak x2, twoj wynik x1 i x2 to: {x1},{x2}")
elif delta > 0:
    print(f"x1 wynosi {x1}, a x2 wynosi {x2}")