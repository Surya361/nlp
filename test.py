import pickle
import sys

def classify(data):
	defpos,defneg,pos_prob_dic,neg_prob_dic = pickle.load(open('model.p','rb'))
	pos,neg = 0,0
	for word in data:
		if(word in pos_prob_dic.keys()):
			pos = pos + pos_prob_dic[word]
		else:
			pos = pos + defpos
		if(word in neg_prob_dic.keys()):
			neg = neg + neg_prob_dic[word]
		else:
			neg = neg + defneg
	if(pos > neg):
		print "+"
	else:
		print "-"
def main():
	data = raw_input('word?')
	data = data.split(" ")
	print data
	classify(data)

main()
