import streamlit as st
import pandas as pd

def render_dataset_overview(df: pd.DataFrame):
    """Render Dataset Overview section using shadcn/ui stat cards and data tables."""
    st.markdown("## Dataset Overview")
    st.caption("Morphological and taxonomic profile of the Fisher Iris benchmark collection.")
    
    # shadcn/ui Stat Badges
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"""
            <div class="shadcn-stat">
                <div class="stat-label">Total Observations</div>
                <div class="stat-value">{df.shape[0]}</div>
            </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
            <div class="shadcn-stat">
                <div class="stat-label">Attributes / Features</div>
                <div class="stat-value">{df.shape[1]}</div>
            </div>
        """, unsafe_allow_html=True)
    with m3:
        st.markdown(f"""
            <div class="shadcn-stat">
                <div class="stat-label">Taxonomic Classes</div>
                <div class="stat-value">{df['species'].nunique()}</div>
            </div>
        """, unsafe_allow_html=True)
    with m4:
        st.markdown(f"""
            <div class="shadcn-stat">
                <div class="stat-label">Missing Cell Count</div>
                <div class="stat-value">{int(df.isnull().sum().sum())}</div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
    
    # Dataset Sample Records
    st.markdown("### Sample Records")
    sample_size = st.slider("Display limit:", min_value=5, max_value=50, value=10, step=5)
    st.dataframe(df.head(sample_size), use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Descriptive Statistics")
        stats_df = df.describe().T[['count', 'mean', 'std', 'min', '50%', 'max']]
        stats_df.columns = ['Count', 'Mean (cm)', 'Std Dev', 'Min (cm)', 'Median (cm)', 'Max (cm)']
        st.dataframe(stats_df.style.format("{:.2f}"), use_container_width=True)
        
    with col2:
        st.markdown("### Metadata & Data Types")
        info_data = []
        for col in df.columns:
            info_data.append({
                "Feature": col,
                "Type": str(df[col].dtype),
                "Non-Null": f"{df[col].count()} / {len(df)}",
                "Null Count": int(df[col].isnull().sum()),
                "Unique": int(df[col].nunique())
            })
        st.dataframe(pd.DataFrame(info_data), use_container_width=True)
        
    # Class Distribution Snapshot
    st.markdown("### Taxonomic Balance")
    class_counts = df['species'].value_counts().reset_index()
    class_counts.columns = ['Species', 'Sample Count']
    class_counts['Ratio'] = (class_counts['Sample Count'] / len(df) * 100).apply(lambda x: f"{x:.1f}%")
    st.dataframe(class_counts, use_container_width=True)
