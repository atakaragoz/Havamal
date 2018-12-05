import os, os.path
import re
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Print a random stanza of Gestathattr.')
parser.add_argument('-norse',help="prints norse stanza instead of english",action='store_true')
args=parser.parse_args()
a = os.getcwd()
pattern = re.compile('\d')
norfile = a + '/Gestathattr.txt'
engfile = a + '/GestathattrEnglish.txt'
if args.norse:
	file = norfile
else:
	file = engfile
linenumber = []
with open(file) as opfile:
	for num, line in list(enumerate(opfile,1)):
		x = pattern.search(line)
		if x != None:
			linenumber.append(num)

opfile = open(file)
fixed = opfile.readlines()
stanzaDict = {}
for i in range(len(linenumber)-1):
	stanzaDict[i+1] = fixed[linenumber[i]-1:linenumber[i+1]-2]
stanzaNumbers = np.arange(1,80)

print('\n'.join(stanzaDict[int(np.random.choice(stanzaNumbers,1))]))
