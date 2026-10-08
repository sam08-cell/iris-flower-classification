import streamlit as st
import pandas as pd
from models.ml_engine import clean_data

def render_data_cleaning(df_raw: pd.DataFrame):
    """Render interactive data cleaning and verification pipeline using shadcn/ui components."""
    st.markdown("## Data Cleaning & Integrity Audit")
    st.caption("Automated duplicate purge, missing cell imputation, and structural dataset verification.")
    
    col1, col2 = st.columns([1.5, 1])
    df_cleaned, report = clean_data(df_raw)
    
    with col1:
        st.markdown(f"""
            <div class="shadcn-card">
                <div class="shadcn-card-header">
                    <span class="shadcn-card-title">Data Hygiene Audit</span>
                    <span class="shadcn-card-description">Summary of automated pipeline sanitization</span>
                </div>
                <div class="shadcn-card-content">
                    <div style="display: flex; gap: 1rem; margin-bottom: 1.25rem;">
                        <div style="flex: 1; border: 1px solid var(--border); border-radius: 0.5rem; padding: 0.75rem;">
                            <div style="font-size: 0.75rem; color: var(--muted-foreground);">Raw Count</div>
                            <div style="font-size: 1.25rem; font-weight: 700;">{report["initial_rows"]}</div>
                        </div>
                        <div style="flex: 1; border: 1px solid var(--border); border-radius: 0.5rem; padding: 0.75rem;">
                            <div style="font-size: 0.75rem; color: var(--muted-foreground);">Duplicates Cleared</div>
                            <div style="font-size: 1.25rem; font-weight: 700; color: #10b981;">{report["duplicates_removed"]}</div>
                        </div>
                        <div style="flex: 1; border: 1px solid var(--border); border-radius: 0.5rem; padding: 0.75rem;">
                            <div style="font-size: 0.75rem; color: var(--muted-foreground);">Clean Rows</div>
                            <div style="font-size: 1.25rem; font-weight: 700;">{report["final_rows"]}</div>
                        </div>
                    </div>
                    <b>Validation Details:</b>
                    <ul style="padding-left: 1.25rem; margin-top: 0.5rem; margin-bottom: 0;">
                        <li>Missing Cells: {report['missing_detected']} detected across all numeric dimensions.</li>
                        <li>Redundant Records: {report['duplicates_removed']} removed to prevent model overfitting.</li>
                        <li>System Status: {report['status']}</li>
                    </ul>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="shadcn-card">
                <div class="shadcn-card-header">
                    <span class="shadcn-card-title">Missing Breakdown</span>
                    <span class="shadcn-card-description">Per-column completeness check</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        missing_df = pd.DataFrame(list(report["missing_per_col"].items()), columns=["Feature", "Missing"])
        missing_df["Missing %"] = (missing_df["Missing"] / report["initial_rows"] * 100).map("{:.1f}%".format)
        st.dataframe(missing_df, use_container_width=True)
        
    # Interactive Comparison Viewer
    st.markdown("### Pre-Cleaning vs Post-Cleaning Verification")
    tab_clean, tab_raw = st.tabs(["Cleaned Dataset (Ready)", "Raw Dataset"])
    
    with tab_clean:
        st.caption(f"Showing cleaned records ({len(df_cleaned)} observations):")
        st.dataframe(df_cleaned, use_container_width=True)
        
    with tab_raw:
        st.caption(f"Showing raw records with duplicates ({len(df_raw)} observations):")
        st.dataframe(df_raw, use_container_width=True)
