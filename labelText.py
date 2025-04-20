import spacy
nlp = spacy.load("en_core_web_sm")
text = "Apple is looking at buying U.K startup for $1 billion"
doc = nlp(text)
for entity in doc.ents:
  print(entity.text, entity.label_)
