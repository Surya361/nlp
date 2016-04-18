from __future__ import division 
from sys import argv
from nltk.corpus import stopwords
import math
import pickle
#script, number = argv
i=1
stop = stopwords.words("english")
#pos = open('pos.txt','w')
#neg = open('neg.txt','w')
#voca = open('vocabluary.txt','w')
#j = number
def create():
#	print number
	j = 0
	pos = []
	neg = []
	voab = []
	while(j != 10):
		print "learning file",j
		fil = open(str(j),'r')
		for line in fil:
			
			lis = line.split()
			if (lis[-1] == '1'):
				pos = pos + lis[:-1]
			else:
				neg = neg + lis[:-1]
			for word in lis:
				if (word not in voab and (word != "1" or word != "0")):
					voab.append(word)
		j = (j+1)
		fil.close()
	return (pos,neg,voab)
			
	
def populate(filed):
	voc = []
	for i in filed:
		i = i.split()
		voc = voc + i
	return voc

def prob(word,lis,vocab):
	k = (lis.count(word) + 1)/(len(lis) + len(vocab) )
#	print lis.count(word)
#	print (len(lis) + len(set(lis)))
#	print k
	return math.log10(k)

def train():
	ps_prob_dic = {}
	neg_prob_dic = {}
	pos,neg,v = create()
	for line in v:
#		print line
		pprob = prob(line,pos,neg)
		nprob = prob(line,neg,pos)
		ps_prob_dic[line] = pprob
		neg_prob_dic[line] = nprob
#	print ps_prob_dic
	defaultpos = math.log10(1/((len(pos))+len(v)))
	defaultneg = math.log10(1/((len(neg))+len(v)))
	var = defaultpos,defaultneg,ps_prob_dic,neg_prob_dic
	pickle.dump(var,open("model.p","wb"))

train()

			
