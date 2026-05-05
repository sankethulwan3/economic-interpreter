import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
econ_data = pd.read_csv("data/economic_data.csv")
news_data = pd.read_csv("data/news_data.csv")

st.title("📊 Economic Interpreter (Mini Project Demo)")

# Select year
year = st.selectbox("Select Year", econ_data["year"])

# Get economic values
row = econ_data[econ_data["year"] == year].iloc[0]

st.subheader("Economic Indicators")
st.write(f"GDP Growth: {row['gdp_growth']}%")
st.write(f"Inflation: {row['inflation']}%")
st.write(f"Unemployment: {row['unemployment']}%")

# --- RAG PART ---

# Convert news into vectors
vectorizer = TfidfVectorizer()
news_vectors = vectorizer.fit_transform(news_data["news"])

# Query
query = f"GDP {row['gdp_growth']} inflation {row['inflation']} unemployment {row['unemployment']}"
query_vec = vectorizer.transform([query])

# Similarity
similarity = cosine_similarity(query_vec, news_vectors)
index = similarity.argmax()

retrieved_news = news_data.iloc[index]["news"]

# Generate explanation
st.subheader("📖 AI Explanation")

explanation = f"""
In {year}, the economy experienced GDP growth of {row['gdp_growth']}%, 
inflation at {row['inflation']}%, and unemployment at {row['unemployment']}%.

This was likely influenced by the following event:

👉 {retrieved_news}

This shows how real-world events impact economic conditions.
"""

st.write(explanation)

# Graph
st.subheader("📈 Trends")

st.line_chart(econ_data.set_index("year"))
