# # 1
# import urllib.request
# import requests
# import urllib3
# plik_url = 'http://textfiles.com/music/stairway.lyr'
# http = urllib3.PoolManager()
# response = http.request('GET', plik_url)
# data = response.data.decode('utf-8')
# for line in urllib.request.urlopen(plik_url):
#     print(line.decode('utf-8'))
# response = requests.get(plik_url)
# if (response.status_code):
#     dane = response.text
#     for linia in enumerate(dane.split('\n')):
#         print(linia)

#2
def odczyt_pliku(nazwa):
    tabela = []
    with open(nazwa) as f:
        for i in f:
            tabela.append(i)

    return tabela

print(odczyt_pliku('tekst.txt'))

#3
def copy_file(plik1, plik2):
    plik1 = open(plik1, 'r')
    plik2 = open(plik2, 'w')
    for line in plik1:
        plik2.write(line)

    plik1.close()
    plik2.close()

copy_file('copy1.txt', 'copy2.txt')

#4
def dlugosc_slowa(nazwa):
    tabela = []
    with open(nazwa) as f:
        for i in f:
            tabela.append(i)
    counter = 0
    slowo = ""
    for j in tabela:
        if counter < len(j):
            counter = len(j)
            slowo = j
        else:
            pass
    return slowo

print(dlugosc_slowa("tekst2.txt"))

#5
def czestotliwosc(nazwa, slowo):
    tabela = []
    with open(nazwa) as f:
        for i in f:
            tabela.append(i)
    counter = 0
    for j in tabela:
        j = j.strip('\n')
        if j == slowo:
            counter += 1
        else:
            pass
    return counter

print(czestotliwosc('tekst2.txt', 'kamil'))

#6
import random
def losowe(nazwa):
    tabela = []
    with open(nazwa) as f:
        for i in f:
            i = i.strip('\n')
            tabela.append(i)
    losowa_tabela = []
    for j in range(11):
        losowa_tabela.append(random.choice(tabela))

    return losowa_tabela

print(losowe("tekst.txt"))

#7
def odczytanie_ostatnich_lini(nazwa, n):
    with open(nazwa, 'r') as f:
        linie = f.readlines()

        for linia in linie[-n:]:
            print(linia.rstrip())


odczytanie_ostatnich_lini('tekst.txt', 3)

#8
def polacz_pliki(nazwa1, nazwa2, plik_wynikowy):
    with open(nazwa1, 'r') as f1, open(nazwa2, 'r') as f2, open(plik_wynikowy, 'w') as fw:
        linie1 = f1.readlines()
        linie2 = f2.readlines()

        min_linii = min(len(linie1), len(linie2))

        for i in range(min_linii):
            fw.write(f"{linie1[i].strip()} {linie2[i].strip()}\n")
polacz_pliki('tekst.txt', 'tekst2.txt', 'wynik.txt')

#9
def usun_spacje(nazwa, plik_docelowy):
    with open(nazwa, 'r') as zrodlo, open(plik_docelowy, 'w') as cel:
        for linia in zrodlo:
            linia_bez_spacji = linia.replace(' ', '')
            cel.write(linia_bez_spacji)


usun_spacje('tekst.txt', 'bez_spacji.txt')