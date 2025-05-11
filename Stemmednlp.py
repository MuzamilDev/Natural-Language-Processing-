from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

words = ['running', 'flies','easily','studies']
stemm_words = [stemmer.stem(word) for word in words]

print("Stemmed Words:", stemm_words)
