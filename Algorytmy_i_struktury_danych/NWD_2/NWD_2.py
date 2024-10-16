class Zadanie:
    def nwd(self, a, b):
        while a % b != 0: #dopoki reszta z dzielenia a i b nie jest rowna 0
            c = a % b #przypisanie reszty z dzielenia a i b do zmiennej pomocniczej c
            a = b
            b = c
        return b

zadanie = Zadanie() #obiekt klasy
a, b = input("Podaj dwie liczby: ").split() #.split dzieli podana wartosc dwoch liczb odzielona spacja na dwie zmienne
a = int(a) #deklaracja ze a jest liczba calkowita
b = int(b)
wynik = zadanie.nwd(a, b)
print(f"Reszta z dzielenia to {wynik}") #wyswietlenie wyniku

