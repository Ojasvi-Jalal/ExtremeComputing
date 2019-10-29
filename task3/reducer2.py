#!/usr/bin/python2.7
# memory-efficient_reducer.py

import sys

#prints the top rated movie of each genre between 1990 and 1999
pre_Decade = ""
pre_Genre = ""
for line in sys.stdin: #"Decade|Genre|Title|Rating"
    fields = line.strip().split("|")

    decade  = fields[0]
    genre   = fields[1]
    rating  = fields[2]
    title   = fields[3]

    if pre_Decade == decade and pre_Genre == genre:
        continue
    else:
        print(decade+"|"+genre+"|"+title)
        pre_Decade = decade
        pre_Genre = genre