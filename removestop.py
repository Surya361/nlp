from sys import argv
from nltk.corpus import stopwords
import re
script, filename = argv
i=1
stop = stopwords.words("english")
txt = open(filename,'r')
pos = open('pos.txt','w')
neg = open('neg.txt','w')
voca = open('vocabluary.txt','w')
voc = []
for line in txt:
	lis = line.split()
	new = []
	for i in lis:
	#	print "%s" % (i)
		i = i.lower()
		if( i not in stop):
		#	print "checking %s" % (i)
			new.append(i)
			if (i not in voc):
				voc.append(i)
				voca.write(i)
				voca.write("\n")
				
		#	print lis
	if(new[-1] == '1'):
		new.remove('1')
		pos.write(" ".join(new))
		pos.write("\n")
	if(new[-1] == '0'):
		new.remove('0')
		neg.write(" ".join(new))
		neg.write("\n")
		
			
