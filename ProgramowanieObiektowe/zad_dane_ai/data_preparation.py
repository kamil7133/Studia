from utils import DateVariable
import pandas as pd

class CategoricalData:
    def __init__(self, path=None, data=None):
        self.data = pd.read_csv(path) if path else data
        self.cat_data = self.data.select_dtypes(include=['object'])

    def encode_data(self, method='one_hot'):
        if method == 'one_hot':
            return pd.get_dummies(self.cat_data)
        else:
            raise ValueError(f"Unknown encoding method: {method}")


class NumericData:
    def __init__(self, path=None, data=None):
        self.data = pd.read_csv(path) if path else data
        self.num_data = self.data.select_dtypes(include=['number'])

    def detect_outliers(self, method='iqr', by_column=False):
        outliers = []
        outliers_by_column = {}

        for col in self.num_data.columns:
            Q1 = self.num_data[col].quantile(0.25)
            Q3 = self.num_data[col].quantile(0.75)
            IQR = Q3 - Q1
            mask = (self.num_data[col] < (Q1 - 1.5 * IQR)) | (self.num_data[col] > (Q3 + 1.5 * IQR))
            col_outliers = self.num_data[mask].index.tolist()
            if by_column:
                outliers_by_column[col] = col_outliers
            outliers.extend(col_outliers)

        return outliers_by_column if by_column else list(set(outliers))


class PreparingDataset(CategoricalData, NumericData):
    def __init__(self, path=None, data=None, date_col_name=None):
        CategoricalData.__init__(self, path=path, data=data)
        NumericData.__init__(self, path=path, data=data)

        if date_col_name is not None:
            self.date_data = self.data[date_col_name]

    def prepare_categoricl_data(self, method='one_hot', impute_missing=False):
        if impute_missing:
            for c in self.cat_data.columns:
                most_common = self.cat_data[c].mode()[0]
                self.cat_data[c] = self.cat_data[c].fillna(most_common)

        return self.encode_data(method=method)

    def prepare_numeric_data(self, method='iqr', remove_outliers=False, impute_missing=False):
        outliers = self.detect_outliers(method)
        outliers_by_column = self.detect_outliers(method, by_column=True)

        if impute_missing:
            for c in self.num_data.columns:
                if c in outliers_by_column:
                    median = self.num_data[c].median()
                    self.num_data[c] = self.num_data[c].fillna(median)
                else:
                    mean = self.num_data[c].mean()
                    self.num_data[c] = self.num_data[c].fillna(mean)

        if remove_outliers:
            indices_keep = [i for i in self.num_data.index if i not in outliers]
            self.num_data = self.num_data.loc[indices_keep]

        return self.num_data

    def prepare_date_data(self):
        return DateVariable(self.date_data).encode_as_number()


class CleanDataset(PreparingDataset):
    def __init__(self, path=None, data=None, date_col_name=None):
        super().__init__(path=path, data=data, date_col_name=date_col_name)
        self.date_col_name = date_col_name

    def get_data(self, encoding_method='one_hot', outlier_method='iqr', remove_outliers=True, impute_missing=False):
        categorical = self.prepare_categoricl_data(method=encoding_method, impute_missing=impute_missing)
        numeric = self.prepare_numeric_data(method=outlier_method, remove_outliers=remove_outliers, impute_missing=impute_missing)

        data_parts = [categorical, numeric]

        if self.date_col_name is not None:
            date_calendar = self.prepare_date_data()
            data_parts.append(date_calendar)

        return pd.concat(data_parts, axis=1)
