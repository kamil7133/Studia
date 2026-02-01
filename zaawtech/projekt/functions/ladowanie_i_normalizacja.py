import pandas as pd
import re

COLS_RN = {
    'Numer rachunku/karty': 'id_konta',
    'Data transakcji': 'data_transakcji',
    'Data rozliczenia': 'data_rozliczenia',
    'Rodzaj transakcji': 'rodzaj_transakcji',
    'Na konto/Z konta': 'na_konto_z_konta',
    'Odbiorca/Zleceniodawca': 'odbiorca_zleceniodawca',
    'Opis':'opis_transakcji',
    'Obciążenia':'obciazenia',
    'Uznania':'uznania',
    'Saldo':'saldo_po_transakcji',
    'Waluta': 'waluta_transakcji'
}

TO_DATETIME_COLS = ['data_transakcji', 'data_rozliczenia']

MAPPING_OPIS_COLS = {
    'Spożywcze': r'ZABKA|BIEDRONKA|LIDL|AUCHAN|ALDI|ABC|DINO|LECLERC|DELIKATESY|LEWIATAN|SPAR|SPOLEM|TESCO|PENNY|CARREFOUR|INTERMARCHE|SKLEP',
    'Transport': r'BILETY|URBANCARD|KOLEO|TAXI|UBER|ORLEN|SHELL|BP|STACJA PALIW|RYBA TAXI',
    'Subskrypcje i Media': r'NETFLIX|GOOGLE PLAY|AUDIBLE|WSJ|WALL-ST-JOURNAL|WELT|OPENAI|UDEMY|CANAL\+|EBAY|AXEL SPRINGER',
    'Restauracje/Kawiarnie': r'BAR|RESTAURANT|CATERING|CAFFE|KAWIARNIA|KFC|WOK|PUB|ATC CATERING|FLOW RESTAURANT',
    'Zdrowie/Uroda': r'APTEKA|ROSSMANN|SUPER-PHARM|FARBIO|TELEMEDI|SALON MANIEWSKI|TIBI SALON',
    'Dom i DIY': r'CASTORAMA|BRICOMARCHE|HORNBACH|ME M02',
    'Bankowość i Opłaty': r'OPŁATA|PROWIZJA|URZAD GMINY',
}

def kategoryzacja_i_czyszczenie(desc):
        category = 'Inne'
        brand = desc.split(',')[0]

        for cat, pattern in MAPPING_OPIS_COLS.items():
            if re.search(pattern, desc, re.IGNORECASE):
                category = cat
                match = re.search(pattern, desc, re.IGNORECASE)
                brand = match.group(0).upper()
                break

        return pd.Series([category, brand])

def ladowanie_i_normalizacja(filepath: str) -> pd.DataFrame:
    # Wczytanie danych z pliku CSV
    df = pd.read_csv(filepath_or_buffer='filepath', delimiter=',')

    # Normalizacja
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    df = df.rename(columns=COLS_RN)

    df['obciazenia'] = df['obciazenia'].fillna(0).astype(float).abs()

    for col in TO_DATETIME_COLS:
        df[col] = pd.to_datetime(df[col])

    df[['kategoria', 'marka']] = df['opis_transakcji'].apply(kategoryzacja_i_czyszczenie)

    return df


