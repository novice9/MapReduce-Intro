#!/usr/bin/python

# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, id, user, time, zone, op, path, protocol, status, size = data
        time = time[1:]
        zone = zone[1:-1]
        op = op[1:]
        protocol = protocol[:-1]
        cur = 0
        while (path.find("/", cur)) != -1:
            cur = path.find("/", cur) + 1
        filename = path[cur:]
        print "{0}\t{1}".format(ip, 1)

