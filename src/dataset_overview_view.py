import streamlit as st
import pandas as pd
import io

def render_dataset_overview(df: pd.DataFrame):
    """Render Dataset Overview section with metrics, info, missing values, and samples."""
    st.markdown("## 📋 Dataset Overview")
    st.caption("Morphological and taxonomic profile of the Fisher Iris benchmark collection.")
    
    # Key Metrics Cards
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"""
            <div class="metric-badge">
                <div class="metric-value">{df.shape[0]}</div>
                <div class="metric-label">Total Observations</div>
            </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
            <div class="metric-badge">
                <div class="metric-value">{df.shape[1]}</div>
                <div class="metric-label">Attributes / Features</div>
            </div>
        """, unsafe_allow_html=True)
    with m3:
        st.markdown(f"""
            <div class="metric-badge">
                <div class="metric-value">{df['species'].nunique()}</div>
                <div class="metric-label">Target Taxon Classes</div>
            </div>
        """, unsafe_allow_html=True)
    with m4:
        st.markdown(f"""
            <div class="metric-badge">
                <div class="metric-value">{int(df.isnull().sum().sum())}</div>
                <div class="metric-label">Missing Cell Count</div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Dataset Sample Records
    st.subheader("🔍 Sample Observations (Preview)")
    sample_size = st.slider("Select sample display limit:", min_value=5, max_value=50, value=10, step=5)
    
    # Styled dataframe
    st.dataframe(df.head(sample_size), use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Descriptive Statistical Summary")
        stats_df = df.describe().T[['count', 'mean', 'std', 'min', '50%', 'max']]
        stats_df.columns = ['Count', 'Mean (cm)', 'Std Dev', 'Min (cm)', 'Median (cm)', 'Max (cm)']
        st.dataframe(stats_df.style.format("{:.2f}"), use_container_width=True)
        
    with col2:
        st.subheader("ℹ️ Metadata & Column Data Types")
        info_data = []
        for col in df.columns:
            info_data.append({
                "Column Name": col,
                "Data Type": str(df[col].dtype),
                "Non-Null Count": f"{df[col].count()} / {len(df)}",
                "Null Values": int(df[col].isnull().sum()),
                "Unique Values": int(df[col].nunique())
            })
        st.dataframe(pd.DataFrame(info_data), use_container_width=True)
        
    # Class Distribution Snapshot
    st.subheader("🌸 Class Balance Snapshot")
    class_counts = df['species'].value_counts().reset_index()
    class_counts.columns = ['Species Name', 'Sample Count']
    class_counts['Class Percentage'] = (class_counts['Sample Count'] / len(df) * 100).apply(lambda x: f"{x:.1f}%")
    st.dataframe(class_counts, use_container_width=True)
