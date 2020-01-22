# Clean the features like the titles and reviews and date and features

import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import datetime
import pandas as pd
from sklearn import preprocessing


class Text_Preprocessing:
    # This function removes stopwords from a text.
    def removeStopwords(str_):
        stopWords = set(stopwords.words('english'))
        wordTokens = word_tokenize(str_)

        newStr = []
        for w in wordTokens:
            if w not in stopWords:
                newStr.append(w)

        return " ".join(newStr)

    # This function removes the punctuations from the sentences.
    def removePunctuation(str_):
        new_str = ''
        for letter in str_:
            if letter not in string.punctuation:
                new_str += letter

        return new_str

    # This function turns a sentence to ascii code (emojies will be removed).
    def removeUnicode(str_):

        return str_.encode('ascii', 'ignore').decode('utf-8');

    # This function removes URL's from a text.
    def removeURL(str_):

        return re.sub(r"http\S+", " ", str_)


class Time_Preprocessing:
    # This function change the date from time format into the integer
    def date_dey_integer(dataframe, name):
        new_date = []
        date_feature = dataframe[[name]]
        for inc in range(len(date_feature)):
            date_array = date_feature.loc[inc][0][:10].split('-')
            new_date.append(
                int(datetime.datetime(int(date_array[0]), int(date_array[1]), int(date_array[2])).timestamp()))
        del dataframe[name]
        dataframe[name] = new_date
        return dataframe


# This code has functions to scale, normalize the numeric features
class Feature_Normalization:

    # Change the range of values for larger values
    def standardScaleFeatures(featureArray):
        return preprocessing.StandardScaler(featureArray)

    # Change the range of values
    def scaleFeatures(featureArray):
        return preprocessing.scale(featureArray)

    def minMaxScaleFeatures(dataFrameColumn):
        #df = pd.read_csv('../../DataSet/Review4AmazonProducts.csv')
        dataFrameColumn = pd.to_datetime(dataFrameColumn).astype('int64')
        max_a = dataFrameColumn.max()
        min_a = dataFrameColumn.min()
        min_norm = -1
        max_norm = 1
        dataFrameColumn = (dataFrameColumn - min_a) * (max_norm - min_norm) / (max_a - min_a) + min_norm
        return dataFrameColumn

