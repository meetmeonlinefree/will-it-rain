import streamlit as st
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="Will It Rain On My Parade?", page_icon="🌦️")

# Заголовок
st.title("🌦️ Will It Rain On My Parade?")
st.markdown("Прототип приложения для анализа вероятности плохой погоды с использованием данных NASA 🌍")

# Ввод даты
date = st.date_input("📅 Выберите дату:", datetime.date.today())

# Карта
st.subheader("📍 Выберите место на карте")
m = folium.Map(location=[40.7128, -74.0060], zoom_start=3)  # карта центрирована на США
map_data = st_folium(m, width=700, height=400)

# Получаем координаты клика
if map_data["last_clicked"] is not None:
    lat, lon = map_data["last_clicked"]["lat"], map_data["last_clicked"]["lng"]
    st.write(f"Вы выбрали точку: **{lat:.2f}, {lon:.2f}**")
else:
    lat, lon = 40.71, -74.00
    st.write("Кликните на карту, чтобы выбрать точку")

# Фейковые данные (заменить на NASA в будущем)
np.random.seed(42)
fake_data = {
    "Погода": ["🌧️ Дождь", "☀️ Жара", "❄️ Холод", "💨 Ветер", "💧 Влажность"],
    "Вероятность (%)": np.random.randint(10, 90, 5)
}
df = pd.DataFrame(fake_data)

# Вывод
st.subheader(f"📍 Координаты: {lat:.2f}, {lon:.2f}, 📅 Дата: {date}")
st.dataframe(df)

# График
fig, ax = plt.subplots()
ax.bar(df["Погода"], df["Вероятность (%)"], color="skyblue")
ax.set_ylabel("Вероятность (%)")
ax.set_title("Прогноз вероятности погодных условий")
st.pyplot(fig)

# Заключение
st.markdown("✅ В реальном приложении сюда будут подключены NASA Earthdata 🌍 для анализа по координатам и дате.")

# Скачать CSV
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Скачать результаты (CSV)", csv, "weather_probabilities.csv", "text/csv")
