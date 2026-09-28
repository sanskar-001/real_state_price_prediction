import streamlit as st


st.header("Welcome to the Real Estate World...")

st.markdown("""
# 🏡 Real Estate Price Predictor & Visualization

### Predict property prices. Explore market trends.

Welcome to the **Real Estate Price Predictor**, a machine learning web app that estimates property prices based on location, area, bedrooms, bathrooms, property age, and amenities. It also offers interactive visualizations to help you understand what drives housing prices.

## 🔍 Key Features

- **💰 Instant Price Prediction:** Enter property details and get an estimated price in seconds.
- **📊 Interactive Visualizations:** Explore price distributions, location-wise comparisons, and correlation heatmaps.
- **🧠 Model Insights:** View accuracy metrics (R², MAE, RMSE) and feature importance.

## ⚙️ How It Works

The dataset is cleaned, preprocessed, and used to train regression models such as Linear Regression, Random Forest, and XGBoost. The best-performing model is deployed here using **Streamlit** for a fast, interactive experience.

## 🛠️ Built With

Python • Pandas • NumPy • Scikit-learn • Plotly • Streamlit

👈 Use the **sidebar** to start predicting and exploring!

> ⚠️ *Predictions are estimates based on historical data and not a professional property valuation.*
""")