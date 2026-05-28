import pandas as pd
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder


# Read from csv file from local directory
df = pd.read_csv("heart_disease_classification_dataset.csv")

# Removed unwanted column that was in the dataset
df = df.drop('Unnamed: 0', axis=1)

#Changed the target value {'yes': 1, 'no': 0}
#df['target'] = df['target'].replace({'yes': 1, 'no': 0})

categorical_features = ["sex", "target"]
categorical_transformer = Pipeline(steps =[
    ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

numeric_features = ["age", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
numeric_transformer = Pipeline(steps =[
    ("imputer", SimpleImputer(strategy="mean"))
])

df = ColumnTransformer(
    transformers = [
        ("cat", categorical_transformer, categorical_features),
        ("num", numeric_transformer, numeric_features)
    ]
)

print(df)

#df.to_csv('cleaned_heart_disease_data.csv')