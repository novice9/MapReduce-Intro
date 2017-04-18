#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter = '\t')
title = True
for line in reader:
    if title:
        title = False
        continue
    node = line[0]
    data = re.split(' |\.|,|!|\?|:|\;|\"|\(|\)|<|>|[|]|\#|\$|=|-|\/', line[4])
    for word in data:
        word = word.strip().lower()
        if word == '' or word == 'p':
            continue
        print "{0}\t{1}".format(word, node)

