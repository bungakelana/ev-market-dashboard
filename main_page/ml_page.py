import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# LOAD MODEL
rating_xgb = joblib.load("models/rating_xgb.pkl")

# LOAD DATA
df = pd.read_csv("data/ev_market_2026.csv")

# FEATURE TRAINING
X = df[
    [
        'range_miles',
        'battery_capacity_kwh',
        'charging_speed_kw',
        'top_speed_mph',
        'autopilot_level',
        'price_usd',
        'brand',
        'market_segment'
    ]
]
X = pd.get_dummies(X)


# SHOW PAGE
def show():

    # CSS
    st.markdown("""
    <style>

    .card {
        background: rgba(255,255,255,0.25);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.3);
        border-radius: 24px;
        padding: 28px;
        margin-bottom: 25px;
}
/* LABEL */
label {
    font-size: 18px !important;
    font-weight: 600 !important;
    color: #06212E !important;
}

    
    /* INPUT NUMBER */
div[data-baseweb="input"] > div {
    background-color: #06212E !important;
    color: white !important;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.2);
    padding: 12px 18px !important;
    min-height: 60px !important;
}

/* INPUT VALUE */
input {
    color: white !important;
    -webkit-text-fill-color: white !important;
    font-size: 22px !important
    font-weight: 600 !important;
}

/* INPUT TEXT */
input 
    color: white !important;
    font-size: 22px !important;
    font-weight: 600 !important;
}

/* PLACEHOLDER */
input::placeholder {
    color: rgba(255,255,255,0.7) !important;
    -webkit-text-fill-color: rgba(255,255,255,0.7) !important;
}

/* SELECTBOX */
div[data-baseweb="select"] > div {
    background-color: #06212E !important;
    color: white !important;
    border-radius: 16px !important;
    border: 1px solid rgba(255,255,255,0.2);
    min-height: 60px !important;
    font-size: 20px !important;
    padding-left: 10px !important;
}

/* SELECTBOX TEXT */
div[data-baseweb="select"] * {
    color: white !important;
    font-size: 20px !important;
    font-weight: 600 !important;
}

/* BUTTON */
.stButton > button {
    background: linear-gradient(
        135deg,
        #1D4ED8,
        #2563EB
    ) !important;
    color: white !important;
    border: none !important;
    border-radius: 16px !important;
    padding: 14px 28px !important;
    font-size: 20px !important;
    font-weight: 700 !important;
    width: 100%;
    transition: 0.3s ease;
}

/* BUTTON HOVER */
.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(37,99,235,0.35);
}

/* SUCCESS BOX */
.stAlert {
    font-size: 22px !important;
    border-radius: 18px !important;
    padding: 20px !important;
}

/* DROPDOWN TEXT */
div[data-baseweb="select"] * {
    color: white !important;
}


    </style>
    """, unsafe_allow_html=True)

    # TITLE
    st.title("🚀 EV Customer Satisfaction Prediction")
    st.markdown("""
    Predict customer satisfaction based on EV specifications
    using XGBoost Machine Learning.
    """)

    # KPI
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🚀 Model", "XGBoost")
    with col2:
        st.metric("📊 Features", "8")
    with col3:
        st.metric("⭐ Prediction", "Customer Rating")




    # INPUT
    st.subheader("🔮 Predict Customer Rating")
    
    range_miles = st.number_input(
        "Range Miles",
        min_value=0,
        format="%d"
    )

    battery = st.number_input(
        "Battery Capacity",
        min_value=0,
        format="%d"
    )

    charging = st.number_input(
        "Charging Speed",
        min_value=0,
        format="%d"
    )

    top_speed = st.number_input(
        "Top Speed",
        min_value=0,
        format="%d"
    )

    price = st.number_input(
        "Price USD",
        min_value=0,
        format="%d"
    )
    
    autopilot = st.selectbox(
        "Autopilot Level",
        sorted(df["autopilot_level"].unique())
    )

    brand = st.selectbox(
        "Brand",
        sorted(df["brand"].unique())
    )

    segment = st.selectbox(
        "Market Segment",
        sorted(df["market_segment"].unique())
    )

    # BUTTON
    if st.button("Predict Rating"):

        input_df = pd.DataFrame({
            'range_miles': [range_miles],
            'battery_capacity_kwh': [battery],
            'charging_speed_kw': [charging],
            'top_speed_mph': [top_speed],
            'price_usd': [price],
            'autopilot_level': [autopilot],
            'brand': [brand],
            'market_segment': [segment]
        })

        # ENCODING
        input_df = pd.get_dummies(input_df)

        # SAMAKAN KOLOM
        input_df = input_df.reindex(
            columns=X.columns,
            fill_value=0
        )
        # PREDICT
        prediction = rating_xgb.predict(input_df)
        st.success(
            f"⭐ Predicted Rating: {prediction[0]:.2f}"
        )
        