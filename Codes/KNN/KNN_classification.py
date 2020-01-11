# This code explains and elaborates the KNN classification.
# Author: Alireza P. Nouri
from typing import List

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from tensorflow_core.python.ops.gen_clustering_ops import nearest_neighbors

dataset_diabetes = pd.read_csv('../../DataSet/DiabetesDataset')

# To get the size of the database and check the values in the dataset
# print(dataset_diabetes.shape)
# print(dataset_diabetes.head())

# To split the data into training, validation, and testing set
# Separate The file into features and labels
features_data = dataset_diabetes[dataset_diabetes.columns[:8]]
labels_data = dataset_diabetes[dataset_diabetes.columns[8]]

# Create train, test, and validation sets
X_trainData = features_data.loc[:499]
X_validateData = features_data.loc[500:567]
X_testData = features_data.loc[568:]

y_trainData = labels_data.loc[:499]
y_validateData = labels_data.loc[500:567]
y_testData = labels_data.loc[568:]

nNeighbors_accuracy = []
for i in range(7):
    # Create KNN classifier model with 3 neighbors
    knn_model = KNeighborsClassifier(n_neighbors=2 * i + 1)

    # Fit the classifier to the training data
    knn_model.fit(X_trainData, y_trainData)

    knn_predict = knn_model.predict(X_validateData)

    # run confusion matrix to check the results
    # print(confusion_matrix(y_validateData, knn_predict))

    # Another way to calculate the accuracy
    nNeighbors_accuracy.append(knn_model.score(X_validateData, y_validateData))
# Choosing the best n neighbors
n_neighbors = nNeighbors_accuracy.index(max(nNeighbors_accuracy))
nNeighbor = 2*n_neighbors + 1
knn_finalModel = KNeighborsClassifier(n_neighbors=nNeighbor)
knn_finalModel.fit(X_trainData, y_trainData)
print(knn_finalModel.score(X_testData, y_testData))

# print(X_trainData.shape)
# print(X_validateData.shape)
# print(X_testData.shape)
#


print('Program runs without any problem')
