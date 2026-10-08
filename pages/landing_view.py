import streamlit as st

def render_landing_page():
    """Render modern SaaS Landing page with Hero, Features, About, and Footer."""
    
    # Hero Section
    st.markdown("""
        <div class="hero-banner">
            <div style="font-size: 3.5rem; margin-bottom: 10px;">🌸 🤖 📊</div>
            <h1 class="hero-title">Iris Flower Classification using Machine Learning</h1>
            <p class="hero-subtitle">
                Predict flower species instantly using Artificial Intelligence. 
                Explore automated data cleaning, exploratory visual analytics, multi-model benchmarking, 
                hyperparameter optimization, and exportable PDF intelligence reports.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Hero Call-to-Action Buttons
    col_btn1, col_btn2, col_space = st.columns([1.5, 1.5, 4])
    with col_btn1:
        if st.button("🚀 Get Started", type="primary", use_container_width=True):
            if st.session_state.get('logged_in', False):
                st.session_state['current_page'] = "Dashboard"
            else:
                st.session_state['current_page'] = "Auth"
            st.rerun()
    with col_btn2:
        if st.button("🔐 Login to Portal", use_container_width=True):
            st.session_state['current_page'] = "Auth"
            st.rerun()
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Features Section
    st.markdown("### 🌟 Key Platform Capabilities")
    fcol1, fcol2, fcol3 = st.columns(3)
    
    with fcol1:
        st.markdown("""
            <div class="glass-card" style="height: 220px;">
                <div style="font-size: 2.2rem; margin-bottom: 8px;">📊</div>
                <h4 style="margin: 0; font-weight: 700;">Data Analysis & EDA</h4>
                <p style="color: #64748b; font-size: 0.9rem; margin-top: 8px;">
                    Interactive 3D scatter plots, species distribution charts, correlation heatmaps, 
                    and box plots with Plotly visualizations.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with fcol2:
        st.markdown("""
            <div class="glass-card" style="height: 220px;">
                <div style="font-size: 2.2rem; margin-bottom: 8px;">⚡</div>
                <h4 style="margin: 0; font-weight: 700;">Multi-Model Training</h4>
                <p style="color: #64748b; font-size: 0.9rem; margin-top: 8px;">
                    Benchmarking K-Nearest Neighbors (KNN), Decision Tree, and Support Vector Machine (SVM) 
                    with GridSearchCV hyperparameter tuning.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with fcol3:
        st.markdown("""
            <div class="glass-card" style="height: 220px;">
                <div style="font-size: 2.2rem; margin-bottom: 8px;">🎯</div>
                <h4 style="margin: 0; font-weight: 700;">Real-Time Inference</h4>
                <p style="color: #64748b; font-size: 0.9rem; margin-top: 8px;">
                    Instant morphological dimension evaluation, confidence metric scoring, 
                    species imagery rendering, and downloadable PDF reports.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    # Second row of features
    fcol4, fcol5, fcol6 = st.columns(3)
    with fcol4:
        st.markdown("""
            <div class="glass-card" style="height: 200px;">
                <div style="font-size: 2.2rem; margin-bottom: 8px;">🧹</div>
                <h4 style="margin: 0; font-weight: 700;">Automated Data Cleaning</h4>
                <p style="color: #64748b; font-size: 0.9rem; margin-top: 8px;">
                    Automatic duplicate identification, missing value imputation, and validation auditing.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with fcol5:
        st.markdown("""
            <div class="glass-card" style="height: 200px;">
                <div style="font-size: 2.2rem; margin-bottom: 8px;">📈</div>
                <h4 style="margin: 0; font-weight: 700;">Model Comparison Matrix</h4>
                <p style="color: #64748b; font-size: 0.9rem; margin-top: 8px;">
                    Real-time comparison of Accuracy, Precision, Recall, and F1 Score with automatic top performer highlights.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with fcol6:
        st.markdown("""
            <div class="glass-card" style="height: 200px;">
                <div style="font-size: 2.2rem; margin-bottom: 8px;">🔒</div>
                <h4 style="margin: 0; font-weight: 700;">Secure SQLite Data Store</h4>
                <p style="color: #64748b; font-size: 0.9rem; margin-top: 8px;">
                    Built-in user credential hashing, login auditing, and prediction persistence with query filters.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # About Section
    st.markdown("### 📖 About the Botanical Intelligence Platform")
    acol1, acol2 = st.columns(2)
    
    with acol1:
        st.markdown("""
            <div class="glass-card">
                <h4 style="color: #4f46e5;">What is the Iris Dataset?</h4>
                <p style="font-size: 0.92rem; line-height: 1.6; color: #475569;">
                    Introduced by British statistician and biologist Ronald Fisher in 1936, the Iris flower dataset 
                    is the quintessential benchmark in pattern recognition and machine learning literature. 
                    It comprises 150 biological specimens across three distinct subspecies:
                </p>
                <ul style="font-size: 0.9rem; color: #475569; padding-left: 20px;">
                    <li><b>Iris Setosa</b> - Highly separable with compact petals.</li>
                    <li><b>Iris Versicolor</b> - Moderate petal span and intermediate morphology.</li>
                    <li><b>Iris Virginica</b> - Prominent petals with expansive dimensions.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with acol2:
        st.markdown("""
            <div class="glass-card">
                <h4 style="color: #9333ea;">Importance of Botanical ML</h4>
                <p style="font-size: 0.92rem; line-height: 1.6; color: #475569;">
                    Automated botanical classification replaces manual taxonomic measurement with high-throughput 
                    computer vision and supervised algorithms.
                </p>
                <p style="font-size: 0.92rem; line-height: 1.6; color: #475569;">
                    By training mathematical decision boundaries across Sepal Length, Sepal Width, Petal Length, 
                    and Petal Width, intelligent models achieve 95% to 100% classification precision without destructive 
                    laboratory intervention.
                </p>
            </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <hr style="border: 0; border-top: 1px solid rgba(226, 232, 240, 0.8); margin-top: 40px; margin-bottom: 25px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; color: #64748b; font-size: 0.88rem;">
            <div>
                <b>Iris Flower Species Classification System</b> | Production AI Application
            </div>
            <div style="display: flex; gap: 20px;">
                <span>📘 Documentation</span>
                <span>📬 Contact Support</span>
                <span>⭐ GitHub Repository</span>
                <span>🔒 Privacy & Security</span>
            </div>
        </div>
        <div style="text-align: center; color: #94a3b8; font-size: 0.78rem; margin-top: 15px;">
            © 2026 Machine Learning Project Systems. All rights reserved.
        </div>
    """, unsafe_allow_html=True)
