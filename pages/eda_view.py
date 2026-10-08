import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

def render_eda(df: pd.DataFrame):
    """Render comprehensive interactive Exploratory Data Analysis with Plotly."""
    st.markdown("## 📊 Exploratory Data Analysis (EDA)")
    st.caption("Deep morphological discovery and multi-variable statistical distributions using Plotly.")
    
    color_map = {
        'Iris Setosa': '#3b82f6',
        'Iris Versicolor': '#8b5cf6',
        'Iris Virginica': '#ec4899',
        'setosa': '#3b82f6',
        'versicolor': '#8b5cf6',
        'virginica': '#ec4899'
    }

    tabs = st.tabs([
        "🌸 Species Distribution",
        "📊 Histograms & KDE",
        "🧬 Interactive Pair Plot",
        "🔥 Correlation Heatmap",
        "📦 Box & Whisker Outliers",
        "🌌 Multi-Dimensional Scatter"
    ])
    
    # ---------------- 1. Species Distribution ----------------
    with tabs[0]:
        st.subheader("Target Class Composition")
        c1, c2 = st.columns([1.5, 1])
        with c1:
            counts = df['species'].value_counts().reset_index()
            counts.columns = ['Species', 'Count']
            fig_pie = px.pie(
                counts, names='Species', values='Count',
                hole=0.45,
                color='Species',
                color_discrete_map=color_map,
                title="Class Balance Across Species Taxa"
            )
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie, use_container_width=True)
        with c2:
            st.markdown("""
                <div class="glass-card" style="margin-top: 30px;">
                    <h4>Taxonomic Distribution Insights</h4>
                    <p style="font-size: 0.9rem; line-height: 1.5; color: #475569;">
                        The Iris dataset maintains an impeccably balanced class representation (approx. 50 specimens each). 
                        This balance is ideal because classification algorithms will not suffer from majority-class bias, 
                        eliminating the requirement for synthetic oversampling (SMOTE) or sample reweighting.
                    </p>
                </div>
            """, unsafe_allow_html=True)

    # ---------------- 2. Histograms ----------------
    with tabs[1]:
        st.subheader("Feature Distributions & Density")
        feature_choice = st.selectbox(
            "Select Botanical Feature to Inspect:",
            ['petal_length', 'petal_width', 'sepal_length', 'sepal_width']
        )
        fig_hist = px.histogram(
            df, x=feature_choice, color='species',
            marginal="box",
            barmode="overlay",
            opacity=0.7,
            color_discrete_map=color_map,
            title=f"Distribution of {feature_choice.replace('_', ' ').title()} by Species"
        )
        st.plotly_chart(fig_hist, use_container_width=True)
        st.markdown(f"""
            <div class="glass-card">
                <b>Distribution Rationale:</b> 
                Observing the histogram for <code>{feature_choice}</code> reveals the distinctive multi-modal distribution 
                where Iris Setosa forms an isolated cluster, while Versicolor and Virginica exhibit slight continuous overlap.
            </div>
        """, unsafe_allow_html=True)

    # ---------------- 3. Pair Plot ----------------
    with tabs[2]:
        st.subheader("Multi-Attribute Pairwise Interaction (Scatter Matrix)")
        num_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        fig_matrix = px.scatter_matrix(
            df, dimensions=num_cols, color='species',
            color_discrete_map=color_map,
            title="Pairwise Scatter Relationships across All Features",
            opacity=0.8
        )
        fig_matrix.update_layout(height=700)
        st.plotly_chart(fig_matrix, use_container_width=True)
        st.info("💡 Notice that **Petal Length vs Petal Width** exhibits near-linear separability for Iris Setosa and distinct boundary margins for Versicolor/Virginica.")

    # ---------------- 4. Correlation Heatmap ----------------
    with tabs[3]:
        st.subheader("Morphological Pearson Correlation Matrix")
        corr = df[num_cols].corr()
        fig_corr = px.imshow(
            corr,
            text_auto=".2f",
            color_continuous_scale="Viridis",
            title="Pearson Correlation Heatmap Between Floral Dimensions",
            aspect="auto"
        )
        st.plotly_chart(fig_corr, use_container_width=True)
        st.markdown("""
            <div class="glass-card">
                <b>Key Correlation Observations:</b>
                <ul>
                    <li><b>Petal Length and Petal Width:</b> Very high positive correlation (r = 0.96). As petals lengthen, their width scales proportionally.</li>
                    <li><b>Petal Length and Sepal Length:</b> Strong positive correlation (r = 0.87).</li>
                    <li><b>Sepal Width vs Petal Length:</b> Moderate negative correlation (r = -0.42).</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # ---------------- 5. Box Plots ----------------
    with tabs[4]:
        st.subheader("Box & Whisker Dispersion Analysis")
        box_feat = st.selectbox("Select feature for Box Plot:", num_cols, key="box_feat_sel")
        fig_box = px.box(
            df, x='species', y=box_feat, color='species',
            points="all",
            color_discrete_map=color_map,
            title=f"Box Plot of {box_feat.replace('_', ' ').title()} by Species"
        )
        st.plotly_chart(fig_box, use_container_width=True)
        st.caption("Individual jittered points show exact observation variance, medians, interquartile ranges (IQR), and potential biological outliers.")

    # ---------------- 6. Scatter Plot ----------------
    with tabs[5]:
        st.subheader("Interactive 2D & 3D Morphological Scatter Mapping")
        sc1, sc2 = st.columns(2)
        with sc1:
            x_axis = st.selectbox("X-Axis Feature:", num_cols, index=2)
        with sc2:
            y_axis = st.selectbox("Y-Axis Feature:", num_cols, index=3)
            
        fig_scatter = px.scatter(
            df, x=x_axis, y=y_axis, color='species',
            size='sepal_length',
            hover_data=num_cols,
            color_discrete_map=color_map,
            title=f"{y_axis.title()} vs {x_axis.title()} (Point Size = Sepal Length)"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        
        with st.expander("🌌 View in 3D Coordinate Space"):
            fig_3d = px.scatter_3d(
                df, x='sepal_length', y='petal_length', z='petal_width',
                color='species',
                color_discrete_map=color_map,
                title="3D Spatial Projection (Sepal Length × Petal Length × Petal Width)"
            )
            fig_3d.update_layout(height=600)
            st.plotly_chart(fig_3d, use_container_width=True)
