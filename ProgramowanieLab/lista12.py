
from datetime import datetime, timedelta
# #1
# def leap_year(y):
#     if y % 400 == 0:
#         return True
#     if y % 100 == 0:
#         return False
#     if y % 4 == 0:
#         return True
#     else:
#         return False
# print(leap_year(1900))
# print(leap_year(2004))
#2
dzisiaj = datetime.today()
za_tydzien = dzisiaj + timedelta(days=7)
print(f'zadanie 2: data za tydzien {za_tydzien}')
#3

biezacy_rok = datetime.now().year

start_data = datetime(biezacy_rok, 1, 1)
koniec_data = datetime(biezacy_rok, 2, 15)
print("zadanie 3")
while start_data != koniec_data:
    if start_data.weekday() == 1:
        print(start_data)
    start_data += timedelta(days=1)
#4
print("zadanie 4")
biezacy_rok = datetime.now().year
for rok in range(biezacy_rok + 1, biezacy_rok + 4):
    data_6_stycznia= datetime(rok, 1, 6)

    while data_6_stycznia.weekday() != 6:
        data_6_stycznia += timedelta(days=1)

    print(f"rok: {rok} data: {data_6_stycznia}")
#5
biezacy_rok = datetime.now().year

data_30_wrzesnia = datetime(biezacy_rok, 9, 30)

while data_30_wrzesnia.weekday() != 0:
    data_30_wrzesnia += timedelta(days=1)

print(f"zadanie 5: pierwszy poniedziałek po 30 września {biezacy_rok} roku: {data_30_wrzesnia.strftime('%Y-%m-%d')}")

#6
def program_do_wyznaczania_daty():
    biezaca_data = datetime.today()
    data_za_100_dni = biezaca_data + timedelta(days=100)
    return data_za_100_dni

print("zadanie 6:", program_do_wyznaczania_daty())
#7
biezacy_rok = datetime.now().year

start_data = datetime(biezacy_rok, 3, 1)
end_data = datetime(biezacy_rok, 6, 30)

soboty = []

obecna_data = start_data
while obecna_data <= end_data:
    if obecna_data.weekday() == 5:
        soboty.append(obecna_data.strftime('%Y-%m-%d'))
    obecna_data += timedelta(days=1)

print("zadanie 7: soboty to:", soboty)
#8
biezacy_rok = datetime.now().year
print("zadanie 8:")
for miesiac in range(1, 13, 2):
    if miesiac == 12:
        nastepny_miesiac = 1
        nastepny_rok = biezacy_rok + 1
    else:
        nastepny_miesiac = miesiac + 1
        nastepny_rok = biezacy_rok

    ostatni_dzien = datetime(nastepny_rok, nastepny_miesiac, 1) - timedelta(days=1)

    while ostatni_dzien.weekday() != 6:
        ostatni_dzien -= timedelta(days=1)

    print(f" otatnia niedziela w {ostatni_dzien.strftime('%B')}: {ostatni_dzien.strftime('%Y-%m-%d')}")
#9
def roznica_w_sekundach(data_poczatkowa, data_koncowa):
    roznica = data_koncowa - data_poczatkowa
    return roznica.total_seconds()

data_poczatkowa = datetime(2023, 1, 20, 1, 0, 0)
data_koncowa = datetime(2023, 1, 23, 12, 33, 5)

roznica = roznica_w_sekundach(data_poczatkowa, data_koncowa)
print(f"zadanie 9: różnica w sekundach wynosi: {int(roznica)} sekund")

#10
start_rok = 2023
end_rok = 2024
print(f"zadanie 10")
for rok in range(start_rok, end_rok + 1):
    for miesiac in range(1, 13):
        data = datetime(rok, miesiac, 1)
        if data.weekday() == 0:  # 0 to poniedziałek
            print(f" poniedziałek jako pierwszy dzień miesiąca: {data.strftime('%Y-%m-%d')}")