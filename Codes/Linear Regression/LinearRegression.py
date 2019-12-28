# This code implenets a linear regression in python
# Code Source : https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html

import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Use only one feature
diabetes_X = diabetes_X[:,np.newaxis,2]

# Split the data into training and testing set
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the target into training and testing set
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training set
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# Results

# The coeficients
print('Coeficients: \n', regr.coef_)

# The mean squared error
print('Mean squared error: %2f' % r2_score(diabetes_y_test,diabetes_y_pred) )

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test, color = 'black')
plt.plot(diabetes_X_test, diabetes_y_pred, color = 'red')

plt.xticks(())
plt.yticks(())

plt.show()