#algorytm euklidesa

class Zadanie:
    def nwd(self, a, b): #funkcja z inputami a i b
        if a and b > 0: #jezeli a i b jest wieksze od 0 to wykonuj
            while a != b: #dopóki a nie jest równe b
                if a > b: #jezeli a wieksze od b
                    a -= b #to odejmij b od a
                else:
                    b -= a #odejmij a od b
            return a
        else: #w innym wypadku wydrukuj
            print("Złe liczby")

a, b = input("Podaj dwie liczby: ").split() #.split dzieli podana wartosc dwoch liczb odzielona spacja na dwie zmienne
a = int(a) #deklaracja ze a jest liczba calkowita
b = int(b) #-=-
zadanie = Zadanie()
wynik = zadanie.nwd(a, b)
if a and b > 0: #jeszcze raz sprawdzenie czy a i b jest mniejsze od 0, jezeli nie to uzytkownik podal zle liczby
    print(f"Najwiekszy wspolny dzielnik to: {wynik}")

#liczby podawać bez przecinka np. 892 292