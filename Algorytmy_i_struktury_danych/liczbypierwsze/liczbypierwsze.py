class Zadanie():
    def czylpierwsza(self, n):
        if n <= 1:
            return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True



zadanie = Zadanie()
n = input("Podaj liczbę do sprawdzenia: ")
n = int(n)

if zadanie.czylpierwsza(n) is True:
    print("Liczba jest liczbą pierwszą.")
else:
    print("Liczba nie jest liczbą pierwszą")

