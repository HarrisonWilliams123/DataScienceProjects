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

#Create Universal Folder Name for Graphs
folder_name = 'EDAGraphs'

# Read from csv file from local directory
df = pd.read_csv("cleaned_heart_disease_data.csv")

# Removed unwanted column that was in the dataset
df = df.drop('Unnamed: 0', axis=1)

#Creates folder for the saved plot figures
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

#Prints out Normalized Value Counts
#print(df.target.value_counts(normalize=True))

#Plot the value counts with a bar graph
#df.target.value_counts().plot(kind="bar", color=["salmon", "lightblue"])
#plt.savefig(f'{folder_name}/targetValueCountsBarGraph.png', dpi=300)
#plt.close()

#Prints out the DataFrame information
#print(df.info())

#Prints out the count, mean, std, min, 25%, 50%, 75%, and max for each column
#print(df.describe())


#Compare target column with sex column
#print(pd.crosstab(index=df.target, columns=df.sex))


#Create a plot
pd.crosstab(df.target, df.sex).plot(kind="bar",
                                    figsize=(10,6),
                                    color=["salmon", "lightblue"])

plt.savefig(f'{folder_name}/targetVsSexBarPlot.png', dpi=300)
plt.close()

