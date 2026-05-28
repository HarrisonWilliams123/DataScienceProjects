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

#Changed the target value {'yes': 1, 'no': 0} for EDA
df['target'] = df['target'].replace({'yes': 1, 'no': 0})
#Changed the sex value {'male': 1, 'female': 0} for EDA
df['sex'] = df['sex'].replace({'male': 1, 'female': 0})
#Fills the missing values with the mean value for numeric columns
df = df.fillna(df.mean(numeric_only=True))

print(df)

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
df.to_csv('cleaned_heart_disease_data.csv')