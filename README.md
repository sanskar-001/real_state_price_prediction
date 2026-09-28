# 🏠 Gurugram Real Estate Analytics & Recommendation System

An end-to-end Data Science and Machine Learning application for analyzing the Gurugram real estate market, predicting property prices, performing interactive market analysis, and recommending suitable apartments based on user preferences.

The project combines data cleaning, exploratory data analysis, feature engineering, machine learning, similarity-based recommendation, geographic analysis, and an interactive Streamlit dashboard.

---

## 🚀 Features

### 💰 1. Property Price Prediction

Predict the estimated price of a property based on different property characteristics such as:

- Property Type
- Sector
- Built-up Area
- Number of Bedrooms
- Number of Bathrooms
- Balcony
- Property Age
- Other relevant property features

The prediction module uses a trained machine learning pipeline with preprocessing and prediction steps.

---

### 📊 2. Real Estate Market Analysis

Explore Gurugram's real estate market through interactive visualizations and statistical analysis.

The analysis module includes:

- Property price distribution
- Sector-wise price analysis
- Property type analysis
- Area vs. price analysis
- Bedroom-wise analysis
- Bathroom-wise analysis
- Correlation analysis
- Outlier analysis
- Market trends
- Geographic sector analysis

---

### 🏢 3. Apartment Recommendation System

The recommendation system helps users discover apartments based on property characteristics and user preferences.

The system uses:

- Property similarity
- Feature-based similarity
- Location-related information
- Pre-computed similarity matrices
- Processed property data

to generate relevant apartment recommendations.

---

### 🗺️ 4. Geographic Analysis

The project uses Gurugram sector-level geographic data to analyze property prices across different sectors.

The geographic analysis is supported by:

- Gurugram sector boundaries
- Sector-wise property prices
- GeoJSON data
- Interactive visualizations

---

### 🖥️ 5. Interactive Streamlit Dashboard

The complete application is implemented using Streamlit.

The application provides separate pages for:

- Price Prediction
- Real Estate Analysis
- Apartment Recommendation

---

# 🧠 Project Workflow

```text
                 Raw Real Estate Data
                         │
                         ▼
                Data Cleaning
                         │
                         ▼
             Missing Value Treatment
                         │
                         ▼
                Outlier Treatment
                         │
                         ▼
             Exploratory Data Analysis
                         │
                         ▼
               Feature Engineering
                         │
                         ▼
                Feature Selection
                         │
                         ▼
                 Model Selection
                         │
                         ▼
              Machine Learning Model
                         │
                         ▼
             Saved Model / Pipelines
                         │
                         ▼
          Similarity & Recommendation
                         │
                         ▼
             Streamlit Application
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
       Price Prediction  Analysis  Recommendation

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Data Science & Machine Learning

- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

## Web Application

- Streamlit

## Data Formats

- CSV
- GeoJSON
- Pickle

## Development Tools

- PyCharm
- Jupyter Notebook
- Git
- GitHub
- Git LFS

---

# 📁 Project Structure

```text
gurugram-real-estate/
│
├── README.md
├── .gitignore
├── .gitattributes
│
├── home.py
│
├── data/
│   ├── gurugram_properties_missing_value_imputation.csv
│   └── gurugram_sectors.geojson
│
├── models/
│   ├── cosine_sim1.pkl
│   ├── cosine_sim2.pkl
│   ├── cosine_sim3.pkl
│   ├── df.pkl
│   ├── feature_text.pkl
│   ├── location_distance.pkl
│   └── pipeline.pkl
│
└── pages/
    ├── 1_Price_predictor.py
    ├── 2_Analysis_App.py
    └── 3_Recommend_Apartments.py

🎯 Project Objective

The objective of this project is to develop a practical real estate intelligence platform for Gurugram.

The system helps users:

- Estimate property prices
- Explore the Gurugram real estate market
- Analyze sector-level price patterns
- Understand property characteristics
- Compare property options
- Discover suitable apartments


🔮 Future Improvements
- Real-time real estate data collection
- Automated web scraping
- Advanced machine learning models
- Interactive map-based property search
- Personalized recommendations
- Property comparison dashboard
- Automated model retraining
- Real-time market analysis
- Cloud deployment
- Database integration

⭐ Project Highlights

This project demonstrates practical experience in:

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning
- Recommendation Systems
- Data Visualization
- Streamlit Development
- Git & GitHub

📜 License

This project is developed for educational and portfolio purposes.
