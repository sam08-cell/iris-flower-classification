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
    
    # Winner Banner (shadcn/ui style card)
    st.markdown(f"""
        <div class="shadcn-card" style="border-left: 4px solid #10b981;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <span class="shadcn-badge shadcn-badge-success">Top Performing Model</span>
                    <div class="shadcn-card-title" style="font-size: 1.5rem !important; margin: 0.5rem 0 0.25rem 0 !important;">{best_algo}</div>
                    <div class="shadcn-card-description">
                        Achieved superior classification accuracy of <b>{best_acc*100:.2f}%</b> and balanced F1-score across holdout tests.
                    </div>
                </div>
                <span class="shadcn-badge shadcn-badge-outline">Rank 1</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Comparison Table
    st.subheader("Comparison Matrix")
    
    # Display formatted table
    formatted_df = comp_df.copy()
    formatted_df["Accuracy"] = formatted_df["Accuracy"].map(lambda x: f"{x*100:.2f}%")
    formatted_df["Precision"] = formatted_df["Precision"].map(lambda x: f"{x*100:.2f}%")
    formatted_df["Recall"] = formatted_df["Recall"].map(lambda x: f"{x*100:.2f}%")
    formatted_df["F1 Score"] = formatted_df["F1 Score"].map(lambda x: f"{x*100:.2f}%")
    
    st.dataframe(formatted_df, use_container_width=True)
    
    # Comparative Bar Chart
    st.subheader("Performance Metrics Benchmark")
    
    melted_df = comp_df.melt(id_vars=["Algorithm"], var_name="Metric", value_name="Score")
    melted_df["Score (%)"] = melted_df["Score"] * 100
    
    fig_bar = px.bar(
        melted_df, x="Algorithm", y="Score (%)", color="Metric",
        barmode="group",
        color_discrete_sequence=['#18181b', '#71717a', '#a1a1aa', '#10b981'],
        title="Metric Comparison by Algorithm"
    )
    fig_bar.update_layout(
        yaxis_range=[80, 103],
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # Technical Insights
    st.markdown("""
        <div class="shadcn-card">
            <div class="shadcn-card-header">
                <span class="shadcn-card-title">Algorithmic Behavior Summary</span>
            </div>
            <div class="shadcn-card-content">
                <ul style="padding-left: 1.25rem; margin: 0;">
                    <li><b>Support Vector Machine (SVM):</b> Maximizes geometric margin separation hyperplanes, resilient to boundary noise.</li>
                    <li><b>K-Nearest Neighbors (KNN):</b> Instance-based localized spatial distance matching.</li>
                    <li><b>Decision Tree:</b> Derives orthogonal axis-parallel thresholds with high rule interpretability.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
