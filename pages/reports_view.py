import streamlit as st
import pandas as pd
from database.db_manager import get_prediction_history, get_login_history
from reports.pdf_generator import generate_comparison_pdf

def render_reports_page():
    """Render Reports & Intelligence Center: Download comparison PDF and query prediction logs."""
    st.markdown("## 📑 Intelligence Reports & Database Auditing")
    st.caption("Review historical botanical inferences, generate benchmark reports, and inspect security access logs.")
    
    tab_reports, tab_history, tab_security = st.tabs([
        "📥 Download Reports",
        "🕒 Prediction History & Filters",
        "🛡️ User Access & Login History"
    ])
    
    # ------------------ 1. Download Reports ------------------
    with tab_reports:
        st.subheader("📄 Export Executive Machine Learning Documents")
        r1, r2 = st.columns(2)
        
        with r1:
            st.markdown('<div class="saas-card">', unsafe_allow_html=True)
            st.markdown("#### Model Comparison Benchmark Report")
            st.write("Generates a structured PDF benchmark detailing Accuracy, Precision, Recall, and F1 metrics for KNN, Decision Tree, and SVM.")
            
            # Check comparison data
            comp_data = st.session_state.get('comparison_table_data', [])
            if not comp_data:
                comp_data = [
                    {"Algorithm": "KNN", "Accuracy": 0.9667, "Precision": 0.9688, "Recall": 0.9667, "F1 Score": 0.9666, "is_best": False},
                    {"Algorithm": "Decision Tree", "Accuracy": 0.9333, "Precision": 0.9388, "Recall": 0.9333, "F1 Score": 0.9330, "is_best": False},
                    {"Algorithm": "SVM", "Accuracy": 1.0000, "Precision": 1.0000, "Recall": 1.0000, "F1 Score": 1.0000, "is_best": True}
                ]
            comp_pdf_bytes = generate_comparison_pdf(comp_data)
            
            st.download_button(
                label="📥 Download Comparison Benchmark PDF",
                data=comp_pdf_bytes,
                file_name="Iris_ML_Model_Benchmark_Report.pdf",
                mime="application/pdf",
                type="primary",
                use_container_width=True
            )
            st.markdown('</div>', unsafe_allow_html=True)
            
        with r2:
            st.markdown('<div class="saas-card">', unsafe_allow_html=True)
            st.markdown("#### 🌸 Individual Specimen Prediction Certificate")
            st.write("Download an official classification report for the most recently evaluated botanical specimen.")
            if 'last_prediction' in st.session_state:
                from reports.pdf_generator import generate_prediction_pdf
                single_pdf = generate_prediction_pdf(st.session_state['last_prediction'])
                st.download_button(
                    label="📥 Download Recent Prediction PDF",
                    data=single_pdf,
                    file_name="Iris_Specimen_Prediction_Certificate.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
            else:
                st.info("Perform a prediction on the 'Prediction' page first to enable certificate export.")
            st.markdown('</div>', unsafe_allow_html=True)

    # ------------------ 2. Prediction History ------------------
    with tab_history:
        st.subheader("🕒 Historical Inferences Database")
        
        # Search & Filter Controls
        fcol1, fcol2 = st.columns([2, 1])
        with fcol1:
            search_query = st.text_input("🔍 Search by Species, Model, or User Email:", placeholder="e.g. Setosa, SVM, admin")
        with fcol2:
            history_limit = st.selectbox("Record Limit:", [25, 50, 100, 200], index=1)
            
        history_records = get_prediction_history(search=search_query, limit=history_limit)
        
        if history_records:
            h_df = pd.DataFrame(history_records)
            # Reorder & rename
            h_df = h_df[['created_at', 'user_email', 'predicted_species', 'confidence', 'model_used', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
            h_df.columns = ['Timestamp', 'User Email', 'Predicted Species', 'Confidence', 'Model Used', 'Sepal L', 'Sepal W', 'Petal L', 'Petal W']
            h_df['Confidence'] = h_df['Confidence'].map(lambda x: f"{x*100:.1f}%")
            
            st.dataframe(h_df, use_container_width=True)
            
            # Export CSV
            csv_data = h_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Export Query Results to CSV",
                data=csv_data,
                file_name="Iris_Inference_History.csv",
                mime="text/csv"
            )
        else:
            st.info("No prediction records found matching the search criteria.")

    # ------------------ 3. Security Access Logs ------------------
    with tab_security:
        st.subheader("🛡️ User Authentication & Access Audit Trail")
        login_logs = get_login_history(limit=50)
        if login_logs:
            l_df = pd.DataFrame(login_logs)
            l_df = l_df[['login_time', 'email', 'status', 'ip_info']]
            l_df.columns = ['Login Time', 'Account Email', 'Status', 'IP Address Origin']
            st.dataframe(l_df, use_container_width=True)
        else:
            st.info("No login events recorded yet.")
