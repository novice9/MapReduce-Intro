#!/usr/bin/python

import sys

totalSale = 0
noofSales = 0
oldWeekday = None

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    
    thisWeekday, thisSale = data_mapped
    if oldWeekday and oldWeekday != thisWeekday:
        meanSale = totalSale / noofSales
        print oldWeekday, '\t', meanSale
        totalSale = 0
        noofSales = 0
    
    oldWeekday = thisWeekday
    totalSale += float(thisSale)
    noofSales += 1

if oldWeekday != None:
    meanSale = totalSale / noofSales
    print oldWeekday, '\t', meanSale

