# Functions for preprocessing the text before feature extraction
# Author: Alireza

import string
import regex
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# This function removes stopwords from a text.
def remove_stopwords(str_):
	stop_words = set(stopwords.words('english'))
	word_tokens = word_tokenize(str_)

	new_str = []

	for w in word_tokens:
		if w not in stop_words:
			new_str.append(w)

	# If you want the output as an array
	# return new_str;

	# The output as a string
	return " ".join(new_str)


# This function removes the punctuations from the sentences.
def remove_punctuation(str_):
	return str_.translate(str.maketrans('', '', string.punctuation))


# This function turns a sentence to ascii code (emojies will be removed).
def remove_unicode(str_):
	return str_.encode('ascii', 'ignore').decode('utf-8')


# This function removes URL's from a text.
def remove_url(str_):
	return re.sub(r"http\S+", "", str_)

# Tokenization


# Testing
exampleText = "First , is a great and awesome price for quality , digital piano , this piano has a lot offer for every level of player from beginner to , accomplished players great action on the keys weight and feel which makes a huge difference when practicing scales ad chord inversions , and all around piano , the electric pianos , perfect DAW and performing live and I use this piano both ways for the price you cant go wrong . https://www.amazon.com/Roland-88-Key-E.  this piano has a lot offer for every level of player from beginner"
print(remove_stopwords(remove_url(remove_unicode(remove_punctuation(exampleText)))))
