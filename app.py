import streamlit as st
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

st.set_page_config(page_title="Will It Rain On My Parade?", page_icon="🌦️")

# Заголовок
st.title("🌦️ Will It Rain On My Parade?")
st.markdown("Прототип приложения для анализа вероятности плохой погоды с использованием данных NASA 🌍")

# Ввод пользователя
city = st.text_input("Введите город или место:", "New York")
date = st.date_input("Выберите дату:", datetime.date.today())

# Фейковые данные (в реальном проекте заменить на данные NASA)
np.random.seed(42)
fake_data = {
    "Погода": ["🌧️ Дождь", "☀️ Жара", "❄️ Холод", "💨 Ветер", "💧 Влажность"],
    "Вероятность (%)": np.random.randint(10, 90, 5)
}
df = pd.DataFrame(fake_data)

# Вывод
st.subheader(f"📍 Локация: {city}, 📅 Дата: {date}")
st.dataframe(df)

# График
fig, ax = plt.subplots()
ax.bar(df["Погода"], df["Вероятность (%)"], color="skyblue")
ax.set_ylabel("Вероятность (%)")
ax.set_title("Прогноз вероятности погодных условий")
st.pyplot(fig)

# Заключение
st.markdown("✅ Данные выше основаны на **исторических наблюдениях**. "
            "В реальном приложении сюда будут подключены NASA Earthdata 🌍")

# Кнопка скачать
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Скачать результаты (CSV)", csv, "weather_probabilities.csv", "text/csv")
