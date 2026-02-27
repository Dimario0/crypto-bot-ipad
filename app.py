import streamlit as st
import ccxt
import pandas as pd

# Настройки страницы для iPad
st.set_page_config(page_title="Crypto Bot Dashboard", layout="wide")
st.title("🤖 Панель управления ботом: DOGE & TON")

# Подключаемся к бирже для получения рыночных данных (пока без ключей)
exchange = ccxt.bybit()

def get_crypto_data(symbol):
    try:
        ticker = exchange.fetch_ticker(symbol)
        return ticker['last'], ticker['percentage']
    except Exception as e:
        return None, None

# Рисуем две колонки
col1, col2 = st.columns(2)

# Получаем и выводим данные для DOGE
doge_price, doge_change = get_crypto_data('DOGE/USDT')
with col1:
    if doge_price:
        st.metric(label="Цена DOGE/USDT", value=f"${doge_price}", delta=f"{doge_change}% за 24ч")
    else:
        st.error("Не удалось загрузить данные DOGE")

# Получаем и выводим данные для TON
ton_price, ton_change = get_crypto_data('TON/USDT')
with col2:
    if ton_price:
        st.metric(label="Цена TON/USDT", value=f"${ton_price}", delta=f"{ton_change}% за 24ч")
    else:
        st.error("Не удалось загрузить данные TON")

st.divider()

# Блок настроек
st.subheader("⚙️ Настройки стратегии")
trade_amount = st.slider("Сумма одной сделки (USDT)", min_value=10, max_value=1000, value=50)
st.write(f"Бот будет покупать монеты на **{trade_amount} USDT** за одну сделку.")

if st.button("🚀 Запустить бота (Тестовый режим)"):
    st.success("Интерфейс работает отлично! Логика торговли будет добавлена позже.")
