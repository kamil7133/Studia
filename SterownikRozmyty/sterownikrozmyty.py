import matplotlib.pyplot as plt
import numpy as np


# ==============================================================================
# 1. CZĘŚĆ MATEMATYCZNA (Logika rozmyta)
# ==============================================================================

def trapmf(x, a, b, c, d):
    """
    Uniwersalna funkcja obliczająca przynależność do trapezu.
    x - badana wartość
    a, b, c, d - współrzędne wierzchołków trapezu na osi X
    """
    if x <= a or x >= d:
        return 0.0
    elif a <= x < b:
        return (x - a) / (b - a)  # Zbocze rosnące
    elif b <= x <= c:
        return 1.0  # Płaski szczyt
    elif c < x < d:
        return (d - x) / (d - c)  # Zbocze opadające
    return 0.0


def get_memberships(val):
    """
    Zwraca stopnie przynależności (N, ŚR, W) dla danej wartości.
    Definicje kształtów przepisane z Twoich notatek:
    N (Niska):   0-30 (opada 20-30)
    ŚR (Średnia): 20-80 (rośnie 20-30, płasko 30-70, opada 70-80)
    W (Wysoka):  70-100 (rośnie 70-80)
    """
    mu_n = trapmf(val, 0, 0, 20, 30)
    mu_sr = trapmf(val, 20, 30, 70, 80)
    mu_w = trapmf(val, 70, 80, 100, 100)
    return mu_n, mu_sr, mu_w


# ==============================================================================
# 2. SILNIK STEROWNIKA (Główna funkcja obliczeniowa)
# ==============================================================================

def oblicz_moc_ciagnika(zwiezlosc, wilgotnosc, pokaz_wykres=True):
    print(f"\n--- ROZPOCZYNAM OBLICZENIA DLA: Z={zwiezlosc}, W={wilgotnosc}% ---")

    # KROK 1: FUZZYFIKACJA (Obliczenie przynależności wejść)
    z_n, z_sr, z_w = get_memberships(zwiezlosc)
    w_n, w_sr, w_w = get_memberships(wilgotnosc)

    print(f"1. Fuzzyfikacja:")
    print(f"   Zwięzłość: N={z_n:.2f}, ŚR={z_sr:.2f}, W={z_w:.2f}")
    print(f"   Wilgotność: N={w_n:.2f}, ŚR={w_sr:.2f}, W={w_w:.2f}")

    # KROK 2: WNIOSKOWANIE (Aplikacja bazy reguł - MIN)
    # Tabela reguł przepisana z Twoich notatek (3x3)

    # Wiersz 1: Zwięzłość Niska
    r1 = min(z_n, w_n)  # -> ŚR
    r2 = min(z_n, w_sr)  # -> N
    r3 = min(z_n, w_w)  # -> N

    # Wiersz 2: Zwięzłość Średnia
    r4 = min(z_sr, w_n)  # -> ŚR
    r5 = min(z_sr, w_sr)  # -> ŚR
    r6 = min(z_sr, w_w)  # -> N

    # Wiersz 3: Zwięzłość Wysoka
    r7 = min(z_w, w_n)  # -> W
    r8 = min(z_w, w_sr)  # -> W
    r9 = min(z_w, w_w)  # -> ŚR

    # KROK 3: AGREGACJA (Grupowanie wyników - MAX)
    # Zbieramy wszystkie reguły, które dają ten sam wynik
    moc_n_cut = max(r2, r3, r6)  # Wszystkie dające N
    moc_sr_cut = max(r1, r4, r5, r9)  # Wszystkie dające ŚR
    moc_w_cut = max(r7, r8)  # Wszystkie dające W

    print(f"2. Agregacja (Poziomy odcięcia):")
    print(f"   Moc Niska:   {moc_n_cut:.2f}")
    print(f"   Moc Średnia: {moc_sr_cut:.2f}")
    print(f"   Moc Wysoka:  {moc_w_cut:.2f}")

    # KROK 4: DEFUZZYFIKACJA
    licznik = 0.0
    mianownik = 0.0
    x_axis = np.arange(0, 100.1, 0.5)  # Próbkowanie osi X co 0.5%
    y_plot = []

    for x in x_axis:
        # Pobieramy kształty bazowe dla danego punktu x
        mu_n, mu_sr, mu_w = get_memberships(x)

        # Przycinamy je do poziomów wyliczonych w agregacji
        final_n = min(mu_n, moc_n_cut)
        final_sr = min(mu_sr, moc_sr_cut)
        final_w = min(mu_w, moc_w_cut)

        # Wynikowy kształt to obwiednia (maksimum)
        y_final = max(final_n, final_sr, final_w)
        y_plot.append(y_final)

        # Sumowanie momentów (całkowanie numeryczne)
        licznik += x * y_final
        mianownik += y_final

    if mianownik == 0:
        wynik = 0
    else:
        wynik = licznik / mianownik

    print(f"3. Wynik końcowy (COG):")
    print(f"   Sugerowana MOC: {wynik:.2f}%")

    # ==========================================================================
    # 3. WIZUALIZACJA
    # ==========================================================================
    if pokaz_wykres:
        plt.figure(figsize=(10, 6))

        # Rysujemy wynikowy kształt
        plt.fill_between(x_axis, y_plot, color='orange', alpha=0.4, label='Wynikowa Agregacja')
        plt.plot(x_axis, y_plot, color='darkorange', linewidth=2)

        # Rysujemy oryginalne kształty w tle (szare)
        y_n_base = [trapmf(i, 0, 0, 20, 30) for i in x_axis]
        y_sr_base = [trapmf(i, 20, 30, 70, 80) for i in x_axis]
        y_w_base = [trapmf(i, 70, 80, 100, 100) for i in x_axis]
        plt.plot(x_axis, y_n_base, 'k:', alpha=0.2)
        plt.plot(x_axis, y_sr_base, 'k:', alpha=0.2)
        plt.plot(x_axis, y_w_base, 'k:', alpha=0.2)

        # Linia wyniku
        plt.axvline(x=wynik, color='red', linewidth=3, linestyle='--', label=f'Wynik: {wynik:.2f}%')

        plt.title(f'Sterownik Rozmyty: Zwięzłość={zwiezlosc}, Wilgotność={wilgotnosc}%')
        plt.xlabel('Moc Ciągnika [%]')
        plt.ylabel('Przynależność')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

    return wynik


# ==============================================================================
# 4. URUCHOMIENIE PROGRAMU
# ==============================================================================

if __name__ == "__main__":
    # Tutaj wpisz dane testowe ze swojego projektu
    test_zwiezlosc = 72
    test_wilgotnosc = 25

    # Wywołanie sterownika
    oblicz_moc_ciagnika(test_zwiezlosc, test_wilgotnosc)

'''
--- ROZPOCZYNAM OBLICZENIA DLA: Z=72, W=25% ---
1. Fuzzyfikacja:
   Zwięzłość: N=0.00, ŚR=0.80, W=0.20
   Wilgotność: N=0.50, ŚR=0.50, W=0.00
2. Agregacja (Poziomy odcięcia):
   Moc Niska:   0.00
   Moc Średnia: 0.50
   Moc Wysoka:  0.20
3. Wynik końcowy:
   Sugerowana MOC: 55.16%
'''