from sys import argv
import nltk
import re
#script, filename = argv
k=0
pos = open("pos.txt",'r')
neg = open("neg.txt",'r')
while(k != 10):
	fil = open(str(k),'w')
	i=0
	j=0
	while(i != 80):
		line = pos.readline()
		lis = line.split()
		lis.append("1")
		line = " ".join(lis)
		fil.write(line)
		fil.write("\n")
		line = neg.readline()
		lis = line.split()
		lis.append("0")
		line = " ".join(lis)
		fil.write(line)
		fil.write("\n")
		i = i+1
	fil.close()
	k=k+1
