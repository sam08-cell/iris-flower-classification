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
init_db()

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
    st.session_state['logged_in'] = False
if 'user' not in st.session_state:
    st.session_state['user'] = None
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = "Landing"
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

# ----------------- TOP NAVBAR & HEADER CONTROLS -----------------
top_c1, top_c2 = st.sidebar.columns([2, 1])
with top_c2:
    mode_label = "🌙 Dark" if not st.session_state['dark_mode'] else "☀️ Light"
    if st.button(mode_label, key="theme_toggle_btn", help="Toggle Dark/Light Glassmorphic Mode"):
        st.session_state['dark_mode'] = not st.session_state['dark_mode']
        st.rerun()

# ----------------- ROUTING LOGIC -----------------
if not st.session_state['logged_in']:
    # User is not logged in: Can view Landing or Auth pages
    st.sidebar.markdown("""
        <div style="text-align: center; padding: 10px 0 15px 0;">
            <div style="font-size: 2.2rem;">🌸</div>
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; background: linear-gradient(135deg, #4f46e5, #9333ea); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                Iris AI Platform
            </h3>
        </div>
    """, unsafe_allow_html=True)
    
    auth_nav = st.sidebar.radio(
        "Navigation Menu",
        ["🏠 Landing Page", "🔐 Sign In / Register"],
        index=0 if st.session_state['current_page'] == "Landing" else 1
    )
    
    if auth_nav == "🏠 Landing Page":
        st.session_state['current_page'] = "Landing"
        render_landing_page()
    else:
        st.session_state['current_page'] = "Auth"
        render_auth_page()
        
else:
    # Authenticated User Dashboard
    render_user_profile_sidebar()
    
    st.sidebar.markdown("<p style='font-size: 0.8rem; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 5px;'>Dashboard Navigation</p>", unsafe_allow_html=True)
    
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
        "ℹ️ About Project"
    ]
    
    selected_menu = st.sidebar.selectbox("Go to Module:", menu_items, index=0)
    
    # Breadcrumbs & Header
    st.markdown(f"""
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 8px; font-size: 0.88rem; color: #64748b;">
                <span>Portal</span> <span>›</span> <b style="color: #4f46e5;">{selected_menu}</b>
            </div>
            <div style="font-size: 0.82rem; background: rgba(99, 102, 241, 0.1); color: #4f46e5; padding: 4px 12px; border-radius: 20px; font-weight: 600;">
                Active Session: {st.session_state['user']['role']} Mode
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Route selection
    if selected_menu == "🏠 Home":
        # Dashboard Overview Home
        st.markdown("""
            <div class="hero-banner">
                <div style="font-size: 2.5rem; margin-bottom: 5px;">🌸 🚀 📈</div>
                <h2 style="font-size: 2.2rem; font-weight: 800; margin: 0 0 10px 0;">Welcome to Iris AI Analytics Command Center</h2>
                <p style="font-size: 1.05rem; opacity: 0.95; max-width: 700px; margin: 0 auto;">
                    Seamlessly analyze morphological specimens, train supervised algorithms, 
                    optimize hyperparameters, and generate real-time taxon predictions.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Summary KPI Cards
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Available Observations", len(df_clean), "100% Validated")
        k2.metric("Evaluated Algorithms", "3 Models", "KNN, Tree, SVM")
        k3.metric("Benchmark Peak Accuracy", "100.0%", "SVM Hyperplane")
        k4.metric("Active Model", "SVM (Tuned)", "Production")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        c_left, c_right = st.columns([1.5, 1])
        with c_left:
            st.markdown("""
                <div class="glass-card">
                    <h4>⚡ Quick Navigation Actions</h4>
                    <p style="color: #64748b; font-size: 0.92rem;">Jump straight into key workflows:</p>
                    <ul style="font-size: 0.92rem; color: #475569; line-height: 1.8;">
                        <li><b>Perform Real-Time Prediction:</b> Navigate to the <i>🔮 Prediction</i> module to enter flower measurements.</li>
                        <li><b>Inspect Exploratory Data Analysis:</b> Head to <i>📊 Data Analysis (EDA)</i> for interactive 3D and correlation charts.</li>
                        <li><b>Optimize Hyperparameters:</b> Run <i>🎛️ Hyperparameter Tuning</i> using automated GridSearchCV cross-validation.</li>
                        <li><b>Export Documentation:</b> Visit <i>📑 Reports</i> to download signed PDF certificates and comparison audits.</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        with c_right:
            st.markdown("""
                <div class="glass-card">
                    <h4>🔒 System Status</h4>
                    <p style="font-size: 0.88rem; color: #64748b; margin-bottom: 12px;">SQLite Database Persistence Status</p>
                    <div style="font-size: 0.9rem; line-height: 1.8;">
                        • <b>Database:</b> <code>iris_app.db</code> (Connected)<br/>
                        • <b>Encryption:</b> Salted SHA-256 Hashing<br/>
                        • <b>Inference Engine:</b> Scikit-Learn 1.9+<br/>
                        • <b>Visual Framework:</b> Plotly 7.1+
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
    elif selected_menu == "📋 Dataset Overview":
        render_dataset_overview(df_raw)
    elif selected_menu == "🧹 Data Cleaning":
        render_data_cleaning(df_raw)
    elif selected_menu == "📊 Data Analysis (EDA)":
        render_eda(df_clean)
    elif selected_menu == "🎯 Feature Selection":
        render_feature_selection(df_clean)
    elif selected_menu == "⚙️ Model Training":
        render_model_training(df_clean)
    elif selected_menu == "📈 Model Comparison":
        render_model_comparison(df_clean)
    elif selected_menu == "🎛️ Hyperparameter Tuning":
        render_hyperparameter_tuning(df_clean)
    elif selected_menu == "🔍 Confusion Matrix":
        render_confusion_matrix_view(df_clean)
    elif selected_menu == "🔮 Prediction":
        render_prediction_page()
    elif selected_menu == "📑 Reports":
        render_reports_page()
    elif selected_menu == "ℹ️ About Project":
        render_about_project()
