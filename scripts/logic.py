import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import joblib
import base64


# 1. Load data
df = pd.read_csv("data/ev_market_2026.csv")

# =========================
# KPI METRICS
# =========================
def get_kpi(df):

# AVG PRICE
    avg_price = (
        df.groupby("brand")["price_usd"]
        .mean()
        .sort_values()
    )

# AVG RANGE
    avg_range = (
        df["range_miles"]
        .mean()
    )

# TOP BRAND
    top_brand = (
        df["brand"]
        .value_counts()
        .head()
    )

# TOP MODEL
    top_model = (
        df["model"]
        .value_counts()
        .reset_index())
    top_model.columns = [
        "model",
        "total_sales"]

# TOP RATING
    top_rating = (
        df.sort_values(
            "customer_rating",
            ascending=False)[
            ["brand", "model","customer_rating"
            ]]
        .head()
    )

# TOP AUTOPILOT
    top_autopilot = (
        df.groupby("brand")[["autopilot_level"]]
        .mean()
        .sort_values(
            by="autopilot_level",
            ascending=False)
        .reset_index()
    )

# COUNTRY ORIGIN
    country_origin = (
        df["country_of_origin"]
        .mode()[0]
    )

# RETURN KPI
    return {
        "avg_price": avg_price,
        "avg_range": avg_range,
        "top_brand": top_brand,
        "top_model": top_model,
        "top_rating": top_rating,
        "top_autopilot": top_autopilot,
        "country_origin": country_origin
    }



# =========================
#CHART STYLES
# =========================
import pandas as pd

#1 TOP BRANDS SALES TREND
def sales_trend(df):
    sales = (
        df.groupby(["year", "brand"]
        )["annual_sales_units"].sum().reset_index())
    top_brands = (
        df.groupby("brand")["annual_sales_units"]
        .sum()
        .nlargest(5)
        .index
    )
# Filter sales data for top 5 brands
    filtered_sales = (
        sales[
            sales["brand"].isin(top_brands)
        ]
    )
    return filtered_sales


#2 MARKET SEGMENT vs PRICE
def market_segment(df):
     return df[["market_segment", "price_usd"]]
   
#3 PRICE DISTRIBUTION
def price_distribution(df):
    return df[["price_usd"]]
   
#4 TOP VALUE BRANDS
def top_value_brands(df):
    df["value_score"] = (
        df["range_miles"] /
        df["price_usd"]
    )
    top_value = (
        df.sort_values(
            by="value_score",
            ascending=False).head(10))
    return top_value[
        [
            "brand",
            "model",    
            "price_usd",
            "range_miles",
            "value_score"
        ]
    ]
    
#3 PRICE DISTRIBUTION
def price_distribution(df):
    return df[["price_usd"]]
   
#4 TOP VALUE BRANDS
def top_value_brands(df):
    df["value_score"] = (
        df["range_miles"] /
        df["price_usd"]
    )
    top_value = (
        df.sort_values(
            by="value_score",
            ascending=False).head(10)) 
    return top_value[
        [
            "brand",
            "model",
            "price_usd",
            "range_miles",
            "value_score"
        ]
    ]
      

