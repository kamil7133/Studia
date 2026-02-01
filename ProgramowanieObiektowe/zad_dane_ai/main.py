import glob
import pandas as pd
from data_preparation import CleanDataset
from utils import DataImputation

# Załaduj dane
path = glob.glob('**/*dengue_features_train.csv', recursive=True)[0]
deng_train = pd.read_csv(path)

# Uzupełnianie braków w jednej kolumnie
imputer = DataImputation(deng_train)
deng_train['reanalysis_specific_humidity_g_per_kg'] = imputer.mean_imputation(
    deng_train['reanalysis_specific_humidity_g_per_kg']
)

# Przygotuj cały dataset
clean_data = CleanDataset(data=deng_train, date_col_name='week_start_date')
prepared_data = clean_data.get_data(impute_missing=True)

# Wyświetl kilka pierwszych wierszy
print(prepared_data.head())
