#!/usr/bin/python

import sys

mostVisit = 0
topFile = None
totalVisit = 0
oldFile = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisFile, thisVisit = data_mapped

    if oldFile and oldFile != thisFile:
        if mostVisit < totalVisit:
            mostVisit = totalVisit
            topFile = oldFile
        totalVisit = 0

    oldFile = thisFile
    totalVisit += int(thisVisit)

if oldFile != None:
    if mostVisit < totalVisit:
            mostVisit = totalVisit
            topFile = oldFile

print topFile, "\t", mostVisit

