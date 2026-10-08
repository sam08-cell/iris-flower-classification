import streamlit as st
import pandas as pd
from models.ml_engine import clean_data

def render_data_cleaning(df_raw: pd.DataFrame):
    """Render interactive data cleaning and verification pipeline."""
    st.markdown("## 🧹 Automated Data Cleaning & Integrity Audit")
    st.caption("Inspect raw data validation, duplicate checks, null value treatment, and cleaning results.")
    
    col1, col2 = st.columns([1.5, 1])
    
    df_cleaned, report = clean_data(df_raw)
    
    with col1:
        st.markdown('<div class="saas-card">', unsafe_allow_html=True)
        st.subheader("🛠️ Data Hygiene Audit Report")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Raw Observations", report["initial_rows"])
        c2.metric("Duplicates Cleared", report["duplicates_removed"])
        c3.metric("Post-Clean Rows", report["final_rows"])
        
        st.markdown("<hr style='margin: 15px 0;'>", unsafe_allow_html=True)
        st.markdown("##### 📌 Audit Findings:")
        st.markdown(f"- **Missing Value Scan:** {report['missing_detected']} total missing cells detected across all numeric features.")
        st.markdown(f"- **Duplicate Record Isolation:** {report['duplicates_removed']} redundant records detected and removed to prevent model overfitting.")
        st.markdown(f"- **Integrity Verification:** {report['status']}")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="saas-card">', unsafe_allow_html=True)
        st.subheader("🔍 Column-Wise Missing Breakdown")
        missing_df = pd.DataFrame(list(report["missing_per_col"].items()), columns=["Column", "Missing Count"])
        missing_df["Missing %"] = (missing_df["Missing Count"] / report["initial_rows"] * 100).map("{:.1f}%".format)
        st.dataframe(missing_df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    # Interactive Comparison Viewer
    st.subheader("📋 Pre-Cleaning vs Post-Cleaning Verification")
    tab_clean, tab_raw = st.tabs(["✅ Cleaned Dataset (Production Ready)", "⚠️ Original Raw Data"])
    
    with tab_clean:
        st.caption(f"Showing cleaned records ({len(df_cleaned)} samples):")
        st.dataframe(df_cleaned, use_container_width=True)
        
    with tab_raw:
        st.caption(f"Showing raw records with duplicates retained ({len(df_raw)} samples):")
        st.dataframe(df_raw, use_container_width=True)
