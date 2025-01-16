#1
slownik2 = {'dane1':-30,'dane2':250,'dane3':-70}
wynik=0
for klucz in slownik2:
 wynik+=slownik2[klucz]
print('Wynik sumowania wartości ze słownika2 wynosi: ',wynik)
#2
slow = {
    'd1':1.1,
    'd2':2.2,
    'd3':3.3
}
def iloczyn(slow):
    wynik = 1
    for i in slow.values():
        wynik *= i
    return wynik

print(round(iloczyn(slow), 7))
#3
slow1 = {
    'd1':1.1,
    'd2':2.2,
    'd3':3.3
}

slow2 = {
    'd4':4.6,
    'd5':5.6,
    'd6':6.6
}

for i, j in slow1.items():
    slow2.update({i:j})

print(slow2)
#4
def slow_pot(n):
    slow1 = {}
    for i in range(1,n+1):
        slow1.update({i:i*i*i})

    return slow1

print(slow_pot(5))
#5
def posort(slow1):
    nowy = {}
    for klucz in sorted(slow1.keys()):
        nowy[klucz] = slow1[klucz]
    return nowy
print(posort({"banan":1, "jablko":2, "mango":3, "ananas":0}))
#6
def unikalne(slow6):
    unikalne = set()
    for wartosc in slow6.values():
        unikalne.add(wartosc)
    return unikalne

print(unikalne({"a":5,"m":5,"n":5,"j":9,"r":7,"g":3,"f":5,"d":8,"b":8}))
#7
def utworz_slow(teskt):
    slownik = {}
    indeks = 1
    for litera in teskt:
        slownik[indeks] = litera
        indeks += 1
    return slownik

print(utworz_slow("ant"))
#8
def czestosc(slow, para):
    klucz, wartosc = para
    licznik = 0
    for i, j in slow.items():
        if i == klucz and j == wartosc:
            licznik += 1
        return licznik
print(czestosc({1:'a',2:'n',3:'n',4:'t',5:'a'}, (1, "a")))
