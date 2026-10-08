import streamlit as st
import os
import plotly.express as px
from models.ml_engine import predict_single
from database.db_manager import log_prediction
from reports.pdf_generator import generate_prediction_pdf

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

def render_prediction_page():
    """Render real-time prediction interface built with shadcn/ui design tokens."""
    st.markdown("## Real-Time Iris Species Inference")
    st.caption("Provide floral morphological dimensions to obtain instant algorithmic taxon predictions.")
    
    col_input, col_result = st.columns([1.15, 1.35])
    
    with col_input:
        st.markdown("""
            <div class="shadcn-card">
                <div class="shadcn-card-header">
                    <span class="shadcn-card-title">Morphological Dimensions</span>
                    <span class="shadcn-card-description">Enter flower measurements or select specimen presets</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Quick presets
        st.caption("Taxonomic Sample Presets:")
        preset_cols = st.columns(3)
        if preset_cols[0].button("Setosa", use_container_width=True):
            st.session_state['input_sl'] = 5.1
            st.session_state['input_sw'] = 3.5
            st.session_state['input_pl'] = 1.4
            st.session_state['input_pw'] = 0.2
        if preset_cols[1].button("Versicolor", use_container_width=True):
            st.session_state['input_sl'] = 6.0
            st.session_state['input_sw'] = 2.9
            st.session_state['input_pl'] = 4.5
            st.session_state['input_pw'] = 1.5
        if preset_cols[2].button("Virginica", use_container_width=True):
            st.session_state['input_sl'] = 6.9
            st.session_state['input_sw'] = 3.1
            st.session_state['input_pl'] = 5.8
            st.session_state['input_pw'] = 2.1
            
        sl = st.number_input("Sepal Length (cm)", min_value=3.5, max_value=9.0, value=st.session_state.get('input_sl', 5.8), step=0.1)
        sw = st.number_input("Sepal Width (cm)", min_value=1.5, max_value=5.0, value=st.session_state.get('input_sw', 3.0), step=0.1)
        pl = st.number_input("Petal Length (cm)", min_value=0.5, max_value=8.0, value=st.session_state.get('input_pl', 4.3), step=0.1)
        pw = st.number_input("Petal Width (cm)", min_value=0.1, max_value=3.5, value=st.session_state.get('input_pw', 1.3), step=0.1)
        
        model_choice = st.selectbox(
            "Predictive Algorithm:",
            ["SVM (Tuned)", "KNN (Tuned)", "Decision Tree (Tuned)", "SVM", "KNN", "Decision Tree"]
        )
        
        predict_clicked = st.button("Run Inference", type="primary", use_container_width=True)
        
    with col_result:
        if predict_clicked:
            with st.spinner("Calculating taxonomic probabilities..."):
                pred_species, confidence, prob_dict, explanation = predict_single(
                    sl, sw, pl, pw, model_type=model_choice
                )
                
                # Save to database
                user_email = st.session_state.get('user', {}).get('email', 'analyst@iris.ai')
                log_prediction(user_email, sl, sw, pl, pw, model_choice, pred_species, confidence)
                
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
            img_file = "setosa.png"
            if "Versicolor" in species:
                img_file = "versicolor.png"
            elif "Virginica" in species:
                img_file = "virginica.png"
                
            img_path = os.path.join(ASSETS_DIR, img_file)
            
            # shadcn/ui Outcome Card
            st.markdown(f"""
                <div class="shadcn-card" style="border-left: 4px solid var(--primary, #18181b);">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div>
                            <span class="shadcn-badge shadcn-badge-default">Identified Specimen</span>
                            <div class="shadcn-card-title" style="font-size: 1.5rem !important; margin: 0.5rem 0 0.25rem 0 !important;">{species}</div>
                            <div class="shadcn-card-description">
                                Confidence Score: <b>{conf * 100:.2f}%</b> (High Reliability)
                            </div>
                        </div>
                        <span class="shadcn-badge shadcn-badge-success">Validated</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Image and explanation columns
            ic1, ic2 = st.columns([1, 1.4])
            with ic1:
                if os.path.exists(img_path):
                    st.image(img_path, caption=f"Specimen: {species}", use_container_width=True)
                else:
                    st.info(f"Specimen: {species}")
            with ic2:
                st.markdown("##### Botanical Rationale")
                st.caption(last["explanation"])
                
                # Probability distribution chart
                probs = last.get("probabilities", {})
                if probs:
                    prob_items = [{"Taxon": k, "Probability (%)": v * 100} for k, v in probs.items()]
                    fig_p = px.bar(
                        prob_items, x="Probability (%)", y="Taxon",
                        orientation="h",
                        color="Probability (%)",
                        color_continuous_scale="Viridis",
                        height=160
                    )
                    fig_p.update_layout(
                        margin=dict(l=0, r=0, t=5, b=5),
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        yaxis={'categoryorder':'total ascending'}
                    )
                    st.plotly_chart(fig_p, use_container_width=True)
                    
            # Download PDF Report button
            pdf_bytes = generate_prediction_pdf(last)
            st.download_button(
                label="Download Official Certificate (PDF)",
                data=pdf_bytes,
                file_name=f"Iris_Classification_Report_{species.replace(' ', '_')}.pdf",
                mime="application/pdf",
                type="primary",
                use_container_width=True
            )
        else:
            st.markdown("""
                <div class="shadcn-card" style="text-align: center; padding: 3rem 1.5rem !important;">
                    <div class="shadcn-card-title" style="margin-bottom: 0.5rem !important;">Awaiting Morphological Input</div>
                    <div class="shadcn-card-description">
                        Select floral dimensions or choose a preset on the left, then click <b>Run Inference</b> to evaluate species predictions.
                    </div>
                </div>
            """, unsafe_allow_html=True)
