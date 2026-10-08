import streamlit as st

def render_about_project():
    """Render About Project details, system architecture, and technical references."""
    st.markdown("## ℹ️ About Iris Flower Species Classification System")
    st.caption("Architecture, Mathematical Principles, and Machine Learning Specifications.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="shadcn-card">
                <div class="shadcn-card-title">🎯 Project Objective & Scope</div>
                <div class="shadcn-card-description" style="margin-top: 8px; line-height: 1.6;">
                    The Iris Flower Species Classification System is a machine learning platform 
                    designed to classify botanical specimens into three taxonomic entities:
                </div>
                <ul style="font-size: 0.875rem; margin-top: 8px; line-height: 1.8;">
                    <li><b>Iris Setosa</b></li>
                    <li><b>Iris Versicolor</b></li>
                    <li><b>Iris Virginica</b></li>
                </ul>
                <div class="shadcn-card-description" style="margin-top: 8px; line-height: 1.6;">
                    Built with end-to-end reproducibility, rigorous cross-validation, and user authentication, 
                    the application bridges biological taxonomic measurement and automated decision systems.
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="shadcn-card">
                <div class="shadcn-card-title">🛠️ Technical Architecture & Stack</div>
                <ul style="font-size: 0.875rem; margin-top: 10px; line-height: 1.8;">
                    <li><b>Design System:</b> shadcn/ui zinc aesthetic with Geist typography.</li>
                    <li><b>Machine Learning:</b> Scikit-Learn (KNN, Decision Tree, SVC, 5-Fold GridSearchCV).</li>
                    <li><b>Data Manipulation:</b> Pandas & NumPy.</li>
                    <li><b>Visualization:</b> Plotly Express interactive charts.</li>
                    <li><b>Persistence & Security:</b> SQLite3 with salted SHA-256 cryptographic hashing.</li>
                    <li><b>Document Generation:</b> ReportLab PDF typography engine.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("### 🧬 Mathematical & Algorithmic Background")
    m1, m2, m3 = st.columns(3)
    
    with m1:
        st.markdown("""
            <div class="shadcn-card">
                <div class="shadcn-badge shadcn-badge-secondary" style="margin-bottom: 8px;">K-Nearest Neighbors</div>
                <div class="shadcn-card-title" style="font-size: 1rem;">Instance-Based Classifier</div>
                <div class="shadcn-card-description" style="margin-top: 8px; line-height: 1.6;">
                    Computes Minkowski or Euclidean distance:
                    <br/><br/>
                    <code>d(x, y) = √(∑(xᵢ - yᵢ)²)</code>
                    <br/><br/>
                    Assigns the specimen to the majority vote of the <i>k</i> nearest spatial neighbors in 4-dimensional feature space.
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with m2:
        st.markdown("""
            <div class="shadcn-card">
                <div class="shadcn-badge shadcn-badge-secondary" style="margin-bottom: 8px;">Decision Tree</div>
                <div class="shadcn-card-title" style="font-size: 1rem;">Rule-Based Classifier</div>
                <div class="shadcn-card-description" style="margin-top: 8px; line-height: 1.6;">
                    Minimizes Gini Impurity at each split:
                    <br/><br/>
                    <code>Gini = 1 - ∑(pᵢ)²</code>
                    <br/><br/>
                    Derives orthogonal rules like: <i>"Petal Length ≤ 2.45 cm ➔ Setosa"</i> for maximum explainability.
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with m3:
        st.markdown("""
            <div class="shadcn-card">
                <div class="shadcn-badge shadcn-badge-secondary" style="margin-bottom: 8px;">Support Vector Machine</div>
                <div class="shadcn-card-title" style="font-size: 1rem;">Maximum Margin Classifier</div>
                <div class="shadcn-card-description" style="margin-top: 8px; line-height: 1.6;">
                    Maximizes the geometric functional margin:
                    <br/><br/>
                    <code>max (2 / ||w||)</code>
                    <br/><br/>
                    Separates high-dimensional floral vectors across Radial Basis (RBF) or Linear kernels to achieve optimal classification.
                </div>
            </div>
        """, unsafe_allow_html=True)
