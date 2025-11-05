import streamlit as st
import pandas as pd
from lab3_logic import calculate_fare_by_sex

st.title("🎟️ Анализ стоимости билетов пассажиров Титаника")

@st.cache_data
def load_data():
    return pd.read_csv("titanic_train.csv")

df = load_data()

st.write("### Первые строки данных:")
st.dataframe(df.head())

st.sidebar.header("⚙️ Настройки анализа")

func_option = st.sidebar.selectbox("Выберите функцию:", ["min", "max", "avg"])

if st.sidebar.button("Рассчитать"):
    result = calculate_fare_by_sex(df, func_option)

    st.subheader(f"Результаты ({func_option.upper()} цена билета)")
    st.table(result)
    st.bar_chart(result)
else:
    st.info("Выберите функцию и нажмите **Рассчитать**.")

st.markdown("""
---
**Описание:**
- `Sex` — пол пассажира (male/female)  
- `Fare` — стоимость билета  
- Можно выбрать одну из функций: **min**, **max** или **avg**
""")
