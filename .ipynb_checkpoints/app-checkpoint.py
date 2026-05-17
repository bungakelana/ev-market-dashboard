import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menus
from numpy.random import default_rng as rng


st.title = = 'EV MARKET 2026'
st.set_page_config(
		page_title = 'EV MARKET 2026',
		layout = 'wide',
	)

#data
df = pd.read_csv("ev_market_2026.csv")
df

df = df.rename(columns={
    "brand": "Brand",
    "model": "Model",
    "year": "Year",
    "variant": "Variant",
    "price_usd": "Price (USD)",
    "battery_capacity_kwh": "Battery Capacity (kWh)",
    "range_miles": "Range (Miles)",
    "charging_speed_kw": "Charging Speed (kW)",
    "acceleration_0_60_mph": "0-60 MPH (sec)",
    "top_speed_mph": "Top Speed (MPH)",
    "horsepower": "Horsepower",
    "torque_nm": "Torque (Nm)",
    "drive_type": "Drive Type",
    "seating_capacity": "Seats",
    "body_type": "Body Type",
    "cargo_volume_cubic_ft": "Cargo Volume (ft³)",
    "weight_kg": "Weight (kg)",
    "safety_rating": "Safety Rating",
    "autopilot_level": "Autopilot Level",
    "country_of_origin": "Country",
    "market_segment": "Segment",
    "annual_sales_units": "Annual Sales",
    "customer_rating": "Rating",
    "warranty_years": "Warranty (Years)"
})


# sidebar
with st.sidebar:
	brand = st.selectbox(
   "Brand",
    sorted(df["Brand"].unique()),
    index=None,
    placeholder="Select a Brand"
   )


price = st.slider(
    "Price Range (USD)",
    int(df["Price (USD)"].min()),
    int(df["Price (USD)"].max()),
    (int(df["Price (USD)"].min()), int(df["Price (USD)"].max()))
)

#filter
if brand:
    df = df[df["Brand"] == brand]

df = df[
    (df["Price (USD)"] >= price[0]) &
    (df["Price (USD)"] <= price[1])
]

st.dataframe(df)
