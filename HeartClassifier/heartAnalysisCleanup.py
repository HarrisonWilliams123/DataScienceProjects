import pandas as pd

# Read from csv file from local directory
df = pd.read_csv("heart_disease_classification_dataset.csv")

# Removed unwanted column that was in the dataset
df = df.drop('Unnamed: 0', axis=1)

#Changed the target value {'yes': 1, 'no': 0}
df['target'] = df['target'].replace({'yes': 1, 'no': 0})

df.to_csv('cleaned_heart_disease_data.csv')