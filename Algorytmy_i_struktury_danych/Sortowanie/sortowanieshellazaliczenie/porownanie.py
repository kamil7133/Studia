import random
import time

# moj algorytm sortowania
def sortowanie_shelle(lista):
    dlugosc = len(lista)
    czy_zamiana = False
    krok = dlugosc
    while not czy_zamiana:
        if krok >= 1:
            krok = krok // 2
            while True:
                czy_zamiana = False
                i = 0
                while i <= dlugosc - krok - 1:
                    if lista[i] > lista[i + krok]:
                        temp = lista[i + krok]
                        lista[i + krok] = lista[i]
                        lista[i] = temp
                        czy_zamiana = True
                    i += 1
                if not czy_zamiana:
                    break
        else:
            czy_zamiana = True
    return lista

# generowanie losowych danych
def generuj_dane(rozmiar, stopien_posortowania):
    """
    generuje dane w zależności od stopnia posortowania.
    stopien_posortowania:
      - 'random': całkowicie losowe
      - '25_sorted': 25% elementów posortowanych
      - '50_sorted': 50% elementów posortowanych
      - '100_sorted': całkowicie posortowane
      - 'reverse_sorted': posortowane malejąco
    """
    dane = [random.randint(0, rozmiar) for _ in range(rozmiar)]

    if stopien_posortowania == '100_sorted':
        dane.sort()
    elif stopien_posortowania == 'reverse_sorted':
        dane.sort(reverse=True)
    elif stopien_posortowania in ['25_sorted', '50_sorted']:
        czesc = 0.25 if stopien_posortowania == '25_sorted' else 0.50
        indeks_podzialu = int(rozmiar * czesc)
        pierwsza_czesc = sorted(dane[:indeks_podzialu])
        druga_czesc = dane[indeks_podzialu:]
        dane = pierwsza_czesc + druga_czesc
    return dane

# mierzenie czasu działania algorytmów
def zmierz_czas(funkcja_sortujaca, dane):
    start = time.perf_counter()
    funkcja_sortujaca(dane)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    rozmiary = [1000, 2000, 5000]
    stopnie_posortowania = ['random', '25_sorted', '50_sorted', '100_sorted', 'reverse_sorted']

    wyniki = {stopien: {} for stopien in stopnie_posortowania}

    for stopien in stopnie_posortowania:
        for rozmiar in rozmiary:
            dane = generuj_dane(rozmiar, stopien)
            dane_dla_shelle = dane.copy()
            dane_dla_wbudowanego = dane.copy()

            czas_shelle = zmierz_czas(sortowanie_shelle, dane_dla_shelle)
            czas_wbudowane = zmierz_czas(lambda lista: lista.sort(), dane_dla_wbudowanego)

            wyniki[stopien][rozmiar] = (czas_shelle, czas_wbudowane)
            print(f"Stopień: {stopien}, Rozmiar: {rozmiar}, Shell Sort: {czas_shelle:.6f}, Wbudowane: {czas_wbudowane:.6f}")
