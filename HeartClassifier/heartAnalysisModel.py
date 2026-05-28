# EDA and plotting libraries
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os

## ML Models
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

## Model Evaluators
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import RocCurveDisplay


# Read from csv file from local directory
df = pd.read_csv("cleaned_heart_disease_data.csv")

# Removed unwanted column that was in the dataset
df = df.drop('Unnamed: 0', axis=1)


"""
categorical_features = ["sex", "target"]
categorical_transformer = Pipeline(steps =[
    ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

numeric_features = ["age", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
numeric_transformer = Pipeline(steps =[
    ("imputer", SimpleImputer(strategy="mean"))
])

transformer = ColumnTransformer(
    transformers = [
        ("cat", categorical_transformer, categorical_features),
        ("num", numeric_transformer, numeric_features)
    ]
)

X = transformer.fit_transform(df)
feature_names = transformer.get_feature_names_out()
X_df = pd.DataFrame(X, columns=feature_names)
print(X_df)
"""