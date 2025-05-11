import nltk
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")

sentence = "The quick brown fox jumps over the lazy dog."
words = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(words)

print(pos_tags)
