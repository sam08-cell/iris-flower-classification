import streamlit as st
import pandas as pd
from models.ml_engine import get_train_test_split, tune_models_gridsearch, train_default_models

def render_hyperparameter_tuning(df: pd.DataFrame):
    """Render Hyperparameter Tuning dashboard using GridSearchCV."""
    st.markdown("## 🎛️ Hyperparameter Tuning with GridSearchCV")
    st.caption("Exhaustive cross-validated grid search across hyperparameter combinations for KNN, Decision Tree, and SVM.")
    
    # Check baseline results
    if 'default_results' not in st.session_state:
        X_train, X_test, y_train, y_test = get_train_test_split(df)
        st.session_state['default_results'] = train_default_models(X_train, X_test, y_train, y_test)
        st.session_state['test_split_info'] = (X_train, X_test, y_train, y_test)
    else:
        X_train, X_test, y_train, y_test = st.session_state['test_split_info']
        
    st.markdown("""
        <div class="saas-card">
            <h4>GridSearchCV Optimization Spaces</h4>
            <ul>
                <li><b>KNN:</b> <code>n_neighbors</code> ∈ [1, 3, 5, 7, 9, 11, 15] & <code>weights</code> ∈ ['uniform', 'distance']</li>
                <li><b>Decision Tree:</b> <code>max_depth</code> ∈ [2, 3, 4, 5, 6, 8, None] & <code>criterion</code> ∈ ['gini', 'entropy']</li>
                <li><b>SVM:</b> <code>kernel</code> ∈ ['linear', 'rbf', 'poly'] & <code>C</code> ∈ [0.1, 1.0, 5.0, 10.0, 50.0]</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("⚡ Run GridSearchCV Optimization", type="primary", use_container_width=True):
        with st.spinner("Executing 5-fold cross-validation grid search across all parameter combinations..."):
            tuned_results = tune_models_gridsearch(X_train, X_test, y_train, y_test)
            st.session_state['tuned_results'] = tuned_results
            st.success("🎯 Hyperparameter Tuning Completed Successfully!")
            
    # Load tuned results if already calculated
    if 'tuned_results' not in st.session_state:
        with st.spinner("Initializing optimal hyperparameter search..."):
            st.session_state['tuned_results'] = tune_models_gridsearch(X_train, X_test, y_train, y_test)
            
    tuned_results = st.session_state['tuned_results']
    default_results = st.session_state['default_results']
    
    st.markdown("### 🔍 Optimal Parameter Results & Accuracy Delta")
    
    t_knn, t_dt, t_svm = st.columns(3)
    
    with t_knn:
        st.markdown('<div class="saas-card">', unsafe_allow_html=True)
        st.markdown("#### KNN (Tuned)")
        knn_tuned = tuned_results["KNN"]
        knn_base_acc = default_results["KNN"]["accuracy"]
        knn_new_acc = knn_tuned["test_accuracy"]
        delta = (knn_new_acc - knn_base_acc) * 100
        
        st.markdown(f"**Best Parameters:**")
        st.code(str(knn_tuned["best_params"]), language="json")
        st.metric("Test Accuracy", f"{knn_new_acc*100:.2f}%", f"{delta:+.2f}% vs Baseline")
        st.caption(f"Cross-Validation Best Score: {knn_tuned['best_cv_score']*100:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with t_dt:
        st.markdown('<div class="saas-card">', unsafe_allow_html=True)
        st.markdown("#### Decision Tree (Tuned)")
        dt_tuned = tuned_results["Decision Tree"]
        dt_base_acc = default_results["Decision Tree"]["accuracy"]
        dt_new_acc = dt_tuned["test_accuracy"]
        delta = (dt_new_acc - dt_base_acc) * 100
        
        st.markdown(f"**Best Parameters:**")
        st.code(str(dt_tuned["best_params"]), language="json")
        st.metric("Test Accuracy", f"{dt_new_acc*100:.2f}%", f"{delta:+.2f}% vs Baseline")
        st.caption(f"Cross-Validation Best Score: {dt_tuned['best_cv_score']*100:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with t_svm:
        st.markdown('<div class="saas-card">', unsafe_allow_html=True)
        st.markdown("#### SVM (Tuned)")
        svm_tuned = tuned_results["SVM"]
        svm_base_acc = default_results["SVM"]["accuracy"]
        svm_new_acc = svm_tuned["test_accuracy"]
        delta = (svm_new_acc - svm_base_acc) * 100
        
        st.markdown(f"**Best Parameters:**")
        st.code(str(svm_tuned["best_params"]), language="json")
        st.metric("Test Accuracy", f"{svm_new_acc*100:.2f}%", f"{delta:+.2f}% vs Baseline")
        st.caption(f"Cross-Validation Best Score: {svm_tuned['best_cv_score']*100:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)
        
    # Summary Table
    st.subheader("📊 Post-Tuning Comparison Summary")
    summary_data = []
    for model_name in ["KNN", "Decision Tree", "SVM"]:
        summary_data.append({
            "Model": model_name,
            "Baseline Acc": f"{default_results[model_name]['accuracy']*100:.2f}%",
            "Tuned Test Acc": f"{tuned_results[model_name]['test_accuracy']*100:.2f}%",
            "Optimal Parameters": str(tuned_results[model_name]['best_params']),
            "5-Fold CV Accuracy": f"{tuned_results[model_name]['best_cv_score']*100:.2f}%"
        })
    st.dataframe(pd.DataFrame(summary_data), use_container_width=True)
