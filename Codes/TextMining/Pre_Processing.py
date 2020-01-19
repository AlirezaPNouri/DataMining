# Clean the features like the titles and reviews and date and features

import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import datetime



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
