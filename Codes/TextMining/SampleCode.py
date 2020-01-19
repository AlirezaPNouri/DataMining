# This code is a excercise code to practice, try and check the functions
# Author: Alireza P. Nouri

import pandas as pd
from Pre_Processing import Time_Preprocessing as tp
from Pre_Processing import Text_Preprocessing as txtp

data_frame = pd.read_csv('../../DataSet/Review4AmazonProducts.csv')

# running pre processing on the data-set
# change the time format data into integer
data_set = tp.date_dey_integer(data_frame, 'reviews.date')

# Clean textes in the comments and titles
data_frame['reviews.text'] = data_frame['reviews.text'].apply(lambda str_: txtp.removeStopwords(txtp.removePunctuation(
    txtp.removeUnicode(txtp.removeURL(str_)))))
data_frame['reviews.title'] = data_frame['reviews.title'].apply(lambda str_: txtp.removeStopwords(
    txtp.removePunctuation(txtp.removeUnicode(txtp.removeURL(str_)))))


