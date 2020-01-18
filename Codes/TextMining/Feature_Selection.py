# This code will select the features and does the preprocessing on them
# Author: Alireza P. Nouri

import pandas as pd
import datetime
import TextCleaning as TC
import sklearn
import numpy as np

dataset_review = pd.read_csv("../../DataSet/Review4AmazonProducts.csv")

#print(dataset_review.columns)
# Index(['Unnamed: 0', 'name', 'reviews.date', 'reviews.didPurchase',
#        'reviews.doRecommend', 'reviews.id', 'reviews.numHelpful',
#        'reviews.rating', 'reviews.text', 'reviews.title', 'reviews.username'],
#       dtype='object')

new_date = []
date_feature = dataset_review[["reviews.date"]]

print(date_feature)
for inc in range(len(date_feature)):
    date_array = date_feature.loc[inc][0][:10].split('-')
    new_date.append(int(datetime.datetime(int(date_array[0]), int(date_array[1]), int(date_array[2])).timestamp()))

print(new_date)




