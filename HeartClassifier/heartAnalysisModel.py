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
import xgboost as xgb

## Model Evaluators
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import RocCurveDisplay


# Read from csv file from local directory
df = pd.read_csv("cleaned_heart_disease_data.csv")

#Created universal folder name variable
folder_name = 'ModelGraphs'

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Removed unwanted column that was in the dataset
df = df.drop('Unnamed: 0', axis=1)

#Everything except target variable
X = df.drop(labels="target", axis=1)

#Target variable
y = df.target.to_numpy()

#Random seed for reproducibility
np.random.seed(42)
#Split into train & test set
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2)

#Put models into a dictionary
models = {"KNN": KNeighborsClassifier(),
          "Logistic Regression": LogisticRegression(max_iter=100),
          "Random Forest": RandomForestClassifier(),
          "Xgb": xgb.XGBClassifier()}

#Create function to fit and score models
def fit_and_score(models, X_train, X_test, y_train, y_test):
    #Fits and evaluates given machine learning models
    #Random seed for reproducible results
    np.random.seed(42)
    #Make a list to keep model scores
    model_scores = {}
    #Loop through models
    for name, model in models.items():
        #Fit the model to the data
        model.fit(X_train, y_train)
        #Evaluate the model and append its score to model_scores
        model_scores[name] = model.score(X_test, y_test)
    return model_scores

model_scores = fit_and_score(models=models,
                             X_train=X_train,
                             X_test=X_test,
                             y_train=y_train,
                             y_test=y_test)

#model_compare = pd.DataFrame(model_scores, index=['accuracy'])
#model_compare.T.plot.bar()
#plt.savefig(f'{folder_name}/modelComparison.png', dpi=300)
#plt.close()

#Create a list of train scores
train_scores = []
#Create a list of test scores
test_scores = []
#Create a list of different values for n_neigbors
neighbors = range(1,21)

#Setup algorithm
#knn = KNeighborsClassifier()

#Loop through different neighbors values
#for i in neighbors:
    #knn.set_params(n_neighbors = i)

    #Fit the algorithm
    #knn.fit(X_train, y_train)

    #Update the training scores
    #train_scores.append(knn.score(X_train, y_train))

    #Update the test scores
    #test_scores.append(knn.score(X_test, y_test))

#Create plot to visualize the test and training scores
#plt.plot(neighbors, train_scores, label="Train score")
#plt.plot(neighbors, test_scores, label="Test Score")
#plt.xticks(np.arange(1, 21, 1))
#plt.xlabel("Number of neighbors")
#plt.ylabel("Model score")
#plt.legend()
#plt.savefig(f'{folder_name}/TestAndTrainScoresKNN.png', dpi=300)
#plt.close()

#print(f"Maximum KNN score on the test data: {max(test_scores)*100:.2f}%")

#Different LogisticRegression hyperparameters
log_reg_grid = {"C": np.logspace(-4, 4, 20),
                "solver": ["liblinear"]}

#Different RandomForestClassifier hyperparameters
rf_grid = {"n_estimators": np.arange(10, 1000, 50),
           "max_depth": [None, 3, 5, 10],
           "min_samples_split": np.arange(2,20,2),
           "min_samples_leaf": np.arange(1,20,2)}

#Setup random hyperparamter search for LogisticRegression
#rs_log_reg = RandomizedSearchCV(LogisticRegression(),
                                #param_distributions=log_reg_grid,
                                #cv=5,
                                #n_iter=20,
                                #verbose=True)

#Fit random hyperparameter search model
#rs_log_reg.fit(X_train, y_train)
#print(rs_log_reg.best_params_)
#print(rs_log_reg.score(X_test, y_test))

#Setup random hyperparameter search for RandomForestClassifier
rs_rf = RandomizedSearchCV(RandomForestClassifier(),
                           param_distributions=rf_grid,
                           cv=5,
                           n_iter=20,
                           verbose=True)

#Fit random hyperparameter search model
rs_rf.fit(X_train, y_train)

#Find the best parameters
print(rs_rf.best_params_)
#Evaluate the randomized search random forest model
print(rs_rf.score(X_test, y_test))
