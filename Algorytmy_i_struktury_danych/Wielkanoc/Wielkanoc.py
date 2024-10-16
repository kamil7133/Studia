class Zadanie:
    def algorytmGaussa(self, n): #<- n = rok
        if n > 2200 or n < 325:
            raise ValueError("Podaj zakres roku od 325 do 2200")
        elif n < 1583:
            x = 15
            y = 6
        elif 1583 <= n < 1700:
            x = 22
            y = 2
        elif 1700 <= n < 1800:
            x = 23
            y = 3
        elif 1800 <= n < 1900:
            x = 23
            y = 4
        elif 1900 <= n < 2100:
            x = 24
            y = 5
        elif 2100 <= n < 2200:
            x = 24
            y = 6

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