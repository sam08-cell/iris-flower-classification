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
except Exception as e:
    pass

from assets.style import get_custom_css
from models.ml_engine import load_data, clean_data

# Views
from authentication.auth_views import render_auth_page, render_user_profile_sidebar
from pages.landing_view import render_landing_page
from pages.dataset_overview_view import render_dataset_overview
from pages.data_cleaning_view import render_data_cleaning
from pages.eda_view import render_eda
from pages.feature_selection_view import render_feature_selection
from pages.model_training_view import render_model_training
from pages.model_comparison_view import render_model_comparison
from pages.hyperparameter_tuning_view import render_hyperparameter_tuning
from pages.confusion_matrix_view import render_confusion_matrix_view
from pages.prediction_view import render_prediction_page
from pages.reports_view import render_reports_page
from pages.about_view import render_about_project

# ----------------- SESSION STATE MANAGEMENT -----------------
if 'logged_in' not in st.session_state:
    # Set default guest session so users can immediately explore all modules without getting blocked
    st.session_state['logged_in'] = True
    st.session_state['user'] = {
        "id": 1,
        "fullname": "Guest Analyst",
        "email": "analyst@iris.ai",
        "role": "Practitioner"
    }

if 'dark_mode' not in st.session_state:
    st.session_state['dark_mode'] = False

if 'selected_menu' not in st.session_state:
    st.session_state['selected_menu'] = "🏠 Home"

# Load Dataset Cache
@st.cache_data
def get_cached_dataset():
    df_raw = load_data()
    df_clean, _ = clean_data(df_raw)
    return df_raw, df_clean

df_raw, df_clean = get_cached_dataset()

# ----------------- THEME & CSS INJECTION -----------------
st.markdown(get_custom_css(dark_mode=st.session_state['dark_mode']), unsafe_allow_html=True)

# ----------------- SIDEBAR CONTROLS -----------------
st.sidebar.markdown("""
    <div style="padding: 10px 0 15px 0;">
        <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; color: #6366f1; font-weight: 700;">Machine Learning Platform</div>
        <h2 style="margin: 2px 0 0 0; font-size: 1.3rem; font-weight: 800; color: #1e1b4b;">Iris AI Studio</h2>
    </div>
""", unsafe_allow_html=True)

# Theme Toggle
side_col1, side_col2 = st.sidebar.columns([2, 1.2])
with side_col1:
    user_name = st.session_state.get('user', {}).get('fullname', 'Analyst')
    st.caption(f"👤 {user_name}")
with side_col2:
    mode_label = "🌙 Dark" if not st.session_state['dark_mode'] else "☀️ Light"
    if st.button(mode_label, key="theme_toggle_btn", help="Toggle Dark/Light Mode"):
        st.session_state['dark_mode'] = not st.session_state['dark_mode']
        st.rerun()

st.sidebar.markdown("<hr style='margin: 10px 0 18px 0;'>", unsafe_allow_html=True)

menu_items = [
    "🏠 Home",
    "📋 Dataset Overview",
    "🧹 Data Cleaning",
    "📊 Data Analysis (EDA)",
    "🎯 Feature Selection",
    "⚙️ Model Training",
    "📈 Model Comparison",
    "🎛️ Hyperparameter Tuning",
    "🔍 Confusion Matrix",
    "🔮 Prediction",
    "📑 Reports",
    "🔐 Account & Security",
    "ℹ️ About Project"
]

# Ensure valid index
current_index = 0
if st.session_state['selected_menu'] in menu_items:
    current_index = menu_items.index(st.session_state['selected_menu'])

chosen_menu = st.sidebar.radio("Navigation Menu", menu_items, index=current_index)
st.session_state['selected_menu'] = chosen_menu

# Quick System Information in Sidebar Footer
st.sidebar.markdown("""
    <hr style='margin: 20px 0 12px 0;'>
    <div style='font-size: 0.78rem; color: #64748b; line-height: 1.6;'>
        <b>Models:</b> KNN • Decision Tree • SVM<br/>
        <b>Tuning:</b> 5-Fold GridSearchCV<br/>
        <b>Pipeline:</b> Production v2.0
    </div>
""", unsafe_allow_html=True)

# ----------------- PAGE ROUTING -----------------
if chosen_menu == "🏠 Home":
    render_landing_page()

elif chosen_menu == "📋 Dataset Overview":
    render_dataset_overview(df_raw)

elif chosen_menu == "🧹 Data Cleaning":
    render_data_cleaning(df_raw)

elif chosen_menu == "📊 Data Analysis (EDA)":
    render_eda(df_clean)

elif chosen_menu == "🎯 Feature Selection":
    render_feature_selection(df_clean)

elif chosen_menu == "⚙️ Model Training":
    render_model_training(df_clean)

elif chosen_menu == "📈 Model Comparison":
    render_model_comparison(df_clean)

elif chosen_menu == "🎛️ Hyperparameter Tuning":
    render_hyperparameter_tuning(df_clean)

elif chosen_menu == "🔍 Confusion Matrix":
    render_confusion_matrix_view(df_clean)

elif chosen_menu == "🔮 Prediction":
    render_prediction_page()

elif chosen_menu == "📑 Reports":
    render_reports_page()

elif chosen_menu == "🔐 Account & Security":
    render_auth_page()

elif chosen_menu == "ℹ️ About Project":
    render_about_project()
