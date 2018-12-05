import os, os.path
import re
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Print a random stanza of Gestathattr.')
parser.add_argument('-norse', nargs='+')
a = os.getcwd()
pattern = re.compile('\d')
norfile = a + '/Gestathattr.txt'
engfile = a + '/GestathattrEnglish.txt'

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
