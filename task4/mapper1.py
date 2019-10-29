#!/usr/bin/python2.7
# mapper.py

import sys

# in: name.basics.tsv, title.crew.tsv, title.ratings.tsv,
# out: tconst, nconst, writes_name OR tconst, numVotes OR tconst, nconst
for line in sys.stdin:
    fields = line.strip().split('\t')  # Split the line to fields

    # for name.basics.tsv
    # for every writer print out all the titles they are known for
    if len(fields) == 6:
        if fields[1] != "\\N" and fields[5] != "\\N":
            nconst = fields[0]
            writer_name = fields[1]
            for known_For_Title in fields[5].strip().split(','):
                print(known_For_Title + "|" + fields[0] + "|" + fields[1])
        else:
            continue

    else:
        # for title.ratings.tsv
        # print tconst|vote
        if fields[2].isdigit():
            print(fields[0] + "|" + fields[2])

        # for title.crew.tsv
        # for each movie print out all its writers
        else:
            if fields[2] != "\\N":
                for writer in fields[2].strip().split(','):
                    print(fields[0] + "|" + writer)
