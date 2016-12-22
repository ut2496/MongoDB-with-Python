import os
from pprint import pprint
list = ['']
directory = '/home/dwaipayan/Zeus/samples'
for filename in os.listdir(directory):
	if filename.endswith(".txt"):
		f = open(os.path.join(directory, filename),'r')
		str = ''
		for line in f.readlines():
			str += line
		list.append(str)
	else:
		continue
for f in list:
	pprint(list)
	print('\n')
