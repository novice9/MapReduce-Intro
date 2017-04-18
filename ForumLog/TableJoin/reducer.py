#!/usr/bin/python

import sys

oldKey = None
oldValue = []

for line in sys.stdin:

    data = line.strip().split('\t') 
    thisKey, thisType, thisValue = data[0], data[1], data[2:]
    if oldKey and oldKey != thisKey:
        print oldKey, '\t', oldValue
        oldValue = []
    
    oldKey = thisKey
    if thisType == 'A':
        oldValue = oldValue + thisValue
    elif thisType == 'B':
        oldValue = thisValue + oldValue
    else:
        continue

if oldKey != None:
    print oldKey, '\t', oldValue
