import spacy
nlp = spacy.load("en_core_web_sm")
text_sentence = "NLP Prossescing. It help"
documents = nlp(text_sentence)
sentences = [text_sentence.text for text_sentence in documents.sents]
print(sentences)
