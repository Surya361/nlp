from sys import argv
import nltk
import re
script, filename = argv
i=1
txt = open(filename)
for line in txt:
	lis = line.split()
	num = lis[1]
	if (int(num) >= i):
		data =  " ".join(lis[2:])
		data = re.sub('[!@#$,\.\)\(\:\;\"?\-\'%&*\/]', '', data)
		data = data.split()
		if  int(data[-1]) == 4:
			data[-1] = "1"
			print " ".join(data)
		elif( int(data[-1]) == 0):
			data[-1] = "0"
			print " ".join(data)

		i = i+1
