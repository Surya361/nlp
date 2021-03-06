from __future__ import division 
from sys import argv
from nltk.corpus import stopwords
import math
script, number = argv
i=1
stop = stopwords.words("english")
#pos = open('pos.txt','w')
#neg = open('neg.txt','w')
#voca = open('vocabluary.txt','w')
#j = number
def create(number):
#	print number
	j = int(number)
	j = (j+1) % 10
	pos = []
	neg = []
	voab = {}
	while(j != int(number)):
		#print "learning file",j
		fil = open(str(j),'r')
		for line in fil:
			lis = line.split()
			if (lis[-1] == '1'):
				pos = pos + lis[:-1]
			else:
				neg = neg + lis[:-1]
			for word in lis:
			#	print word
				if (word not in voab.keys() and (word != "1" or word != "0")):
					voab[word] = 1;
				else:
					voab[word] = voab[word] + 1;
		
		#print voab			
		j = (j+1)%10
		fil.close()
	for w in voab.keys():
		if(voab[w] < 2):
			del voab[w]
	return (pos,neg,voab)
			
	
def populate(filed):
	voc = []
	for i in filed:
		i = i.split()
		voc = voc + i
	return voc

def prob(word,lis,voc):
	if(word in voc.keys() and voc[word] >= 2):
		k = (lis.count(word) + 1)/(len(lis) + len(voc) )
	else:
		k = 1/(len(lis) + len(voc))
	return math.log10(k)

def classify(stri,posi,negi,v):
	stri = stri.split()
	nprob = 0
	pprob = 0
	for i in stri:
		nprob = nprob + prob(i,negi,v)
		pprob = pprob + prob(i,posi,v)
	if(nprob > pprob):
		return '0'
	else:
		return '1'

def validation(number):			
	positive,negative,vocab = create(number)
	#print positive
#vocab = populate(voca)
#positive = populate(pos)
#negative = populate(neg)
	TP = 0
	count = 0;
	test = open(number,'r')
	for line in test:
		#print line
		li = line.split()
		li = li[:-1]
		linee = " ".join(li)
	#	print linee
		res = classify(linee,positive,negative,vocab)	
		lis = line.split()
	#	print "checking",lis[-1],res
		if (lis[-1] == res):
			TP = TP + 1
		count = count + 1
	print (TP/count)*100

validation(number)
			
