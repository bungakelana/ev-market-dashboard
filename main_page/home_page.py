from tkinter import font
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly.graph_objs._figure import Figure
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import joblib
import base64
from scripts.logic import (
    get_kpi,
    sales_trend,
    market_segment,
    price_distribution,
)

#Function convert image ke base64
def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Ambil gambar
img = get_base64("picture/3_back_car.jpg")


def show():
    st.title("Automotive EV Market Dashboard 2026 ⚡")
    st.markdown("""Analyze electric vehicle market trends, sales performance, and EV insights globally.
""")
    
#KPI STYLE
    st.markdown("""
    <style>

    div[data-testid="stMetric"] {
        background: rgba(240,248,255,0.65);
        border: 1px solid rgba(255,255,255,0.5);
        border-radius: 24px;
        padding: 10px;
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        box-shadow: 0 8px 32px rgba(31,38,135,0.18);
    }

    /* HOVER EFFECT */
    div[data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        transition: 0.3s ease;
        box-shadow: 0 12px 40px rgba(31,38,135,0.25);
    }
    
    </style>
    """, unsafe_allow_html=True)

# CSS background
    page_bg = f"""
    <style>

    .stApp {{
        background-image:
        linear-gradient(rgba(240,248,255,0.75),
                        rgba(220,235,255,0.85)),
        url("data:image/jpeg;base64,{img}");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stSidebar"] {{
        background: rgba(255,255,255,0.25);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);

        border-right: 1px solid rgba(255,255,255,0.3);
    }}

    div[data-testid="metric-container"] {{
        background: rgba(255,255,255,0.25);
        border: 1px solid rgba(255,255,255,0.3);
        padding: 15px;
        border-radius: 20px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px rgba(31,38,135,0.15);
    }}
    </style>
    """

    # MAIN CSS background style
    page_bg = f"""
    <style>

    /* MAIN BACKGROUND */
    .stApp {{
        background-image:
        linear-gradient(rgba(240,248,255,0.75),
                        rgba(220,235,255,0.85)),
        url("data:image/jpeg;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* SIDEBAR STYLES */
    [data-testid="stSidebar"] {{
        background: rgba(255,255,255,0.25);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-right: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 8px 32px rgba(31,38,135,0.1);
        
        border-radius: 0 0 0 20px;
        padding: 20px;
    }}

    /* KPI CARD STYLES */
    div[data-testid="metric-container"] {{
        background: rgba(255,255,255,0.18);
        border: 1px solid rgba(255,255,255,0.3);
        padding: 20px;
        border-radius: 20px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px rgba(31,38,135,0.1);
    }}

    /* CHART CONTAINER */
    .chart-card {{
        background: rgba(255,255,255,0.25);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255,255,255,0.3);
        backdrop-filter: blur(12px);
    }}

    div[data-testid="metric-container"] {{
        background: rgba(255,255,255,0.25);
        border: 1px solid rgba(255,255,255,0.3);
        padding: 15px;
        border-radius: 20px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px rgba(31,38,135,0.15);
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

    st.markdown("""
        <style>
        
        div[data-testid="stMetric"] {
            background: rgba(240,248,255,0.65);
            border: 1px solid rgba(255,255,255,0.5);
            border-radius: 24px;
            padding: 10px;
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            box-shadow: 0 8px 32px rgba(31,38,135,0.18);
        }

        /* HOVER EFFECT */
        div[data-testid="stMetric"]:hover {
            transform: translateY(-5px);
            transition: 0.3s ease;
            box-shadow: 0 12px 40px rgba(31,38,135,0.25);
        }
        </style>
        """, unsafe_allow_html=True)


        # LOAD DATA
    df = pd.read_csv("data/ev_market_2026.csv")
    
       
        # FILTER SECTION
    filter_col1 = st.columns([1])[0]

    with filter_col1:
        brand = st.sidebar.selectbox(
        "🚘 Select Brand",
        options=["All"] + sorted(df["brand"].unique().tolist())
            )

        price = st.sidebar.slider(
        "💲 Price Range (USD)",
        int(df["price_usd"].min()),
        int(df["price_usd"].max()),
            (
            int(df["price_usd"].min()),
            int(df["price_usd"].max())
                )
            )

        # =========================
        # FILTER DATA
        # =========================
        filtered_df = df.copy()
        if brand != "All":
            filtered_df = filtered_df[
                filtered_df["brand"] == brand
            ]
        filtered_df = filtered_df[
            (filtered_df["price_usd"] >= price[0]) &
            (filtered_df["price_usd"] <= price[1])
        ]

        # KPI Metrics
        kpi = get_kpi(filtered_df)
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

        with col1:
            #with st.container(border=True):
                st.metric(
                    "Average Price (USD)",
                    f"💲{kpi['avg_price'].mean():.0f}"
                )

        with col2:
            #with st.container(border=True):
                st.metric(
                    "Average Range (Miles)",
                    f"⏱️{kpi['avg_range']:.0f} miles"
                )

        with col3:
            #with st.container(border=True):
                st.metric(
                    "Top Value Brand",
                    f"🏆{kpi['top_brand'].idxmax()}"
                )

        with col4:
            #with st.container(border=True):
                st.metric(
                    "Top Model by Sales",
                    f"🚘{kpi['top_model']['model'].iloc[0]}"
                )

        with col5:
            #with st.container(border=True):
                st.metric(
                    "Top Customer Rating",
                    f"⭐{kpi['top_rating']['customer_rating'].iloc[0]:.1f}"
                )

        with col6:
                st.metric(
                    "Autopilot Leader",
                    f"🤖{kpi['top_autopilot']['autopilot_level'].iloc[0]:.1f}"
                )

        with col7:
            st.metric(
                "Country Origin",
                f"🌍 {kpi['country_origin']}"
            )


        #CHART CARD STYLE
        st.markdown("""
        <style>

        .chart-card{
            background: rgba(15,23,42,0.72);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 24px;
            padding: 18px;
            backdrop-filter: blur(18px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.35);
            transition: 0.3s ease;
        }

        .chart-card:hover{
            transform: translateY(-4px);
            border: 1px solid rgba(0,255,255,0.25);

        }

        </style>
        """, unsafe_allow_html=True)


# GET DATA FROM LOGIC
        sales_df = sales_trend(filtered_df)
        market_df = market_segment(filtered_df)
        price_df = price_distribution(filtered_df)


        # SALES TREND FIGURE
        template="plotly_dark"
        fig = px.line(
            sales_df,
            x="year",
            y="annual_sales_units",
            color="brand",
            template="plotly_dark"
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(
                color='white'
            )
        )

        # =========================
        # TABS
        # =========================

        tab1, tab2 = st.tabs([
            "📊 Market Analytics",
            "🤖 EV Intelligence"
        ])


        # =========================
        # TAB 1
        # =========================

        with tab1:

            # TOP ROW
            col1, col2 = st.columns([2,1])

            # SECOND ROW
            col3, col4 = st.columns(2)

            # =====================
            # SALES TREND
            # =====================
            with col1:
                with st.container(border=True):
                    fig_sales = px.line(
                        sales_df,
                        x="year",
                        y="annual_sales_units",
                        color="brand",
                        title="📈 EV Sales Trend",
                        template="plotly_dark"
                    )
                    fig_sales.update_layout(
                        paper_bgcolor="#06212E",
                        plot_bgcolor="#06212E",
                        font=dict(color='white'),
                        title_font=dict(
                            color='white',
                            size=22
                        ),
                        xaxis=dict(
                            tickfont=dict(color='white'),
                            gridcolor='rgba(255,255,255,0.1)'
                        ),
                        yaxis=dict(
                            tickfont=dict(color='white'),
                            gridcolor='rgba(255,255,255,0.1)'
                        ),
                        legend=dict(
                            font=dict(color='white')
                        )
                    )
                    st.plotly_chart(
                        fig_sales,
                        use_container_width=True
                    )


            # =====================
            # MARKET SEGMENT vs PRICE
            # =====================

            with col2:
                with st.container(border=True):
                    fig_market = px.bar(
                        market_df,
                        x="market_segment",
                        y="price_usd",
                        color="market_segment",
                        title="📊 Market Segment vs Price",
                        template="plotly_dark",
                        color_discrete_sequence=[
                            "#FAFAFA",   # cyan
                            "#818CF8",   # soft purple
                            "#06B6D4",   # teal
                            "#F59E0B"    # orange
                        ]
                    )
                    fig_market.update_layout(
                        paper_bgcolor="#06212E",
                        plot_bgcolor="#06212E",
                        font=dict(color='white'),
                        title_font=dict(
                            color='white',
                            size=22
                        ),
                        legend=dict(
                            font=dict(
                                color='white',
                                size=14
                            ),
                        ),
                    )
                    st.plotly_chart(
                        fig_market,
                        use_container_width=True
                    )


            # =====================
            # PRICE DISTRIBUTION
            # =====================

            with col3:
                with st.container(border=True):
                    fig_price: Figure = px.histogram(
                        price_df,
                            x="price_usd",
                            title="💲 Price Distribution",
                            template="plotly_dark")

            # WARNA HISTOGRAM
                    fig_price.update_traces(
                            marker_color="#97DFFE")

            # LAYOUT
            fig_price.update_layout(
                paper_bgcolor="#06212E",
                plot_bgcolor="#06212E",
                font=dict(
                    color='white'
                ),

                title_font=dict(
                    color='white',
                    size=22
                ),
                xaxis=dict(
                    tickfont=dict(color='white'),
                    gridcolor='rgba(255,255,255,0.1)'
                ),
                yaxis=dict(
                    tickfont=dict(color='white'),
                    gridcolor='rgba(255,255,255,0.1)'
                ),
                legend=dict(
                    font=dict(color='white')
                )
            )

            st.plotly_chart(
                fig_price,
                use_container_width=True
            )



        # =========================
        # TAB 2
        # =========================

        #with tab2:

            #col5, col6 = st.columns(2)


            # =====================
            # TOP VALUE
            # =====================

            #with col5:

            # =====================
            # AUTOPILOT
            # =====================

            #with col6:
                #with st.container(border=True):
                
        st.success("""
        ⚡ EV Market Insight

        Tesla dominates premium EV sales,
        while BYD leads value efficiency growth
        across Asia markets.
        """)