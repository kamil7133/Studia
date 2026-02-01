import pandas as pd


class MonthIterator:
    """
    Iterator, który przechodzi przez DataFrame miesiąc po miesiącu.
    Spełnia wymóg: 'Implementacja własnego iteratora MonthIterator opartego o pandas.groupby'
    """

    def __init__(self, df, date_col='data_transakcji'):
        # Grupowanie danych po miesiącu (freq='M' lub 'ME')
        self.grouped = df.sort_values(date_col).groupby(pd.Grouper(key=date_col, freq='M'))
        self.month_keys = list(self.grouped.groups.keys())
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.month_keys):
            raise StopIteration

        month = self.month_keys[self.current_index]
        month_data = self.grouped.get_group(month)
        self.current_index += 1
        return month, month_data


def stats_generator(iterator):
    """
    Generator do obliczeń strumieniowych.
    Spełnia wymóg: 'Zastosowanie generatorów do obliczeń strumieniowych bez struktur pośrednich'
    """
    for month, data in iterator:
        # Obliczamy statystyki "w locie" i wyrzucamy (yield) wynik
        yield {
            "Miesiąc": month.strftime('%Y-%m'),
            "Suma wydatków": round(data['obciazenia'].sum(), 2),
            "Ilość transakcji": len(data),
            "Największy wydatek": data['obciazenia'].max()
        }