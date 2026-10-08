import streamlit as st
import pandas as pd
import plotly.express as px
from models.ml_engine import get_train_test_split, train_default_models

def render_model_comparison(df: pd.DataFrame):
    """Render Algorithm Benchmark Comparison dashboard highlighting top model."""
    st.markdown("## 📊 Model Comparison & Benchmark Leaderboard")
    st.caption("Side-by-side performance comparison across Accuracy, Precision, Recall, and F1 Score.")
    
    if 'default_results' not in st.session_state:
        X_train, X_test, y_train, y_test = get_train_test_split(df)
        st.session_state['default_results'] = train_default_models(X_train, X_test, y_train, y_test)
        
    results = st.session_state['default_results']
    
    # Build comparison dataframe
    table_rows = []
    for algo, metric in results.items():
        table_rows.append({
            "Algorithm": algo,
            "Accuracy": metric["accuracy"],
            "Precision": metric["precision"],
            "Recall": metric["recall"],
            "F1 Score": metric["f1_score"]
        })
        
    comp_df = pd.DataFrame(table_rows)
    # Find best model based on F1 Score & Accuracy
    best_idx = comp_df['F1 Score'].idxmax()
    best_algo = comp_df.loc[best_idx, 'Algorithm']
    best_acc = comp_df.loc[best_idx, 'Accuracy']
    
    # Store for PDF report generator
    st.session_state['comparison_table_data'] = [
        {**row, "is_best": (row['Algorithm'] == best_algo)} for row in table_rows
    ]
    
    # Winner Banner
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(5, 150, 105, 0.25) 100%); 
                    border: 2px solid #10b981; border-radius: 16px; padding: 20px 24px; margin-bottom: 24px; display: flex; align-items: center; justify-content: space-between;">
            <div>
                <span class="best-badge">🥇 TOP PERFORMING MODEL</span>
                <h3 style="margin: 8px 0 4px 0; color: #065f46;">{best_algo}</h3>
                <p style="margin: 0; color: #047857; font-size: 0.95rem;">
                    Achieved superior classification accuracy of <b>{best_acc*100:.2f}%</b> and balanced F1 Score on the test partition.
                </p>
            </div>
            <div style="font-size: 3rem;">🎖️</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Comparison Table
    st.subheader("📋 Comprehensive Comparison Matrix")
    
    # Display formatted table
    formatted_df = comp_df.copy()
    formatted_df["Accuracy"] = formatted_df["Accuracy"].map(lambda x: f"{x*100:.2f}%")
    formatted_df["Precision"] = formatted_df["Precision"].map(lambda x: f"{x*100:.2f}%")
    formatted_df["Recall"] = formatted_df["Recall"].map(lambda x: f"{x*100:.2f}%")
    formatted_df["F1 Score"] = formatted_df["F1 Score"].map(lambda x: f"{x*100:.2f}%")
    
    st.dataframe(formatted_df, use_container_width=True)
    
    # Comparative Bar Chart
    st.subheader("📊 Visual Benchmark Comparison")
    
    melted_df = comp_df.melt(id_vars=["Algorithm"], var_name="Metric", value_name="Score")
    melted_df["Score (%)"] = melted_df["Score"] * 100
    
    fig_bar = px.bar(
        melted_df, x="Algorithm", y="Score (%)", color="Metric",
        barmode="group",
        color_discrete_sequence=['#4f46e5', '#8b5cf6', '#ec4899', '#10b981'],
        title="Comparison of Performance Metrics by Algorithm"
    )
    fig_bar.update_layout(yaxis_range=[80, 103])
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # Technical Insights
    st.markdown("""
        <div class="saas-card">
            <h4>Algorithm Behavior Analysis</h4>
            <p style="font-size: 0.92rem; color: #475569; line-height: 1.6;">
                • <b>Support Vector Machine (SVM):</b> Calculates optimal separating hyperplanes with maximum geometric margin, rendering it resilient against boundary noise.<br/>
                • <b>K-Nearest Neighbors (KNN):</b> Instance-based learner performing localized spatial distance matching. Sensitive to scale but highly effective for non-linear Iris distributions.<br/>
                • <b>Decision Tree:</b> Derives orthogonal axis-parallel thresholds. Highly interpretable, but susceptible to minor variance on small boundary clusters.
            </p>
        </div>
    """, unsafe_allow_html=True)
