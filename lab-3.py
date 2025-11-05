import streamlit as st
import pandas as pd

st.title("🎟️ Анализ стоимости билетов пассажиров Титаника")

@st.cache_data
def load_data():
    df = pd.read_csv("titanic_train.csv")
    return df

df = load_data()

st.dataframe(df.head())

st.sidebar.header("⚙️ Настройки анализа")

func_option = st.sidebar.selectbox(
    "Выберите функцию:",
    ["min", "max", "avg"]
)

if st.sidebar.button("Рассчитать"):
    st.subheader(f"Результаты ({func_option.upper()} цена билета)")

    result = df.groupby("Sex")["Fare"].agg(
        min="min", max="max", avg="mean"
    )[func_option].round(2)

    st.table(result)

    st.bar_chart(result)

else:
    st.info("Выберите функцию и нажмите **Рассчитать**.")

st.markdown("""
---
**Описание:**
- `Sex` — пол пассажира (male/female)  
- `Fare` — стоимость билета  
- Вы можете выбрать одну из функций: **min**, **max** или **avg**  
- Результаты отображаются в таблице и на графике
""")
