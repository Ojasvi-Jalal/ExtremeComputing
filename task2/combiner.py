#!/usr/bin/python2.7
# combiner.py

import sys

prev_tconst = None
prev_title = None

#if combination possible:
# Out: [prev_tconst+"|c|"+prev_title]
# else out: [prev_tconst+"|m|"+prev_title] or [prev_tconst+"|m"]
for line in sys.stdin:
    fields = line.strip().split("|")
    if len(fields) == 3:
        tconst = fields[0]
        title = fields[2]
        if prev_tconst == tconst:
            print(tconst+"|c|"+title)
            prev_tconst = None
            prev_title = None
        else:
            if prev_tconst != None:
                if prev_title !=None:
                    print(prev_tconst+"|m|"+prev_title)
                else:
                    print(prev_tconst+"|m")
            prev_tconst = tconst
            prev_title = title
    else:
        tconst = fields[0]
        if prev_tconst == tconst:
            print(prev_tconst+"|c|"+prev_title)
            prev_tconst = None
            prev_title = None
        else:
            if prev_tconst != None:
                if prev_title != None:
                    print(prev_tconst+"|m|"+prev_title)
                    prev_title = None
                else:
                    print(prev_tconst+"|m")
            prev_tconst = tconst

if prev_tconst is not None:
    if prev_title is not None:
        print(prev_tconst+"|m|"+prev_title)
    else:
        print(prev_tconst+"|m")