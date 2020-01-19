# This code has functions to scale, normalize the numeric features
# Author: Namrata Sharma

import pandas as pd
import numpy as np
import datetime
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler

dataset_review = pd.read_csv("../../DataSet/Review4AmazonProducts.csv")

new_date = []
date_feature = dataset_review[["reviews.date"]]

print(date_feature)
for inc in range(len(date_feature)):
    date_array = date_feature.loc[inc][0][:10].split('-')
    new_date.append(int(datetime.datetime(int(date_array[0]), int(date_array[1]), int(date_array[2])).timestamp()))

print(new_date)

#Change the range of values for larger values
def standardScaleFeatures(featureArray):
    scaledFeatures = preprocessing.StandardScaler(featureArray)

#Change the range of values
def scaleFeatures(featureArray):
    scaledFeatures = preprocessing.scale(featureArray)

def minMaxScaleFeatures(new_date):
    values = np.reshape(new_date, (len(new_date),1))
# train the normalization
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler = scaler.fit(values)
    print('Min: %f, Max: %f' % (scaler.data_min_, scaler.data_max_))
# normalize the dataset and print the first 5 rows
    normalized = scaler.transform(values)
    for i in range(5):
	    print(normalized[i])













