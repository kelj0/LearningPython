#! /usr/bin/python3
# python pls.py this text will be changed
# changes text in ThIs tExT WiLl bE ChAnGeD

import sys

pls = ' '.join(sys.argv[1:])
ret=[]
pls.lower()
c=0
for i in pls:
	if c%2==0:ret.append(i.upper())
	else:ret.append(i)
	c+=1
print(''.join(ret))