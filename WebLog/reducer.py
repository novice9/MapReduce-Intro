#!/usr/bin/python

import sys

totalVisit = 0
oldIP = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisIP, thisVisit = data_mapped

    if oldIP and oldIP != thisIP:
        print oldIP, "\t", totalVisit
        totalVisit = 0

    oldIP = thisIP
    totalVisit += int(thisVisit)

if oldIP != None:
    print oldIP, "\t", totalVisit

