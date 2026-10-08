import streamlit as st
import os
import plotly.express as px
from models.ml_engine import predict_single
from database.db_manager import log_prediction
from reports.pdf_generator import generate_prediction_pdf

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

def render_prediction_page():
    """Render real-time prediction interface with image cards, confidence bars, and PDF generation."""
    st.markdown("## 🔮 Real-Time Iris Flower Species Classification")
    st.caption("Provide floral morphological dimensions to obtain instant algorithmic taxon predictions.")
    
    col_input, col_result = st.columns([1.1, 1.4])
    
    with col_input:
        st.markdown('<div class="saas-card">', unsafe_allow_html=True)
        st.subheader("Floral Measurement Inputs")
        
        # Preset buttons for quick testing
        st.markdown("<p style='font-size: 0.85rem; color: #64748b; margin-bottom: 5px;'>Quick Sample Presets:</p>", unsafe_allow_html=True)
        preset_cols = st.columns(3)
        if preset_cols[0].button("Setosa"):
            st.session_state['input_sl'] = 5.1
            st.session_state['input_sw'] = 3.5
            st.session_state['input_pl'] = 1.4
            st.session_state['input_pw'] = 0.2
        if preset_cols[1].button("Versicolor"):
            st.session_state['input_sl'] = 6.0
            st.session_state['input_sw'] = 2.9
            st.session_state['input_pl'] = 4.5
            st.session_state['input_pw'] = 1.5
        if preset_cols[2].button("Virginica"):
            st.session_state['input_sl'] = 6.9
            st.session_state['input_sw'] = 3.1
            st.session_state['input_pl'] = 5.8
            st.session_state['input_pw'] = 2.1
            
        sl = st.number_input("Sepal Length (cm)", min_value=3.5, max_value=9.0, value=st.session_state.get('input_sl', 5.8), step=0.1)
        sw = st.number_input("Sepal Width (cm)", min_value=1.5, max_value=5.0, value=st.session_state.get('input_sw', 3.0), step=0.1)
        pl = st.number_input("Petal Length (cm)", min_value=0.5, max_value=8.0, value=st.session_state.get('input_pl', 4.3), step=0.1)
        pw = st.number_input("Petal Width (cm)", min_value=0.1, max_value=3.5, value=st.session_state.get('input_pw', 1.3), step=0.1)
        
        model_choice = st.selectbox(
            "Predictive Algorithm Architecture:",
            ["SVM (Tuned)", "KNN (Tuned)", "Decision Tree (Tuned)", "SVM", "KNN", "Decision Tree"]
        )
        
        predict_clicked = st.button("Predict Species", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_result:
        if predict_clicked:
            with st.spinner("Executing statistical inference and confidence evaluation..."):
                pred_species, confidence, prob_dict, explanation = predict_single(
                    sl, sw, pl, pw, model_type=model_choice
                )
                
                # Save to database
                user_email = st.session_state.get('user', {}).get('email', 'guest@iris.ai')
                log_prediction(user_email, sl, sw, pl, pw, model_choice, pred_species, confidence)
                
                # Store in session state for downloading report
                st.session_state['last_prediction'] = {
                    "user_email": user_email,
                    "sepal_length": sl,
                    "sepal_width": sw,
                    "petal_length": pl,
                    "petal_width": pw,
                    "model_used": model_choice,
                    "predicted_species": pred_species,
                    "confidence": confidence,
                    "probabilities": prob_dict,
                    "explanation": explanation
                }
                
        if 'last_prediction' in st.session_state:
            last = st.session_state['last_prediction']
            species = last["predicted_species"]
            conf = last["confidence"]
            
            # Species card theme
            css_class = "prediction-card-setosa"
            img_file = "setosa.png"
            if "Versicolor" in species:
                css_class = "prediction-card-versicolor"
                img_file = "versicolor.png"
            elif "Virginica" in species:
                css_class = "prediction-card-virginica"
                img_file = "virginica.png"
                
            img_path = os.path.join(ASSETS_DIR, img_file)
            
            # Clean, high-contrast outcome banner
            badge_class = "species-tag-setosa"
            if "Versicolor" in species:
                badge_class = "species-tag-versicolor"
            elif "Virginica" in species:
                badge_class = "species-tag-virginica"
                
            st.markdown(f"""
                <div class="saas-card" style="border-left: 5px solid #4f46e5; margin-bottom: 20px;">
                    <div class="species-tag {badge_class}">Identified Species Taxon</div>
                    <h2 style="margin: 10px 0 6px 0; font-size: 2rem; color: #0f172a; font-weight: 800;">{species}</h2>
                    <p style="margin: 0; font-size: 1.05rem; font-weight: 600; color: #4338ca;">
                        Algorithmic Confidence: <b>{conf * 100:.2f}%</b> (High Reliability)
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Image and explanation columns
            ic1, ic2 = st.columns([1, 1.4])
            with ic1:
                if os.path.exists(img_path):
                    st.image(img_path, caption=f"Botanical Specimen: {species}", use_container_width=True)
                else:
                    st.info(f"🌸 Specimen: {species}")
            with ic2:
                st.markdown("#### 🔬 AI Inference Explanation")
                st.write(last["explanation"])
                
                # Probability distribution chart
                probs = last.get("probabilities", {})
                if probs:
                    prob_items = [{"Class": k, "Probability (%)": v * 100} for k, v in probs.items()]
                    fig_p = px.bar(
                        prob_items, x="Probability (%)", y="Class",
                        orientation="h",
                        color="Probability (%)",
                        color_continuous_scale="Viridis",
                        height=180
                    )
                    fig_p.update_layout(margin=dict(l=5, r=5, t=5, b=5), yaxis={'categoryorder':'total ascending'})
                    st.plotly_chart(fig_p, use_container_width=True)
                    
            # Download PDF Report button
            pdf_bytes = generate_prediction_pdf(last)
            st.download_button(
                label="📄 Download Official Prediction Report (PDF)",
                data=pdf_bytes,
                file_name=f"Iris_Classification_Report_{species.replace(' ', '_')}.pdf",
                mime="application/pdf",
                type="primary",
                use_container_width=True
            )
        else:
            st.markdown("""
                <div class="saas-card" style="text-align: center; padding: 40px 20px;">
                    <h3>Ready for Botanical Inference</h3>
                    <p style="color: #64748b;">
                        Provide floral measurements on the left panel or click one of the quick presets 
                        (<b>Setosa</b>, <b>Versicolor</b>, <b>Virginica</b>) to evaluate taxon predictions.
                    </p>
                </div>
            """, unsafe_allow_html=True)
