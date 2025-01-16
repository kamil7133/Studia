#1
def pierwsze_znaki(lista7, znak):
 result = [i for i in lista7 if i.startswith(znak)]
 return result
lista7 = ["cdba", "abcd", "adbg", "bacd", "bdac", "cdae", "mwar", "sgrs",
"atre"]
print("\nLista poczatkowa:")
print(lista7)
znak = "a"
print("\nElementy zaczynajace sie na",znak)
print(pierwsze_znaki(lista7, znak))
#2
def iloczyn(l: list):
    wynik = 1
    for i in range(len(l)):
        wynik *= l[i]
    return wynik
print(round(iloczyn([1.1, 2.2, 3.3]), 7))
#3
def min_max(lista: list):
    return min(lista), max(lista)
print(min_max([1,2,3,4,5,6,7,8,9,10]))
#4
def usuwanie_powtarzajacej(lista: list):
    wynikowa = []
    for i in range(len(lista)):
        if lista[i] in wynikowa:
            pass
        else:
            wynikowa.append(lista[i])

    return wynikowa

print(usuwanie_powtarzajacej([1,2,3,4,5,5,5,6,7,8,8,9,10]))
#5
def lista_zankow(lista: list):
    wynikowa = ""
    pomocnicza = ""
    for i in lista:
        pomocnicza = pomocnicza.join(i)
        wynikowa += pomocnicza
    return wynikowa
print(f"Połączony string: {lista_zankow(["k","a","m","i","l"])}")
#6
lista1 = ["k","a","m","i","l"]
lista2 = ["k", "a", "c", "p", "e", "r"]
for i in lista1:
    for j in lista2:
        if i == j:
            print(f"znaleziono taki sam znak w obu listach!: {i}")

#7
lista = ["a","b","c","d","e","f","g","h","i","j", "k", "l", "m", "n", "o"]
def split_list(lista, n):
    pomoc = []
    for i in range(0, len(lista), n):
        y = lista[i:i + n]
        pomoc.append(y)
    return pomoc

print(split_list(lista, 3))
#8
lista1 = [10, 20, 30, 40, 50, 100]
lista2 = [15, 25, 35, 45]

for i in range(len(lista1)):
    if (i + 1) == len(lista1):
        lista1.pop(i)
        for j in lista2:
            lista1.append(j)
    else:
        pass
print(lista1)

#9
def dolacz(lista: list, slowo: str):
    nowa = []
    for i in lista:
        nowa.append(slowo + str(i))
    return nowa

print(dolacz([1, 2, 3], "kamil"))
#10
def przesun(lista: list):
    nowa_lista = []
    licznik_zero = 0
    for x in lista:
        print(x)
        if x == 0:
            licznik_zero += 1
        else:
            nowa_lista.append(x)
    for _ in range(licznik_zero):
        nowa_lista.append(0)
    return nowa_lista
print(przesun([1, 2, 0, 5, 0, 1, 2, 0, 3]))

#11
def sito(n):
    tab = [0] * (n + 1)
    tab[0] = 1
    tab[1] = 1
    for i in range(2, int(n**0.5) + 1):
        if tab[i] == 0:
            for j in range(i * i, n + 1, i):
                tab[j] = 1
    pierwsze = []
    for i in range(n + 1):
        if tab[i] == 0:
            pierwsze.append(i)
    return pierwsze

print(sito(100))