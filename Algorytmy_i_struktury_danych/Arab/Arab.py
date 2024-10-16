class Zadanie:
    def Arab(self, n): #n <- rok
        if not isinstance(n, int):
            raise ValueError("Podany rok musi być liczbą")
        f = ""
        while n > 0:
            if n >= 1000:
                f += "M"
                n -= 1000
            elif n >= 900:
                f += "CM"
                n -= 900
            elif n >= 500:
                f += "D"
                n -= 500
            elif n >= 400:
                f += "CD"
                n -= 400
            elif n >= 100:
                f += "C"
                n -= 100
            elif n >= 90:
                f += "XC"
                n -= 90
            elif n >= 50:
                f += "L"
                n -= 50
            elif n >= 40:
                f += "XL"
                n -= 40
            elif n >= 10:
                f += "X"
                n -= 10
            elif n == 9:
                f += "IX"
                n -= 9
            elif n >= 5:
                f += "V"
                n -= 5
            elif n == 4:
                f += "IV"
                n -= 4
            elif n >= 1:
                f += "I"
                n -= 1
        return f

zadanie = Zadanie()

n = input("Podaj rok jaki chcesz zamienić: ")

try:
    n = int(n)
    rok = zadanie.Arab(n)
    print(f"{rok}")
except ValueError as g:
    print(g)