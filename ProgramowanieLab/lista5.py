#1
def sumuj_liste(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + sumuj_liste(lista[1:])

print(sumuj_liste([1, 2, 3, 4, 5]))
#2
def oblicz(n):
    if n == 0:
        return 0
    else:
        return n + oblicz(n - 1)

    return wynik

print("wynik obliczania to", oblicz(5))

#3
def sumuj(n2):
    if n2 == 0:
        return 0
    else:
        return n2 % 10 + sumuj(n2//10)



n2 = input("Podaj liczbę: ")
n2 = int(n2)
print("wynik sumy to", sumuj(n2))

#4
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("4 element ciagu fibonnaciego to:", fibonacci(4))

#5
def rekurencyjnie_nwd(n, m):
    if m == 0:
        return n
    else:
        return rekurencyjnie_nwd(m, n % m)

print("nwd 3 i 6 to:", rekurencyjnie_nwd(6, 3))
#6
def iteracyjne_nwd(n, m):
    while n != m:
        if n > m:
            n = n - m
        else:
            m = m - n
    return n

print("nwd 9 i 5 to:", iteracyjne_nwd(9, 5))
#7
# an=a1+(n−1)⋅r
def ciag_aryt(an, a1, r):
    if an == 1:
        return a1
    else:
        return ciag_aryt(an-1, a1, r) + r

print("ciag art", ciag_aryt(3, 0, 2))

#8
#an=a1⋅qn−1
def ciag_geo(an, a1, q):
    if an == 1:
        return a1
    else:
        return ciag_geo(an-1, a1, q) * q
print("ciag geo", ciag_geo(3, 1, 2))