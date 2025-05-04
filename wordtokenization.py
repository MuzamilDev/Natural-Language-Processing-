import spacy
nlp = spacy.load("en_core_web_sm")
text ="tokenization is crucial for NLP!"
documents = nlp(text)
tokens = [token.text for token in documents]
print(tokens)
