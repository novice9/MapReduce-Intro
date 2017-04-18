#!/usr/bin/python

import sys

totalVisit = 0
oldPath = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisPath, thisVisit = data_mapped

    if oldPath and oldPath != thisPath:
        print oldPath, "\t", totalVisit
        totalVisit = 0

    oldPath = thisPath
    totalVisit += int(thisVisit)

if oldPath != None:
    print oldPath, "\t", totalVisit

