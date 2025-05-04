import nltk
nltk.download("punkt_tab")
nltk.download("punkt")

from nltk.tokenize import word_tokenize, sent_tokenize
text="Natural Language processing is Amazing! It enables machines to understand text."
print("Word tokens:", word_tokenize(text))
print("Sentence tokens:", sent_tokenize(text))
