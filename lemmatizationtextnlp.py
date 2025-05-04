import spacy
nlp = spacy.load("en_core_web_sm")
text = "running flies copying easily studies"
documents = nlp(text)
lemma = [token.lemma_ for token in documents]
print(lemma)
