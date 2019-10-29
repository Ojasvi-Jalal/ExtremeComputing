#!/usr/bin/python2.7
# memory-efficient_reducer.py

import sys

prev_tconst = None
prev_title = None
prev_genres = None
prev_decade = None
prev_ave_rating = None

#if combination possible, combines and prints: str(decade) + "|" + genre + "|" + title + "|" + str(prev_ave_rating)
#otherwise skips when combination not possible
for line in sys.stdin:
    line = line.strip()
    fields = line.split("|")

    if fields[1] == "c":
        decade  = fields[0]
        genre   = fields[2]
        title   = fields[3]
        ave_rating  = fields[4]
        print(str(decade) + "|" + genre + "|" + title + "|" + str(ave_rating))
        continue

    if len(fields) == 4:
        tconst = fields[0]
        title  = fields[1]
        decade = fields[2]
        genres = fields[3]
        if prev_tconst==tconst and prev_ave_rating is not None:
            for genre in genres.strip().split(","):
                print(str(decade) + "|" + genre + "|" + title + "|" + str(prev_ave_rating))
            prev_ave_rating = None

        else:
            prev_tconst = tconst
            prev_title = title
            prev_genres = genres
            prev_decade = decade
            prev_ave_rating = None

    else:
        tconst = fields[0]
        ave_rating = fields[1]
        if prev_tconst == tconst:
            for genre in prev_genres.strip().split(","):
                print(str(prev_decade) + "|" + genre + "|" + prev_title + "|" + str(ave_rating))
            prev_decade = None
            prev_genres = None
            prev_title = None
            prev_tconst = None
        else:
            prev_tconst = tconst
            prev_ave_rating = ave_rating
            prev_decade = None
            prev_genres = None
            prev_title = None
