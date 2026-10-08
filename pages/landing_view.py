import streamlit as st

def render_landing_page():
    """Render modern, clean enterprise SaaS Landing page."""
    
    # Hero Section
    st.markdown("""
        <div class="saas-hero">
            <div style="display: inline-block; padding: 4px 12px; background: rgba(255,255,255,0.15); border-radius: 20px; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 12px;">
                Botanical AI Platform • v2.0
            </div>
            <h1>Iris Flower Species Classification System</h1>
            <p>
                An enterprise machine learning pipeline for real-time botanical taxon prediction, 
                automated feature importance evaluation, multi-algorithm benchmarking, and PDF reporting.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Action Buttons
    c_btn1, c_btn2, _ = st.columns([1.3, 1.3, 4])
    with c_btn1:
        if st.button("🚀 Explore Dashboard", type="primary", use_container_width=True):
            st.session_state['selected_menu'] = "📋 Dataset Overview"
            st.rerun()
    with c_btn2:
        if st.button("🔮 Real-Time Prediction", use_container_width=True):
            st.session_state['selected_menu'] = "🔮 Prediction"
            st.rerun()
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Core Architecture Highlights (Dynamic flex height - no text overflow)
    st.subheader("Core System Architecture")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="saas-card">
                <h4>📊 Exploratory Data Analysis</h4>
                <p>
                    Interactive multi-dimensional Plotly visualizations including species distributions, 
                    correlation matrices, and 3D coordinate space mappings.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="saas-card">
                <h4>⚡ Multi-Model Benchmarking</h4>
                <p>
                    Evaluates K-Nearest Neighbors (KNN), Decision Tree, and Support Vector Machine (SVM) 
                    with stratified 80/20 train-test partitioning.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class="saas-card">
                <h4>🎛️ 5-Fold GridSearchCV Tuning</h4>
                <p>
                    Cross-validated hyperparameter optimization across distance metrics, tree depths, 
                    and SVM kernels with automated best model identification.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown("""
            <div class="saas-card">
                <h4>🧹 Automated Data Hygiene</h4>
                <p>
                    Automated duplicate record purging, missing value checks, and statistical data validation.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with col5:
        st.markdown("""
            <div class="saas-card">
                <h4>🎯 Explainable AI Inference</h4>
                <p>
                    Instant taxonomic classification with confidence scoring, probability distribution, and biological rationale.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with col6:
        st.markdown("""
            <div class="saas-card">
                <h4>📄 ReportLab PDF Export</h4>
                <p>
                    Download formal PDF prediction certificates and model benchmark reports.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Technical Overview Section
    st.subheader("Dataset & Scientific Rationale")
    ac1, ac2 = st.columns(2)
    
    with ac1:
        st.markdown("""
            <div class="saas-card">
                <h4>Fisher's Botanical Iris Benchmark</h4>
                <p>
                    Introduced by British statistician Ronald Fisher in 1936, the Iris dataset represents 
                    the quintessential standard for pattern recognition. It measures 150 specimens across 
                    three distinct species:
                </p>
                <ul>
                    <li><b>Iris Setosa</b> — Separable by compact petals (length &lt; 2.5 cm).</li>
                    <li><b>Iris Versicolor</b> — Intermediate morphological petal span.</li>
                    <li><b>Iris Virginica</b> — Prominent petals with expansive dimensions.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with ac2:
        st.markdown("""
            <div class="saas-card">
                <h4>Mathematical Decision Boundaries</h4>
                <p>
                    By formulating mathematical separating hyperplanes across 
                    Sepal Length, Sepal Width, Petal Length, and Petal Width, 
                    the models achieve 95% to 100% precision.
                </p>
                <p>
                    Feature importance audits confirm petal dimensions contribute over 
                    85% of total predictive power due to ecological pollinator specialization.
                </p>
            </div>
        """, unsafe_allow_html=True)

    # Professional Footer
    st.markdown("""
        <hr style="border: 0; border-top: 1px solid #e2e8f0; margin-top: 40px; margin-bottom: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; color: #64748b; font-size: 0.85rem;">
            <div>
                <b>Iris Species Classification System</b> • Machine Learning Production Portal
            </div>
            <div>
                Built with Python, Streamlit, Scikit-Learn, and Plotly
            </div>
        </div>
    """, unsafe_allow_html=True)
