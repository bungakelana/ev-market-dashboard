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
from scripts.logic import get_kpi
from main_page import ml_page
from main_page import aboutme_page
from main_page import home_page

# CONFIG HARUS PALING ATAS
st.set_page_config(
    page_title='EV MARKET 2026',
    layout='wide'
)

# Function convert image ke base64
def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

#MULTIPAGE SETUP
# NAVIGATION
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=[
            "Home",
            "EV Intelligence",
            "About Me"
        ],
        icons=[
            "house",
            "auto_graph",
            "person"
        ],
        menu_icon="cast_connected",
        default_index=0,
    )
   
#HEADER HOME PAGE
if selected == "Home":
    home_page.show()
elif selected == "EV Intelligence":
    ml_page.show()
elif selected == "About Me":
    aboutme_page.show()
