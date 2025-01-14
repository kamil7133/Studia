class Zadanie:
    def Arab(self, n): #n <- rok
        if not isinstance(n, int):
            raise ValueError("Podany rok musi być liczbą")
        roman_numerals = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }
        f = ""
        for i, j in roman_numerals.items():
            while n >= i:
                f += j
                n -= i
        return f


zadanie = Zadanie()

n = input("Podaj rok jaki chcesz zamienić: ")

try:
    n = int(n)
    rok = zadanie.Arab(n)
    print(f"{rok}")
except ValueError as g:
    print(g)