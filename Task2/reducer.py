#!/usr/bin/python2.7
# memory-efficient_reducer.py
import sys

l = set()
for line in sys.stdin:
    line = line.strip()
    tconst, title = line.split("|")
    if(tconst in l):
        if(title != ""):
            print(title)
        else:
            continue
    else:
        l.add(tconst)