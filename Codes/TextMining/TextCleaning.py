import string
import regex
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


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

	return re.sub(r"http\S+", "", str);





# Testin
# exampleText = "First , is a great and awesome price for quality , digital piano , this piano has a lot offer for every level of player from beginner to , accomplished players great action on the keys weight and feel which makes a huge difference when practicing scales ad chord inversions , and all around piano , the electric pianos , perfect DAW and performing live and I use this piano both ways for the price you cant go wrong . https://www.amazon.com/Roland-88-Key-E.  this piano has a lot offer for every level of player from beginner"
# print(removeStopwords(removeURL(removeUnicode(removePunctuation(exampleText)))))


