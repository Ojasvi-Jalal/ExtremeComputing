#!/usr/bin/python2.7
# memory-efficient_reducer.py
import sys

#out: [title:str]
prev_tconst = None
prev_title = None
for line in sys.stdin:
    fields = line.strip().split("|")

    #the entry had already been combines, print and continue
    if fields[1] == "c":
        print(fields[2])
        continue

    else:
        if len(fields) == 3:
            tconst = fields[0]
            title = fields[2]
            if prev_tconst == fields[0]:
                print(title)
                prev_tconst = None
                prev_title = None
            else:
                prev_tconst = fields[0]
                prev_title = fields[2]

        else:
            tconst = fields[0]
            if prev_tconst == tconst:
                print(prev_title)
                prev_tconst = None
                prev_title = None
            else:
                prev_tconst = tconst