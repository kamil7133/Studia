#1
krotka4 = (-30,250,-70)
wynik=sum(krotka4)
print('Wynik sumowania wartości z krotki4 wynosi: ',wynik)

#2
krotka = (1,2)
krotka = list(krotka)
krotka.pop(0)
krotka = tuple(krotka)
print(f"wynik listy to: {krotka}")
#3
lista_krotek = [(1,2),(3,4),(5,6),(7,8)]
def sprawdz_indeks(l: list, w: tuple) -> int:
    counter = 0
    for i in l:
        if i == w:
            counter += 1
        else:
            pass
    return counter


print(sprawdz_indeks(lista_krotek, (1, 2)))
#4
def odwroc(tuplee: list) -> tuple:
    tuplee = list(tuplee)
    tuplee.reverse()
    odwrocona = tuple(tuplee)
    return odwrocona

print(odwroc((1, 2, 3)))

#5
def dodaj_zero_na_koniec(l: list):
    nowa_lista = []
    for i in l:
        x = list(i)
        for j in range(len(x)):
            if j == len(x) - 1:
                x.pop(j)
                x.append(0)
                x = tuple(x)
                nowa_lista.append(x)
            else:
                pass

    return nowa_lista



list2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

print(dodaj_zero_na_koniec(list2))

#6
def usun_puste_krotki(l):
    nowa_lista = []
    for i in l:
        x = list(i)
        if not i:
            pass
        else:
            zamien_krotka = tuple(x)
            nowa_lista.append(zamien_krotka)
    return nowa_lista

list2 = [(),(),('',),('i1','i2'),('i1','i2','i3'),('i4',)]
print(usun_puste_krotki(list2))

#7
def sort_tuple(t:tuple):
    posortowana = list(t)
    posortowana.sort()
    posortowana = tuple(posortowana)
    return posortowana

krotka = (1,4,3,2,5)
print(sort_tuple(krotka))

#8
def konwersja_lancucha(tekst:str) -> tuple:
    krotka = []
    for i in tekst:
        krotka.append(i)
    krotka = tuple(krotka)
    return krotka

tekst = "Kamil"
print(konwersja_lancucha(tekst))

#9
def srednia_krotek(krotka):
    srednia = []
    for i in range(len(krotka[0])):
        suma = 0
        for j in krotka:
            suma += j[i]
        srednia.append(suma / len(krotka))
    return srednia


krotka1 = ((1, 2, 3, 4), (10, 15, 25, 35), (70, 80, 90, 100), (-20, -15, -10, -5))

print(srednia_krotek(krotka1))

#10
def sprawdzenie(krotka:tuple, w: str) -> bool:
    pomoc = list(krotka)
    for i in pomoc:
        x = list(i)
        if w in x:
            return True
        else:
            pass
    return False

krotka1 = (('pon', 'wto', 'srd'), ('czw', 'ptk', 'sob'), ('ndz', 'pon', 'wto'))
print(sprawdzenie(krotka1, 'kamil'))
