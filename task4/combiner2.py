#!/usr/bin/python2.7
# combiner2.py

import sys

#only prints the first 10 writers with highest vote for each combiner round
writers = set()
n = 0
prev_writer = None
for line in sys.stdin:
    if n<10:
        fields = line.strip().split("|")
        if fields[1] in writers:
            continue
        else:
            print line.strip()
            n = n+1
            writers.add(fields[1])