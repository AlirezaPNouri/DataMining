# Clean the features like the titles and reviews and date and features

import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import datetime
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler


class Text_Preprocessing:
    # This function removes stopwords from a text.
    def removeStopwords(str):
        stopWords = set(stopwords.words('english'))
        wordTokens = word_tokenize(str)

        newStr = [w for w in wordTokens if not w in stopWords]

        newStr = []

        for w in wordTokens:
            if w not in stopWords:
                newStr.append(w)

        return " ".join(newStr);

    # This function removes the punctuations from the sentences.
    def removePunctuation(str_):
        return str_.translate(str.maketrans('', '', string.punctuation));

    # This function turns a sentence to ascii code (emojies will be removed).
    def removeUnicode(str):
        return str.encode('ascii', 'ignore').decode('utf-8');

    # This function removes URL's from a text.
    def removeURL(str):
        if not str:
            return re.sub(r"http\S+", "", str);
        else:
            return ''


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

    def minMaxScaleFeatures(new_date):
        dates = np.reshape(new_date, (len(new_date), 1))
        # train the normalization
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaler = scaler.fit(dates)
        # normalize the dataset and print the first 5 rows
        return scaler.transform(dates)
