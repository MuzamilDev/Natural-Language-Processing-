import nltk
from nltk.tag import hmm

train_data = [[("The","DT"),("dog","NN"),("barks","VB")],[("A","DT"),("cat","NN"),("meows","VB")]]

tagger = hmm.HiddenMarkovModelTrainer().train(train_data)

print(tagger.tag(["A","dog","meows"]))
