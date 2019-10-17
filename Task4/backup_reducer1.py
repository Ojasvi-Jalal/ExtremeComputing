#!/usr/bin/python2.7
# memory-efficient_reducer.py
#cat title.basics.tsv | ./mapper.py | sort -t'|' -k./reducer.py

import sys

# a  = "tt8347882|70\ntt8347882|nm1913625\ntt8347882|nm1913625|Dipankar Sarkar"
# prev_tconst = None
# prev_nconst = None
# vote = None
# for line in sys.stdin:
# #for line in a.split("\n"):
#     fields = line.strip().split("|")
#
#     if len(fields) == 3:
#         if prev_tconst == fields[0]:
#             if prev_nconst == fields[1] and vote is not None:
#                 print(vote+"|"+fields[2])
#                 prev_nconst = None
#
#         elif prev_tconst != fields[0]:
#             vote = None
#             prev_tconst = fields[0]
#             prev_nconst = fields[1]
#         else:
#             prev_nconst = fields[1]
#
#     else:
#         if fields[1].isdigit():
#             prev_tconst = fields[0]
#             vote = fields[1]
#         else:
#             if prev_tconst == fields[0]:
#                 prev_nconst = fields[1]
#             else:
#                 prev_tconst = fields[0]
#
#                 prev_nconst = fields[1]
#                 vote = None

f = open("output_part4.out", "r")
prev_tconst = None
prev_nconst = None
prev_writer = None
prev_vote   = None

#for line in sys.stdin:
for line in f:
    fields = line.strip().split("|")

    if len(fields) == 3:
        tconst = fields[0]
        nconst = fields[1]
        writer = fields[2]
        if prev_tconst == tconst and prev_nconst == nconst and prev_vote != None:
            print(prev_vote+"|"+writer)
            prev_nconst = None

        else:
            if prev_tconst != None:
                prev_vote = None

            prev_tconst = tconst
            prev_nconst = nconst
            prev_writer = writer

    else:
        if fields[1].isdigit():
            if prev_tconst == fields[0] and prev_nconst is not None and prev_writer is not None:
                print(fields[1]+"|"+prev_writer)
                prev_nconst = None

            else:
                prev_tconst = fields[0]
                prev_vote = fields[1]
        else:
            if prev_tconst == fields[0] and prev_nconst == fields[1] and prev_writer is not None and prev_vote is not None:
                print(prev_vote+"|"+prev_writer)
                prev_nconst = None
            else:
                prev_tconst = fields[0]
                prev_nconst = fields[1]
                prev_writer = None

