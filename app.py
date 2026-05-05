import streamlit as st
import pandas as pd

# Load data
econ_data = pd.read_csv("economic_data.csv")
news_data = pd.read_csv("news_data.csv")

st.title("📊 Economic Interpreter")

# Select year
year = st.selectbox("Select Year", econ_data["year"])

# Get economic data
row = econ_data[econ_data["year"] == year].iloc[0]

st.subheader("Economic Indicators")
st.write(f"GDP Growth: {row['gdp_growth']}%")
st.write(f"Inflation: {row['inflation']}%")
st.write(f"Unemployment: {row['unemployment']}%")

# Simple retrieval (NO sklearn)
news = news_data[news_data["year"] == year]["news"]

if len(news) > 0:
    news = news.values[0]
else:
    news = "No major event found"

st.subheader("📖 Explanation")

st.write(f"In {year}, the economy was affected by: {news}")

# Graph
st.subheader("📈 Trends")
st.line_chart(econ_data.set_index("year"))
