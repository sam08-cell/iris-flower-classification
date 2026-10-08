import streamlit as st
import pandas as pd
import plotly.express as px
from models.ml_engine import get_train_test_split, train_default_models

def render_model_training(df: pd.DataFrame):
    """Render Train/Test Split inspection and Multi-Model Training interface."""
    st.markdown("## ⚙️ Model Training & Partitioning")
    st.caption("Stratified 80/20 partitioning and supervised training for KNN, Decision Tree, and Support Vector Machine.")
    
    # Train-Test Split Section
    st.subheader("1️⃣ Train / Test Partitioning Configuration")
    
    col_split, col_stats = st.columns([1, 1.5])
    with col_split:
        test_pct = st.slider("Select Test Data Ratio (%):", min_value=10, max_value=40, value=20, step=5)
        random_seed = st.number_input("Random Seed Generator:", min_value=1, max_value=999, value=42)
        
    X_train, X_test, y_train, y_test = get_train_test_split(df, test_size=test_pct/100.0, random_state=random_seed)
    
    with col_stats:
        s1, s2, s3 = st.columns(3)
        s1.metric("Training Samples", f"{len(X_train)} ({(100-test_pct)}%)")
        s2.metric("Testing Samples", f"{len(X_test)} ({test_pct}%)")
        s3.metric("Total Records", len(df))
        
        # Split distribution bar
        split_df = pd.DataFrame({
            "Partition": ["Training Set (80%)", "Testing Set (20%)"],
            "Count": [len(X_train), len(X_test)]
        })
        fig_split = px.bar(
            split_df, x="Partition", y="Count", color="Partition",
            color_discrete_sequence=['#4f46e5', '#ec4899'],
            height=200
        )
        fig_split.update_layout(margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_split, use_container_width=True)
        
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Model Training Section
    st.subheader("2️⃣ Supervised Algorithms Training")
    st.write("Click below to train baseline versions of all 3 algorithms:")
    
    if st.button("🚀 Train All Baseline Models", type="primary", use_container_width=True):
        with st.spinner("Fitting models on training split and evaluating on testing holdout..."):
            results = train_default_models(X_train, X_test, y_train, y_test)
            st.session_state['default_results'] = results
            st.session_state['test_split_info'] = (X_train, X_test, y_train, y_test)
            st.success("✅ All 3 Machine Learning models successfully trained and evaluated!")
            
    # Load from session or train automatically
    if 'default_results' not in st.session_state:
        st.session_state['default_results'] = train_default_models(X_train, X_test, y_train, y_test)
        st.session_state['test_split_info'] = (X_train, X_test, y_train, y_test)
        
    results = st.session_state['default_results']
    
    # Display cards for each model
    st.markdown("### 🏆 Individual Model Performance Metrics")
    c_knn, c_dt, c_svm = st.columns(3)
    
    with c_knn:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 🔵 K-Nearest Neighbors (KNN)")
        st.caption("Hyperparameters: n_neighbors=5, metric=minkowski")
        knn_res = results["KNN"]
        st.metric("Accuracy", f"{knn_res['accuracy']*100:.2f}%")
        st.metric("Precision (Weighted)", f"{knn_res['precision']*100:.2f}%")
        st.metric("Recall (Weighted)", f"{knn_res['recall']*100:.2f}%")
        st.metric("F1 Score", f"{knn_res['f1_score']*100:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c_dt:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 🟢 Decision Tree")
        st.caption("Hyperparameters: max_depth=3, criterion=gini")
        dt_res = results["Decision Tree"]
        st.metric("Accuracy", f"{dt_res['accuracy']*100:.2f}%")
        st.metric("Precision (Weighted)", f"{dt_res['precision']*100:.2f}%")
        st.metric("Recall (Weighted)", f"{dt_res['recall']*100:.2f}%")
        st.metric("F1 Score", f"{dt_res['f1_score']*100:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c_svm:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 🟣 Support Vector Machine (SVM)")
        st.caption("Hyperparameters: kernel=linear, C=1.0")
        svm_res = results["SVM"]
        st.metric("Accuracy", f"{svm_res['accuracy']*100:.2f}%")
        st.metric("Precision (Weighted)", f"{svm_res['precision']*100:.2f}%")
        st.metric("Recall (Weighted)", f"{svm_res['recall']*100:.2f}%")
        st.metric("F1 Score", f"{svm_res['f1_score']*100:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)
