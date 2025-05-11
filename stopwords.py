
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

words =["This",'is',"a","simple","example","of","stopword","removel"]
filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]

print("Filtered Words:", filtered_words)
