import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
import branca.colormap as cm
from streamlit_folium import st_folium
import pickle
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import plotly.express as px
import seaborn as sns


st.title("📊 Gurugram Real Estate Analysis")

df = pd.read_csv(
    "data/gurugram_properties_missing_value_imputation.csv"
)

gdf = gpd.read_file(
    "data/gurugram_sectors.geojson"
)

sector_avg = (
    df.groupby("sector")
    .agg(
        price_per_sqft=("price_per_sqft", "mean"),
        property_count=("price_per_sqft", "count")
    )
    .reset_index()
)

sector_avg["sector_match"] = (
    sector_avg["sector"]
    .str.replace("sector ", "", regex=False)
    .str.lower()
    .str.replace(" ", "", regex=False)
)

gdf["sector_match"] = (
    gdf["Name"]
    .astype(str)
    .str.lower()
    .str.replace(" ", "", regex=False)
)

merged = sector_avg.merge(
    gdf[["sector_match", "Name", "geometry"]],
    on="sector_match",
    how="left"
)

merged = gpd.GeoDataFrame(
    merged,
    geometry="geometry",
    crs=gdf.crs
)

map_data = merged[
    merged.geometry.notna()
].copy()

map_data = map_data.to_crs(epsg=4326)

min_price = map_data["price_per_sqft"].min()
max_price = map_data["price_per_sqft"].max()

colormap = cm.LinearColormap(
    colors=["green", "yellow", "orange", "red"],
    vmin=min_price,
    vmax=max_price
)

colormap.caption = "Average Price per Sq.Ft. (₹)"

m = folium.Map(
    location=[28.4595, 77.0266],
    zoom_start=12,
    tiles="CartoDB positron"
)

def style_function(feature):

    price = feature["properties"]["price_per_sqft"]

    return {
        "fillColor": colormap(price),
        "color": "black",
        "weight": 1,
        "fillOpacity": 0.7
    }

tooltip = folium.GeoJsonTooltip(
    fields=[
        "sector",
        "price_per_sqft",
        "property_count"
    ],
    aliases=[
        "Sector:",
        "Average Price (₹/sq.ft.):",
        "Properties:"
    ],
    localize=True,
    sticky=False,
    labels=True
)

folium.GeoJson(
    map_data.to_json(),
    style_function=style_function,
    tooltip=tooltip,
    highlight_function=lambda feature: {
        "weight": 3,
        "color": "blue",
        "fillOpacity": 0.85
    }
).add_to(m)



colormap.add_to(m)

st_folium(
    m,
    width=None,
    height=680
)

st.header('Features wordcloud')

with open("models/feature_text.pkl", "rb") as file:
    feature_text = pickle.load(file)

plt.rcParams["font.family"] = "Arial"

wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

fig, ax = plt.subplots(figsize = (8, 8), facecolor = None)
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad = 0)
st.pyplot(fig)

st.header('Sample Suburst Chart')
df1 = pd.read_csv('data/gurugram_properties_missing_value_imputation.csv')
fig = px.sunburst(
    df1,
    path=['property_type', 'bedRoom'],
    values='price_per_sqft',
    color_discrete_sequence = px.colors.qualitative.Pastel,
    width=600,
    height=600
)
st.plotly_chart(fig)

st.header('Area Vs Price ')
fig = px.scatter(df, x="built_up_area", y="price", color="bedRoom", height=700)
# Show the plot
st.plotly_chart(fig)

st.header('bedrooms wise bill')
fig =px.pie(df,names='bedRoom')
st.plotly_chart(fig)

import plotly.io as pio
pio.templates.default = "plotly"

st.header('BHK Price Range')
temp_df = df[df['bedRoom'] <= 4]
# Create side-by-side boxplots of the total bill amounts by day
fig = px.box(temp_df, x='bedRoom', y='price')

# Show the plot
st.plotly_chart(fig)

st.header('Price Distribution')
fig, ax = plt.subplots()

sns.histplot(df[df['property_type'] == 'house']['price'], kde=True, label='House', ax=ax)
sns.histplot(df[df['property_type'] == 'flat']['price'], kde=True, label='Flat', ax=ax)

ax.legend()
ax.set_title("Price Distribution: House vs Flat")

st.pyplot(fig)