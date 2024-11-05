class Zadanie:
    def algorytmGaussa(self, n): #<- n = rok
        if n > 2200 or n < 325:
            raise ValueError("Podaj zakres roku od 325 do 2200")
        zakres_lat = {
            (325, 1582): (15, 6),
            (1583, 1699): (22, 2),
            (1700, 1799): (23, 3),
            (1800, 1899): (23, 4),
            (1900, 2099): (24, 5),
            (2100, 2199): (24, 6)
            }

        for (i, j), (x, y) in zakres_lat.items():
            if i <= n <= j:
                break

        a = n % 19
        b = n % 4
        c = n % 7
        d = (19*a + x) % 30
        e = (2*b + 4*c + 6*d + y) % 7
        f = 22 + d + e #dzien miesiaca

        return f

zadanie = Zadanie() #obiekt klasy
n = input("Podaj rok: ")
n = int(n)
try:
    data = zadanie.algorytmGaussa(n)
    int(data)
    if data > 31:
        print("Wielkanoc wypada",(data - 31), "kwietnia")
    else:
        print("Wielkanoc wypada", data, "marca")
except ValueError as e:
    print(e)