import pandas as pd
from datetime import datetime

class DataImputation:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def mode_imputation(self, column: pd.Series) -> pd.Series:
        mode = column.mode()[0]
        return column.fillna(mode)

    def mean_imputation(self, column: pd.Series) -> pd.Series:
        mean = column.mean()
        return column.fillna(mean)

    def median_imputation(self, column: pd.Series) -> pd.Series:
        median = column.median()
        return column.fillna(median)


class DateVariable:
    def __init__(self, date_series: pd.Series):
        self.date_series = pd.to_datetime(date_series)

    def encode_as_number(self) -> pd.DataFrame:
        return pd.DataFrame({
            'year': self.date_series.dt.year,
            'month': self.date_series.dt.month,
            'day': self.date_series.dt.day,
            'dayofweek': self.date_series.dt.dayofweek
        })
