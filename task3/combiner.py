#!/usr/bin/python2.7
# memory-efficient_reducer.py
#cat title.basics.tsv | ./mapper.py | sort -t'|' -k./reducer.py

import sys

# Input: [tconst|title|decade|genre] or [tconst|average_rating]

# Output:
# if combination possible, output: decade|genre|title|ave_rating
#else print the input line as it is

prev_tconst = None
prev_title = None
prev_genres = None
prev_decade = None
prev_ave_rating = None

for line in sys.stdin:
    line = line.strip()
    fields = line.split("|")

    if len(fields) == 4:
        tconst = fields[0]
        title  = fields[1]
        decade = fields[2]
        genres = fields[3]
        if prev_tconst==tconst and prev_ave_rating is not None:
            for genre in genres.strip().split(","):
                print(str(decade) + "|c|" + genre + "|" + title + "|" + str(prev_ave_rating))
            prev_ave_rating = None
            prev_decade = None
            prev_genres = None
            prev_title = None
            prev_tconst = None
        else:
            if prev_tconst != None:
                if prev_title != None and prev_decade != None and prev_genres != None:
                    print(prev_tconst + "|" + prev_title + "|" + str(prev_decade) + "|" + prev_genres)
                else:
                    print(prev_tconst + "|" + prev_ave_rating)
                    prev_ave_rating = None
            prev_tconst = tconst
            prev_title = title
            prev_genres = genres
            prev_decade = decade

    else:
        tconst = fields[0]
        ave_rating = fields[1]
        if prev_tconst == tconst:
            for genre in prev_genres.strip().split(","):
                print(str(prev_decade) + "|c|" + genre + "|" + prev_title + "|" + str(ave_rating))
            prev_decade = None
            prev_genres = None
            prev_title = None
            prev_tconst = None
            prev_ave_rating = None
        else:
            if prev_tconst != None:
                if prev_title != None and prev_decade != None and prev_genres != None:
                    print(prev_tconst + "|" + prev_title + "|" + str(prev_decade) + "|" + prev_genres)
                    prev_title = None
                    prev_genres = None
                    prev_decade = None
                else:
                    print(prev_tconst + "|" + prev_ave_rating)
            prev_tconst = tconst
            prev_ave_rating = ave_rating

if prev_tconst is not None:
    if prev_title is not None:
        print(prev_tconst + "|" + prev_title + "|" + str(prev_decade) + "|" + prev_genres)
    else:
        print(prev_tconst + "|" + prev_ave_rating)
