import streamlit as st
import os
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Iris Species AI Classification System",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Database and Environment
from database.db_manager import init_db
try:
    init_db()
except Exception:
    pass

from assets.style import get_custom_css
from models.ml_engine import load_data, clean_data

# Views from src directory
from src.landing_view import render_landing_page
from src.dataset_overview_view import render_dataset_overview
from src.data_cleaning_view import render_data_cleaning
from src.eda_view import render_eda
from src.feature_selection_view import render_feature_selection
from src.model_comparison_view import render_model_comparison
from src.hyperparameter_tuning_view import render_hyperparameter_tuning
from src.prediction_view import render_prediction_page
from src.reports_view import render_reports_page

# ----------------- SESSION STATE MANAGEMENT -----------------
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = True
    st.session_state['user'] = {
        "fullname": "Guest Analyst",
        "email": "analyst@iris.ai",
        "role": "Practitioner"
    }

if 'dark_mode' not in st.session_state:
    st.session_state['dark_mode'] = False

# Load Dataset Cache
@st.cache_data
def get_cached_dataset():
    df_raw = load_data()
    df_clean, _ = clean_data(df_raw)
    return df_raw, df_clean

df_raw, df_clean = get_cached_dataset()

# ----------------- THEME & CSS INJECTION -----------------
st.markdown(get_custom_css(dark_mode=st.session_state['dark_mode']), unsafe_allow_html=True)

# ----------------- SIDEBAR HEADER -----------------
st.sidebar.markdown("""
    <div style="padding: 10px 0 10px 0;">
        <div style="font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; color: #6366f1; font-weight: 700;">Botanical AI Studio</div>
        <h2 style="margin: 2px 0 0 0; font-size: 1.25rem; font-weight: 800;">Iris Platform</h2>
    </div>
""", unsafe_allow_html=True)

# Theme Toggle Button
side_col1, side_col2 = st.sidebar.columns([1.8, 1.2])
with side_col1:
    user_name = st.session_state.get('user', {}).get('fullname', 'Analyst')
    st.caption(f"👤 {user_name}")
with side_col2:
    mode_label = "🌙 Dark" if not st.session_state['dark_mode'] else "☀️ Light"
    if st.button(mode_label, key="theme_toggle_btn", help="Switch between Dark and Light mode"):
        st.session_state['dark_mode'] = not st.session_state['dark_mode']
        st.rerun()

st.sidebar.markdown("<hr style='margin: 8px 0 16px 0;'>", unsafe_allow_html=True)

# Clean, essential streamlined menu tabs
menu_items = [
    "🏠 Overview & Home",
    "📋 Dataset & Cleaning",
    "📊 Exploratory Data Analysis",
    "🎯 Feature Importance",
    "📈 Model Comparison & Tuning",
    "🔮 Real-Time Prediction",
    "📑 Reports & History"
]

# Ensure current navigation state exists before widget instantiation
if 'nav_selection' not in st.session_state:
    st.session_state['nav_selection'] = menu_items[0]

def on_nav_change():
    st.session_state['nav_selection'] = st.session_state['main_nav_radio']

selected_menu = st.sidebar.radio(
    "Navigation Menu",
    menu_items,
    index=menu_items.index(st.session_state['nav_selection']) if st.session_state['nav_selection'] in menu_items else 0,
    key="main_nav_radio",
    on_change=on_nav_change
)

# Sidebar footer
st.sidebar.markdown("""
    <hr style='margin: 24px 0 12px 0;'>
    <div style='font-size: 0.78rem; opacity: 0.7; line-height: 1.6;'>
        <b>Algorithms:</b> KNN, Tree, SVM<br/>
        <b>Tuning:</b> 5-Fold GridSearchCV<br/>
        <b>System:</b> Production v2.0
    </div>
""", unsafe_allow_html=True)

# ----------------- CLEAN PAGE ROUTING -----------------
current_view = st.session_state.get('nav_selection', selected_menu)

if current_view == "🏠 Overview & Home":
    render_landing_page()

elif current_view == "📋 Dataset & Cleaning":
    tab_ds, tab_clean = st.tabs(["📋 Dataset Overview", "🧹 Data Cleaning & Audit"])
    with tab_ds:
        render_dataset_overview(df_raw)
    with tab_clean:
        render_data_cleaning(df_raw)

elif current_view == "📊 Exploratory Data Analysis":
    render_eda(df_clean)

elif current_view == "🎯 Feature Importance":
    render_feature_selection(df_clean)

elif current_view == "📈 Model Comparison & Tuning":
    tab_comp, tab_tune = st.tabs(["📈 Model Comparison Matrix", "🎛️ Hyperparameter Tuning (GridSearchCV)"])
    with tab_comp:
        render_model_comparison(df_clean)
    with tab_tune:
        render_hyperparameter_tuning(df_clean)

elif current_view == "🔮 Real-Time Prediction":
    render_prediction_page()

elif current_view == "📑 Reports & History":
    render_reports_page()
