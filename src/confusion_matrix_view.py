import streamlit as st
import pandas as pd
import plotly.express as px
from models.ml_engine import get_train_test_split, train_default_models

def render_confusion_matrix_view(df: pd.DataFrame):
    """Render Confusion Matrix Heatmaps and Classification Reports for all models."""
    st.markdown("## 🔍 Confusion Matrix & Classification Diagnostics")
    st.caption("Deep error auditing, true vs predicted distributions, and precision-recall trade-offs across all classes.")
    
    if 'default_results' not in st.session_state:
        X_train, X_test, y_train, y_test = get_train_test_split(df)
        st.session_state['default_results'] = train_default_models(X_train, X_test, y_train, y_test)
        
    results = st.session_state['default_results']
    
    model_choice = st.selectbox("Select Model Architecture to Inspect:", ["KNN", "Decision Tree", "SVM"])
    res = results[model_choice]
    
    col1, col2 = st.columns([1.2, 1.3])
    
    with col1:
        st.subheader("🔥 Confusion Matrix Heatmap")
        classes = res["classes"]
        cm = res["confusion_matrix"]
        
        # Plotly heatmap
        fig_cm = px.imshow(
            cm,
            x=classes,
            y=classes,
            text_auto=True,
            color_continuous_scale="Purples",
            labels=dict(x="Predicted Class", y="Ground Truth Class", color="Specimens")
        )
        fig_cm.update_layout(height=450)
        st.plotly_chart(fig_cm, use_container_width=True)
        
    with col2:
        st.subheader("📋 Classification Diagnostic Report")
        cr = res["classification_report"]
        
        # Build tabular report
        rep_rows = []
        for class_name in classes:
            if class_name in cr:
                rep_rows.append({
                    "Class": class_name,
                    "Precision": f"{cr[class_name]['precision']*100:.2f}%",
                    "Recall": f"{cr[class_name]['recall']*100:.2f}%",
                    "F1 Score": f"{cr[class_name]['f1-score']*100:.2f}%",
                    "Support": int(cr[class_name]['support'])
                })
                
        st.dataframe(pd.DataFrame(rep_rows), use_container_width=True)
        
        # Overall Summary Metrics
        st.markdown(f"""
            <div class="saas-card" style="margin-top: 15px;">
                <b>Aggregated Performance Indicators:</b><br/>
                • <b>Accuracy:</b> {cr['accuracy']*100:.2f}%<br/>
                • <b>Macro Avg F1:</b> {cr['macro avg']['f1-score']*100:.2f}%<br/>
                • <b>Weighted Avg F1:</b> {cr['weighted avg']['f1-score']*100:.2f}%
            </div>
        """, unsafe_allow_html=True)
        
    # Multi-Model Side by Side Comparison
    with st.expander("👁️ Compare All 3 Confusion Matrices Side-by-Side"):
        cm_col1, cm_col2, cm_col3 = st.columns(3)
        with cm_col1:
            st.markdown("##### 🔵 KNN")
            f1 = px.imshow(results["KNN"]["confusion_matrix"], x=classes, y=classes, text_auto=True, color_continuous_scale="Blues")
            st.plotly_chart(f1, use_container_width=True)
        with cm_col2:
            st.markdown("##### 🟢 Decision Tree")
            f2 = px.imshow(results["Decision Tree"]["confusion_matrix"], x=classes, y=classes, text_auto=True, color_continuous_scale="Greens")
            st.plotly_chart(f2, use_container_width=True)
        with cm_col3:
            st.markdown("##### 🟣 SVM")
            f3 = px.imshow(results["SVM"]["confusion_matrix"], x=classes, y=classes, text_auto=True, color_continuous_scale="Purples")
            st.plotly_chart(f3, use_container_width=True)
