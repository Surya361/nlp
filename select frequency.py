from sys import argv
from nltk.corpus import stopwords
import re
script, filename = argv
i=1

txt = open(filename,'r')

#bigramvocabulary=open('bigramvocabulary.txt','w')
filteredbigramvocabulary = open('filteredbigramvocabulary.txt','w')

for line in txt:
	lis = line.split()
	new = []
	
	for i in lis:
	        new.append(i)
	
	if(new[-1] == '2'):
	        new.remove('2')
	        filteredbigramvocabulary.write(" ".join(new))
	        filteredbigramvocabulary.write("\n")


