#!/usr/bin/python2.7
# mapper.py

import sys

#prints the first 10 writers with highest vote
#avoids duplicate writers
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
