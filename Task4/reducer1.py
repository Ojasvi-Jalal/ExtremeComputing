#!/usr/bin/python2.7
# memory-efficient_reducer.py
#cat title.basics.tsv | ./mapper.py | sort -t'|' -k./reducer.py

import sys

a  = "tt8347882|70\ntt8347882|nm1913625\ntt8347882|nm1913625|Dipankar Sarkar"
prev_tconst = None
prev_nconst = None
vote = None
for line in sys.stdin:
#for line in a.split("\n"):
    fields = line.strip().split("|")

    if len(fields) == 3:
        if prev_tconst == fields[0]:
            if prev_nconst == fields[1] and vote is not None:
                print(vote+"|"+fields[2])

        elif prev_tconst != fields[0]:
            vote = None
            prev_tconst = fields[0]
            prev_nconst = fields[1]
        else:
            prev_nconst = fields[1]

    else:
        if fields[1].isdigit():
            prev_tconst = fields[0]
            vote = fields[1]
        else:
            if prev_tconst == fields[0]:
                prev_nconst = fields[1]
            else:
                prev_tconst = fields[0]

                prev_nconst = fields[1]
                vote = None