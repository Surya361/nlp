from __future__ import division 
from sys import argv
from nltk.corpus import stopwords
import math
import nltk

script, number = argv
i=1
stop = open('stopwords.txt','r')
#pos = open('pos.txt','w')
#neg = open('neg.txt','w')
#voca = open('vocabluary.txt','w')
#j = number
# from bigramvocabulary import get_bigram_list
def get_bigram_list(fname):
	f = open(fname)
	raw = f.read()
	#print raw
	tokens = nltk.word_tokenize(raw)
	bgs = nltk.bigrams(tokens)
	fdist = nltk.FreqDist(bgs)
#print fdist.str()
	#for k,v in fdist.items():
		#print k,v
	return fdist
def create(number):
#   print number
    j = int(number)
    j = (j+1) % 10
    pos = []
    neg = []
    voab = {}
    train_pos = open('train_pos.txt','w')
    train_neg = open('train_neg.txt','w')
    train_file = open('train_file.txt','w')
    while(j != int(number)):
        #print "learning file",j
        fil = open(str(j),'r')
        for line in fil:
            lis = line.split()
            if (lis[-1] == '1'):
                train_file.write(" ".join(lis[:-1]))
                train_pos.write(" ".join(lis[:-1]))
                train_pos.write("\n")
                pos = pos + lis[:-1]
            else:
                neg = neg + lis[:-1]
                train_file.write(" ".join(lis[:-1]))
                train_neg.write(" ".join(lis[:-1]))
                train_neg.write("\n")
            for word in lis:
			#	print word
				if (word not in voab.keys() and (word != "1" or word != "0")):
					voab[word] = 1;
				else:
					voab[word] = voab[word] + 1;
        j = (j+1)%10
        fil.close()
	for w in voab.keys():
		if(voab[w] < 2):
			del voab[w]
    train_pos.close()
    train_neg.close()

    pbfl = get_bigram_list('train_pos.txt')
    nbfl = get_bigram_list('train_neg.txt')
    tbfl = get_bigram_list('train_file.txt')

    #for k,l in 

    voc_size= len([w for w in tbfl if tbfl[w] >= 2])
    #print voc_size



    return (pos,neg,voab,pbfl,nbfl,voc_size)
            
    
def populate(filed):
    voc = []
    for i in filed:
        i = i.split()
        voc = voc + i
    return voc

def prob(bigram,wl,wl1,bfl,n):

	#print wl
	if(bfl[bigram]>=3):
		#print bigram,bfl[bigram]
		val=bfl[bigram]
		k = (val+1)/(wl.count(bigram[0])+n-bfl[bigram])
        #print "bigram"
        #print bigram[0]
	elif(bigram[1] in wl1.keys() and wl1[bigram[1]] >= 2):
		k = (wl.count(bigram[1]) + 1)/(len(wl) +  len(wl1) )
	else:
		k = 1/(len(wl) + len(wl1))
	return math.log10(k)

def str_to_bigrams(doc):
	doc = doc.split()
	bigrams = []
	bigrams.append(('*',doc[0]))
	bigrams.append((doc[-1],'**'))
	for i in range(len(doc)-1):
		abigram = (doc[i],doc[i+1])
		#print abigram
		bigrams.append(abigram)
	return bigrams

def classify(stri,posi,negi,pbfl,nbfl,n,v):
    nprob,pprob=0,0
    bigrams = str_to_bigrams(stri)
    for i in bigrams:
        nprob = nprob + prob(i,negi,v,nbfl,n)
        pprob = pprob + prob(i,posi,v,pbfl,n)
    if(nprob > pprob):
        return '0'
    else:
        return '1'

def validation(number):         
    positive,negative,vocab,pbfl,nbfl,n = create(number)
    #print pbfl
   # for k,v in pbfl:
    #    print k,v	
    #print positive
#vocab = populate(voca)
#positive = populate(pos)
#negative = populate(neg)
    n = len(vocab)
    TP = 0
    count = 0;
    test = open(number,'r')
    for line in test:
        
        li = line.split()
       # print li
        li = li[:-1]
        #print li
        linee = " ".join(li)
        res = classify(linee,positive,negative,pbfl,nbfl,n,vocab)   
        lis = line.split()
    #   print "checking",lis[-1],res
        if (lis[-1] == res):
            TP = TP + 1
        count = count + 1
    print (TP/count)*100

validation(number)
            
