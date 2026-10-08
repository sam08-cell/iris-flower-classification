import pandas as pd
from sklearn.datasets import load_iris
import os

def prepare_iris_dataset():
    data = load_iris(as_frame=True)
    df = data.frame
    
    # Rename columns to standard readable names
    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target']
    
    # Map species name
    species_map = {0: 'Iris Setosa', 1: 'Iris Versicolor', 2: 'Iris Virginica'}
    df['species'] = df['target'].map(species_map)
    
    csv_path = os.path.join(os.path.dirname(__file__), 'iris.csv')
    df.to_csv(csv_path, index=False)
    print(f"Iris dataset saved to {csv_path} with shape {df.shape}")

if __name__ == '__main__':
    prepare_iris_dataset()
