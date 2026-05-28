import pandas as pd

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

#df.to_csv('cleaned_heart_disease_data.csv')