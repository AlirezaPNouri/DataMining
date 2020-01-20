# This code is an exercise code to practice, try and check the functions
# Author: Alireza P. Nouri, Namrata Sharma

import pandas as pd
from DataMining.Codes.TextMining.Pre_Processing import Time_Preprocessing as tp
from DataMining.Codes.TextMining.Pre_Processing import Feature_Normalization as fnorm
from DataMining.Codes.TextMining.Pre_Processing import Text_Preprocessing as txtp

data_frame = pd.read_csv('../../DataSet/Review4AmazonProducts.csv')

# running pre processing on the data-set
# change the time format data into integer
data_set = tp.date_dey_integer(data_frame, 'reviews.date')

# Clean texts in the comments and titles
data_frame['reviews.text'] = data_frame['reviews.text'].apply(lambda str_: txtp.removeStopwords(txtp.removePunctuation(
    txtp.removeUnicode(txtp.removeURL(str_)))))
data_frame['reviews.title'] = data_frame['reviews.title'].apply(lambda str_: txtp.removeStopwords(
    txtp.removePunctuation(txtp.removeUnicode(txtp.removeURL(str_)))))
data_frame['reviews.date'] = data_frame['reviews.date'].apply(lambda dates_: fnorm.minMaxScaleFeatures(data_frame['reviews.date']))
data_frame['reviews.rating'] = data_frame['reviews.rating'].apply(lambda ratings_: fnorm.scaleFeatures(data_frame['reviews.title']))

data_frame.to_csv(r'../DataSet/NormalizedData.csv', index=None, header=True)





