from sys import argv
from nltk.corpus import stopwords
import re
import nltk

f = open('removedstopwordsandlables.txt')
raw = f.read()

tokens = nltk.word_tokenize(raw)

#Create your bigrams
bgs = nltk.bigrams(tokens)

#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)
for k,v in fdist.items():
    print k,v
