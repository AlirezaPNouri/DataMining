# This code implements a Logistic regression in python
# Author: Alireza Nouri 

import pandas as pd
import matplotlib.pyplot as plt


import numpy as np


path = ""+"Review4AmazonProducts.csv"

df = pd.read_csv(path, usecols=['name', 'reviews.date', 'reviews.didPurchase', 'reviews.doRecommend', 'reviews.id', 
       'reviews.numHelpful', 'reviews.rating', 
       'reviews.text', 'reviews.title', 'reviews.username'], skipinitialspace=True )


# Get histogram from some features like Number of helpful reviews, reviews rating, reviews' username.

df[['reviews.rating']].plot(kind='hist', bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5], rwidth=0.8)
plt.title("Histogram of Number of Reviews' Rating")
plt.show()

df[['reviews.numHelpful']].plot(kind='hist', bins=[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 
	12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 
	31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5]
, rwidth=0.5)
plt.title("Histogram of Number of Helpful Reviews")
plt.show()


# Plot the histogram of the first 20 most frequent name of the products
df['name'].value_counts()[:20].plot(kind='bar')
plt.title("Histogram of Products name")
plt.show()


# Save the new CSV file
# df.to_csv(""+'Review4AmazonProducts.csv')

