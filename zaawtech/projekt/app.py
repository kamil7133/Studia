import pandas as pd
import streamlit as st
import plotly.express as px
from functions.ladowanie_i_normalizacja import ladowanie_i_normalizacja
from functions.geen_i_iter import MonthIterator, stats_generator

st.set_page_config(page_title="Expense Dashboard", layout="wide")

@st.cache_data
def load_data():
    return ladowanie_i_normalizacja(filepath= 'data/Historia_transakcji_projekt.csv')

df = load_data()

currency = df['waluta_transakcji'].iloc[0] if 'waluta_transakcji' in df.columns else "???"

st.title("Dashboard Wydatków")

# a) Wykres słupkowy wydatków całkowitych według kategorii
st.header("Wykres słupkowy wydatków całkowitych według kategorii")
df_cat = df.groupby('kategoria')['obciazenia'].sum().reset_index().sort_values('obciazenia', ascending=False)

fig_a = px.bar(df_cat, x='kategoria', y='obciazenia',
               title=f"Całkowite wydatki ({currency})",
               labels={'obciazenia': f'Suma ({currency})', 'kategoria': 'Kategoria'},
               color='kategoria')
st.plotly_chart(fig_a, use_container_width=True)

# Layout
col1, col2 = st.columns(2)

with col1:
    # b) Wykres liniowy wydatków w czasie dla trzech wybranych kategorii
    st.header("Wykres liniowy wydatków w czasie dla trzech wybranych kategorii)")
    top_3_cats = df.groupby('kategoria')['obciazenia'].sum().nlargest(3).index.tolist()
    df_top = df[df['kategoria'].isin(top_3_cats)]

    df_line = (df_top.set_index('data_transakcji')
               .groupby('kategoria')
               .resample('M')['obciazenia'].sum()
               .reset_index())

    fig_b = px.line(df_line, x='data_transakcji', y='obciazenia', color='kategoria',
                    title=f"Dynamika wydatków ({currency})",
                    labels={'obciazenia': f'Kwota ({currency})', 'data_transakcji': 'Miesiąc'},
                    markers=True)
    st.plotly_chart(fig_b, use_container_width=True)

with col2:
    # c) Grupowany wykres słupkowy dla kategorii złożonej
    st.header("Grupowany wykres słupkowy dla kategorii złożonej (marka)")
    selected_cat = st.selectbox("Wybierz kategorię:", df['kategoria'].unique(), index=0)

    df_brands = (df[df['kategoria'] == selected_cat]
                 .groupby('marka')['obciazenia'].sum()
                 .reset_index()
                 .sort_values('obciazenia', ascending=False))

    fig_c = px.bar(df_brands, x='marka', y='obciazenia',
                   title=f"Marki w kategorii: {selected_cat}",
                   labels={'obciazenia': f'Suma ({currency})', 'marka': 'Sklep / Marka'},
                   color_discrete_sequence=['#ef553b'])
    st.plotly_chart(fig_c, use_container_width=True)

st.divider()
total_spent = df['obciazenia'].sum()
st.metric("Całkowite wydatki", f"{total_spent:,.2f} {currency}")

st.divider()
st.header("Etap III")

st.write("""
W tej sekcji dane są przetwarzane przez **własny iterator** (`MonthIterator`), 
a statystyki są wyliczane przez **generator** (`stats_generator`) w sposób strumieniowy.
""")

# Inicjalizacja iteratora
month_iter = MonthIterator(df)

# Użycie generatora do pobrania wyników
monthly_stats = list(stats_generator(month_iter))

# Wyświetlenie w formie tabeli
stats_df = pd.DataFrame(monthly_stats)
st.dataframe(stats_df, use_container_width=True)

if not stats_df.empty:
    best_month = stats_df.loc[stats_df['Suma wydatków'].idxmax()]
    st.info(f"Najwięcej wydałeś w **{best_month['Miesiąc']}** ({best_month['Suma wydatków']} {currency})")