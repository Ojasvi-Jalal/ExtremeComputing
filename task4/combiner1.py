#!/usr/bin/python2.7
#combiner 2

import sys

tconst_rating = list()
tconst_nconst = list()
tconst_nconst_writer = list()

#combine and prints the votes and the writer if finds a match else prints the line as it is
for line in sys.stdin:

    line = line.strip()
    fields = line.strip().split("|")

    if len(fields) == 3:
        tconst_nconst_writer = fields
        if tconst_nconst and tconst_nconst_writer[0] == tconst_nconst[0] and tconst_nconst_writer[1] == tconst_nconst[1]:
            if tconst_nconst_writer[0] == tconst_rating[0]:
                print(tconst_rating[1] + "|" + tconst_nconst_writer[2] + "|c")
                tconst_nconst = None
                tconst_nconst_writer = None
            else:
                print(tconst_nconst_writer[0]+"|"+tconst_nconst_writer[1]+"|"+tconst_nconst_writer[2])
                tconst_nconst = None
                tconst_nconst_writer = None
        else:
            print(tconst_nconst_writer[0] + "|" + tconst_nconst_writer[1] + "|" + tconst_nconst_writer[2])
            tconst_nconst = None
            tconst_nconst_writer = None

    else:
        if fields[1].isdigit():
            print(fields[0] + "|" +fields[1])
            tconst_rating = fields
        else:
            print(fields[0] + "|" + fields[1])
            tconst_nconst = fields
