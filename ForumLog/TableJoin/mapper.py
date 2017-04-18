#!/usr/bin/python

import sys
import csv

key = None

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

for line in reader:
    if len(line) == 5:
        line.insert(1, 'A')
    elif len(line) == 19:
        line = [line[3]] + line[:3] + line[5:10]
        line.insert(1, 'B')
    else:
        continue

    writer.writerow(line)
        
