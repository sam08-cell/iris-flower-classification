import streamlit as st

def render_about_project():
    """Render About Project details, system architecture, and technical references."""
    st.markdown("## ℹ️ About Iris Flower Species Classification System")
    st.caption("Architecture, Mathematical Principles, and Machine Learning Specifications.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="saas-card">
                <h4>🎯 Project Objective & Scope</h4>
                <p style="font-size: 0.92rem; color: #475569; line-height: 1.6;">
                    The Iris Flower Species Classification System is an enterprise-grade machine learning platform 
                    designed to classify botanical specimens into three taxonomic entities:
                </p>
                <ol style="font-size: 0.9rem; color: #475569; padding-left: 20px;">
                    <li><b>Iris Setosa</b></li>
                    <li><b>Iris Versicolor</b></li>
                    <li><b>Iris Virginica</b></li>
                </ol>
                <p style="font-size: 0.92rem; color: #475569; line-height: 1.6;">
                    Built with end-to-end reproducibility, rigorous cross-validation, and user authentication, 
                    the application bridges biological taxonomic measurement and automated decision systems.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="saas-card">
                <h4>🛠️ Technical Architecture & Stack</h4>
                <ul style="font-size: 0.9rem; color: #475569; padding-left: 20px; line-height: 1.7;">
                    <li><b>Front-End:</b> Streamlit 1.45+ with responsive Glassmorphic design and CSS3 animations.</li>
                    <li><b>Machine Learning:</b> Scikit-Learn (KNeighborsClassifier, DecisionTreeClassifier, SVC, GridSearchCV).</li>
                    <li><b>Data Manipulation:</b> Pandas & NumPy.</li>
                    <li><b>Visualization:</b> Plotly Express & Figure Factory for interactive charts.</li>
                    <li><b>Authentication & Persistence:</b> SQLite3 with salted SHA-256 cryptographic hashing.</li>
                    <li><b>Document Generation:</b> ReportLab PDF typography engine.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("### 🧬 Mathematical & Algorithmic Background")
    m1, m2, m3 = st.columns(3)
    
    with m1:
        st.markdown("""
            <div class="saas-card">
                <h5 style="color: #2563eb;">K-Nearest Neighbors</h5>
                <p style="font-size: 0.88rem; color: #475569;">
                    Computes Minkowski or Euclidean distance:
                    <br/><br/>
                    <code>d(x, y) = √(∑(xᵢ - yᵢ)²)</code>
                    <br/><br/>
                    Assigns the specimen to the majority vote of the <i>k</i> nearest spatial neighbors in 4-dimensional space.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with m2:
        st.markdown("""
            <div class="saas-card">
                <h5 style="color: #059669;">Decision Tree</h5>
                <p style="font-size: 0.88rem; color: #475569;">
                    Minimizes Gini Impurity at each split:
                    <br/><br/>
                    <code>Gini = 1 - ∑(pᵢ)²</code>
                    <br/><br/>
                    Derives orthogonal rules like: <i>"Petal Length ≤ 2.45 cm ➔ Setosa"</i> for maximum explainability.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with m3:
        st.markdown("""
            <div class="saas-card">
                <h5 style="color: #9333ea;">Support Vector Machine</h5>
                <p style="font-size: 0.88rem; color: #475569;">
                    Maximizes the geometric functional margin:
                    <br/><br/>
                    <code>max (2 / ||w||)</code>
                    <br/><br/>
                    Projects high-dimensional floral vectors across Radial Basis (RBF) or Linear kernels to achieve optimal separation.
                </p>
            </div>
        """, unsafe_allow_html=True)
