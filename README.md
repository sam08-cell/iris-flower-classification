# 🌸 Iris Flower Species Classification System

A production-grade, full-stack Machine Learning web application designed to classify Iris flowers into their taxonomic species (**Iris Setosa**, **Iris Versicolor**, and **Iris Virginica**) based on sepal and petal dimensions.

Built with **Python**, **Streamlit**, **Scikit-Learn**, **Pandas**, **NumPy**, **Plotly**, and **ReportLab**.

---

## 🚀 Key Features

1. **🔐 Authentication & User Management**
   - SQLite relational database (`database/iris_app.db`)
   - Salted SHA-256 password hashing
   - Login, User Registration, and Forgot Password recovery
   - Audit trail for login attempts and IP origins
   - Pre-seeded Demo Admin: `admin@iris.ai` / `Admin@123`

2. **✨ Modern SaaS Landing Page**
   - High-impact Hero banner with CTA buttons
   - Feature spotlight cards
   - Botanical context & importance of ML classification
   - Responsive Glassmorphic UI with light/dark mode toggle

3. **📊 Exploratory Data Analysis (EDA) & Data Cleaning**
   - Automated duplicate detection and missing value handling
   - Interactive Plotly visualizations:
     - Species Distribution (Donut Chart)
     - Feature Histograms & KDE with marginal box plots
     - Multi-dimensional Pair Plot scatter matrix
     - Pearson Correlation Heatmap
     - Box & Whisker dispersion plots with outlier detection
     - 2D & 3D Morphological coordinate scatter projection

4. **🎯 Feature Selection**
   - Tree-based Gini feature importance (MDI)
   - Biological rationale for Petal Length & Petal Width dominance

5. **⚡ Multi-Model Training & Benchmarking**
   - Stratified 80/20 train-test partitioning
   - Supervised models implemented and compared:
     - **K-Nearest Neighbors (KNN)**
     - **Decision Tree Classifier**
     - **Support Vector Machine (SVM)**
   - Metric evaluation: Accuracy, Precision, Recall, and F1 Score
   - Automatic highlighting of top-performing model

6. **🎛️ Hyperparameter Tuning (GridSearchCV)**
   - 5-fold cross-validated grid search
   - KNN: `n_neighbors`, `weights`
   - Decision Tree: `max_depth`, `criterion`
   - SVM: `kernel`, `C`
   - Real-time display of optimal parameters and accuracy gains

7. **🔍 Confusion Matrix & Diagnostics**
   - Interactive confusion matrix heatmaps
   - Detailed classification diagnostic reports per class

8. **🔮 Real-Time Species Inference**
   - Direct manual input or instant presets (Setosa, Versicolor, Virginica)
   - Model architecture selector
   - Predicted species, confidence score, and probability distribution
   - Botanical explanation for decision transparency
   - Specimen graphic rendering

9. **📄 Executive PDF Reporting & History**
   - Download signed, high-resolution botanical PDF certificates
   - Download model benchmark comparison PDF reports
   - Searchable, filterable inference logs stored in SQLite database with CSV export

---

## 📁 Project Architecture

```
d:/machine learnin project/
├── app.py                      # Main Streamlit web application & router
├── requirements.txt            # Python dependencies
├── README.md                   # Complete documentation
├── assets/                     # UI styles and flower graphics
│   ├── setosa.png
│   ├── versicolor.png
│   ├── virginica.png
│   └── style.py
├── authentication/             # Login, register, and password reset views
│   └── auth_views.py
├── database/                   # SQLite database manager & schemas
│   ├── db_manager.py
│   └── iris_app.db
├── dataset/                    # Dataset storage & preparation scripts
│   ├── iris.csv
│   └── prepare_data.py
├── models/                     # ML training, GridSearchCV, persistence
│   ├── ml_engine.py
│   ├── knn_default.pkl
│   ├── knn_tuned.pkl
│   ├── decision_tree_default.pkl
│   ├── decision_tree_tuned.pkl
│   ├── svm_default.pkl
│   └── svm_tuned.pkl
├── pages/                      # Modular UI views
│   ├── landing_view.py
│   ├── dataset_overview_view.py
│   ├── data_cleaning_view.py
│   ├── eda_view.py
│   ├── feature_selection_view.py
│   ├── model_training_view.py
│   ├── model_comparison_view.py
│   ├── hyperparameter_tuning_view.py
│   ├── confusion_matrix_view.py
│   ├── prediction_view.py
│   ├── reports_view.py
│   └── about_view.py
└── reports/                    # ReportLab PDF generator
    └── pdf_generator.py
```

---

## 💻 How to Run the Application

To launch the web application, open your terminal and run:

```bash
streamlit run app.py
```

Default credentials:
- **Email:** `admin@iris.ai`
- **Password:** `Admin@123`
*(Or register a new account on the registration tab)*
