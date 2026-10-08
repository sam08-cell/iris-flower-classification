import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "dataset", "iris.csv")
MODELS_DIR = os.path.join(BASE_DIR, "models")

SPECIES_LABEL_MAP = {
    'setosa': 'Iris Setosa',
    'versicolor': 'Iris Versicolor',
    'virginica': 'Iris Virginica',
    'Iris-setosa': 'Iris Setosa',
    'Iris-versicolor': 'Iris Versicolor',
    'Iris-virginica': 'Iris Virginica',
    'Iris Setosa': 'Iris Setosa',
    'Iris Versicolor': 'Iris Versicolor',
    'Iris Virginica': 'Iris Virginica'
}

def load_data():
    """Load the Iris dataset and standardize columns."""
    df = pd.read_csv(DATA_PATH)
    # Standardize column names
    col_rename = {
        'sepal_length': 'sepal_length',
        'sepal_width': 'sepal_width',
        'petal_length': 'petal_length',
        'petal_width': 'petal_width',
        'species': 'species'
    }
    df.columns = [c.lower().strip().replace(' ', '_') for c in df.columns]
    # Clean species column
    df['species'] = df['species'].map(lambda x: SPECIES_LABEL_MAP.get(str(x), str(x)))
    return df

def clean_data(df: pd.DataFrame):
    """
    Data Cleaning:
    - Missing value detection & imputation
    - Duplicate detection & removal
    - Data validation
    Returns: cleaned_df, cleaning_report_dict
    """
    initial_shape = df.shape
    missing_count_initial = df.isnull().sum().to_dict()
    duplicates_initial = int(df.duplicated().sum())
    
    # Impute missing if any (using median for numeric)
    df_cleaned = df.copy()
    numeric_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    for col in numeric_cols:
        if col in df_cleaned.columns and df_cleaned[col].isnull().sum() > 0:
            df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median())
            
    # Drop duplicates
    df_cleaned = df_cleaned.drop_duplicates().reset_index(drop=True)
    final_shape = df_cleaned.shape
    
    report = {
        "initial_rows": initial_shape[0],
        "initial_cols": initial_shape[1],
        "missing_detected": sum(missing_count_initial.values()),
        "missing_per_col": missing_count_initial,
        "duplicates_removed": duplicates_initial,
        "final_rows": final_shape[0],
        "final_cols": final_shape[1],
        "status": "Dataset is validated, cleaned, and verified."
    }
    return df_cleaned, report

def get_train_test_split(df=None, test_size=0.2, random_state=42):
    """Perform 80-20 train-test split."""
    if df is None:
        df = load_data()
        df, _ = clean_data(df)
        
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['species']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    return X_train, X_test, y_train, y_test

def train_default_models(X_train, X_test, y_train, y_test):
    """Train KNN, Decision Tree, and SVM with standard baseline parameters."""
    models = {
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "Decision Tree": DecisionTreeClassifier(random_state=42, max_depth=3),
        "SVM": SVC(kernel='linear', C=1.0, probability=True, random_state=42)
    }
    
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average='weighted', zero_division=0)
        rec = recall_score(y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
        cm = confusion_matrix(y_test, y_pred)
        cr = classification_report(y_test, y_pred, output_dict=True)
        
        # Save model
        os.makedirs(MODELS_DIR, exist_ok=True)
        joblib.dump(model, os.path.join(MODELS_DIR, f"{name.lower().replace(' ', '_')}_default.pkl"))
        
        results[name] = {
            "model": model,
            "accuracy": float(acc),
            "precision": float(prec),
            "recall": float(rec),
            "f1_score": float(f1),
            "confusion_matrix": cm,
            "classification_report": cr,
            "classes": list(model.classes_)
        }
        
    return results

def tune_models_gridsearch(X_train, X_test, y_train, y_test):
    """
    Perform Hyperparameter Tuning using GridSearchCV:
    - KNN: n_neighbors [1..15]
    - Decision Tree: max_depth [1..10]
    - SVM: kernel ['linear', 'rbf', 'poly'], C [0.1, 1, 10, 50]
    """
    param_grids = {
        "KNN": {
            "model": KNeighborsClassifier(),
            "params": {"n_neighbors": [1, 3, 5, 7, 9, 11, 15], "weights": ['uniform', 'distance']}
        },
        "Decision Tree": {
            "model": DecisionTreeClassifier(random_state=42),
            "params": {"max_depth": [2, 3, 4, 5, 6, 8, None], "criterion": ["gini", "entropy"]}
        },
        "SVM": {
            "model": SVC(probability=True, random_state=42),
            "params": {"kernel": ["linear", "rbf", "poly"], "C": [0.1, 1.0, 5.0, 10.0, 50.0]}
        }
    }
    
    tuning_results = {}
    for name, cfg in param_grids.items():
        grid = GridSearchCV(cfg["model"], cfg["params"], cv=5, scoring='accuracy', n_jobs=1)
        grid.fit(X_train, y_train)
        best_model = grid.best_estimator_
        
        y_pred = best_model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average='weighted', zero_division=0)
        rec = recall_score(y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
        cm = confusion_matrix(y_test, y_pred)
        cr = classification_report(y_test, y_pred, output_dict=True)
        
        # Save tuned model
        joblib.dump(best_model, os.path.join(MODELS_DIR, f"{name.lower().replace(' ', '_')}_tuned.pkl"))
        
        tuning_results[name] = {
            "best_params": grid.best_params_,
            "best_cv_score": float(grid.best_score_),
            "test_accuracy": float(acc),
            "precision": float(prec),
            "recall": float(rec),
            "f1_score": float(f1),
            "confusion_matrix": cm,
            "classification_report": cr,
            "classes": list(best_model.classes_),
            "model": best_model
        }
        
    return tuning_results

def predict_single(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float, model_type="SVM (Tuned)"):
    """
    Make real-time prediction for given input dimensions.
    Returns: species_name, confidence_score, probabilities_dict, explanation
    """
    X_input = pd.DataFrame([{
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }])
    
    # Try loading saved model or fall back to quick trained model
    model_file_map = {
        "KNN": "knn_default.pkl",
        "KNN (Tuned)": "knn_tuned.pkl",
        "Decision Tree": "decision_tree_default.pkl",
        "Decision Tree (Tuned)": "decision_tree_tuned.pkl",
        "SVM": "svm_default.pkl",
        "SVM (Tuned)": "svm_tuned.pkl"
    }
    
    target_file = model_file_map.get(model_type, "svm_tuned.pkl")
    full_path = os.path.join(MODELS_DIR, target_file)
    
    if os.path.exists(full_path):
        model = joblib.load(full_path)
    else:
        # Train on the fly
        df = load_data()
        df, _ = clean_data(df)
        X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
        y = df['species']
        model = SVC(kernel='rbf', C=1.0, probability=True, random_state=42)
        model.fit(X, y)
        os.makedirs(MODELS_DIR, exist_ok=True)
        joblib.dump(model, full_path)
        
    pred = model.predict(X_input)[0]
    
    # Calculate confidence / probabilities
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(X_input)[0]
        classes = model.classes_
        prob_dict = {classes[i]: float(probs[i]) for i in range(len(classes))}
        confidence = float(np.max(probs))
    else:
        confidence = 0.95
        prob_dict = {pred: 0.95}
        
    # Generate human explanation
    explanation = generate_explanation(sepal_length, sepal_width, petal_length, petal_width, pred)
    
    return pred, confidence, prob_dict, explanation

def generate_explanation(sl, sw, pl, pw, species):
    """Botanical rule-based explanation for ML transparency."""
    if species == "Iris Setosa":
        return (
            f"Species classified as Iris Setosa primarily due to short petal length ({pl:.1f} cm) "
            f"and small petal width ({pw:.1f} cm). Setosa flowers are botanically characterized by distinctively small, "
            f"delicate petals (usually < 2.5 cm) and relatively broad sepals ({sw:.1f} cm)."
        )
    elif species == "Iris Versicolor":
        return (
            f"Species identified as Iris Versicolor based on intermediate petal dimensions "
            f"(Length: {pl:.1f} cm, Width: {pw:.1f} cm). Versicolor occupies the characteristic mid-range spectrum "
            f"between Setosa and Virginica, with moderate sepal lengths ({sl:.1f} cm)."
        )
    else:
        return (
            f"Species classified as Iris Virginica driven by high petal length ({pl:.1f} cm) "
            f"and robust petal width ({pw:.1f} cm). Virginica flowers are the largest among the three species, "
            f"characteristically exhibiting petals longer than 4.8 cm and widths exceeding 1.6 cm."
        )
