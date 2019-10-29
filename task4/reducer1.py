#!/usr/bin/python2.7
# memory-efficient_reducer.py

import sys

#combine and prints the votes and the writer if there's a match
prev_tconst = None
prev_nconst = None
prev_writer = None
prev_vote = None
for line in sys.stdin:
    fields = line.strip().split("|")

    if len(fields) == 3:

        if fields[2] == "c":
            print(fields[0]+"|"+fields[2])
            continue

        tconst = fields[0]
        nconst = fields[1]
        writer = fields[2]
        if prev_tconst == tconst:
            if prev_nconst == nconst and prev_vote is not None:
                print(prev_vote + "|" + writer)
                prev_nconst = None
            elif prev_nconst != nconst:
                prev_nconst = nconst
                prev_writer = writer
            else:
                prev_writer = writer

        elif prev_tconst != fields[0]:
            prev_vote = None
            prev_tconst = tconst
            prev_nconst = nconst
            prev_writer = writer
        else:
            prev_nconst = fields[1]

    else:
        if fields[1].isdigit():
            prev_tconst = fields[0]
            prev_vote = fields[1]
            prev_nconst = None
            prev_writer = None
        else:
            if prev_tconst == fields[0]:
                prev_nconst = fields[1]
                prev_writer = None
            else:
                prev_tconst = fields[0]
                prev_nconst = fields[1]
                prev_vote = None
                prev_writer = None
