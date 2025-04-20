import re
def normalize_text(text):
  text= text.lower()
  text= re.sub(r"[^a-zA-Z0-9\s]","",text) #remove special character
  text= re.sub(r"\s+"," ",text).strip() #remove extra spaces
  return text
  text="Hellom NLP! This is basic Text-Normalization Example."
  print(normalize_text(text))
