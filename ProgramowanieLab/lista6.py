#1
tab4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(tab4)):
    for j in range(len(tab4[i])):
        print( tab4[i][j], end=' ')
    print()

tab3 = [[9, 8, 7, 6], [5, 4], [3, 2, 1]]
for wiersz in tab3:
    for kolumna in wiersz:
        print(kolumna, end=' ')
    print()

#2
tab1 = [[1,2,3,4], [5,6,7,8]]
tab2 = [[9,10,11,12], [13,14,15,16]]
tab3 = []

i = 0
while i < len(tab1):
    tab3.append(tab1[i])
    i += 1
j=0
while j < len(tab2):
    tab3.append(tab2[j])
    j += 1

print(tab3)

#3
def zliczanie(lista1, numerek):
    miejsce = 0
    counter = 0
    for i in range(len(lista1)):
        if numerek == lista1[i]:
            counter += 1
    for j in lista1:
        if j in lista1:
            miejsce = lista1.index(numerek)
    return counter, miejsce

print(zliczanie([3, 2, 2, 2, 4, 5, 6, 2, 2, 8], 2))
#4
lista = []
for i in range(1, 21):
    lista.append(i)
    reverse = lista[::-1]

for j in reverse:
    if j % 3 == 0 or j % 7 == 0:
        reverse.pop(j)
    else:
        pass

print(reverse)
#5
tab = list(input("Podaj nie wiecej niz 15 liczb:"))
b = 0
c = 0
for i in tab:
    b += int(i)
for j in range(len(tab)):
    c += int(j)

srednia_aryt = b / c
print(srednia_aryt)

#6
def wyznacz_max_min(n: list):
    maxy = max(n)
    miny = min(n)
    return maxy, miny

lista = list(input("Podaj cztery liczby: "))
print(f"lista liczb to: {lista}")
print(wyznacz_max_min(lista))
# 7
list = []
while len(list) != 5:
    a = int(input('Podaj liczbe: '))
    if a > 20 or a < 0:
        print('błędna liczba')
    else:
        list.append(a)

maxy = max(list)
miny = min(list)
list.remove(maxy)
list.remove(miny)
wynik = 0
for i in list:
    wynik += i
print(f"Ostateczna ocena za wynik to: {wynik}")
# zad8
n = 5
tablica = []
for i in range(1, n + 1):
    wiersz = []
    for j in range(1, n + 1):
        if j <= i:
            wiersz.append(j)
        else:
            wiersz.append(i)
    tablica.append(wiersz)

for wiersz in tablica:
    print(wiersz)
#zad 9
wiersze = 4
kolumny = 4
tablica = []
for i in range(1, wiersze + 1):
    wiersz = []
    for j in range(1, kolumny + 1):
        wiersz.append(i * j)
    tablica.append(wiersz)

for wiersz in tablica:
    print(wiersz)


