import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(page_title="Viz Demo")

# property_type	sector	built_up_area	bedRoom	bathroom	balcony	agePossession	Servant Room	furnishing_type	luxury_category	floor_category

with open("models/df.pkl", "rb") as file:
    df = pickle.load(file)

with open("models/pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)

st.dataframe(df)

st.header('Enter your inputs')

# property_type
property_type = st.selectbox('Property Type',['flat','house'])

# sector
sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))

area = float(st.number_input('Built up Area'))

bedrooms =float(st.selectbox('Number of Bedrooms', sorted(df['bedRoom'].unique().tolist())))

bathroom = float(st.selectbox('Bathrooms', sorted(df['bathroom'].unique().tolist())))

balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))

property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))

servant_room = float(st.selectbox('Servant Room', [0.0,1.0]))

furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))

luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))

floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):

    #form a data frame
    data = [[ property_type, sector, area, bedrooms, bathroom, balcony, property_age, servant_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'built_up_area', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'Servant Room',
               'furnishing_type', 'luxury_category', 'floor_category']

    one_df = pd.DataFrame(data, columns=columns)

    # st.dataframe(one_df)

    # Predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price *0.95
    high = base_price *1.05

    st.text("The price of the flat is between {}Cr and {}Cr".format(round(low,2), round(high,2)))