import spacy
nlp = spacy.load("en_core_web_sm")

sentence =  "NLP is fascinating"
doc = nlp(sentence)

print([(token.text,token.pos_) for token in doc])
