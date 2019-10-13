#!/usr/bin/python2.7
# memory-efficient_reducer.py
#cat title.basics.tsv | ./mapper.py | sort -t'|' -k./reducer.py

import sys

prev_word = None
title = ""
genre = ""
decade = -1
ave_rating = -1.0

a = "tt0012759|Tilly of Bloomsbury|2|Comedy\ntt0015335|Sinners in Heaven|2|Drama\ntt0015335|Sinners in Heaven|2|Romance\ntt0023346|7.4\ntt0023346|Pojkarna p Storholmen|3|Comedy\ntt0027283|The Terrible Lovers|3|Comedy\ntt0034947|7.5"
#for line in a.split("\n"):
for line in sys.stdin:
    line = line.strip()
    fields = line.split("|")

    if len(fields) == 4:
        if prev_word == fields[0] and ave_rating == -1.0:
            title = fields[1]
            decade = fields[2]
            genre = fields[3]

        if prev_word == fields[0] and ave_rating != -1.0:
            if title != "" and genre != "" and decade != -1:
                print(prev_word + "|" + title + "|" + genre + "|" + str(decade) + "|" + str(ave_rating))
            title = fields[1]
            decade = fields[2]
            genre = fields[3]

        else:
            if prev_word is not None and ave_rating != -1.0:
                if title != "" and genre != "" and decade != -1:
                    print(prev_word + "|" + title + "|" + genre + "|" + str(decade) + "|" + str(ave_rating))
                ave_rating = -1.0

            prev_word = fields[0]
            title = fields[1]
            decade = fields[2]
            genre = fields[3]

    else:
        if prev_word == fields[0]:
            ave_rating = fields[1]

        else:
            if prev_word != None and title != "" and genre != "" and decade != -1:
                if ave_rating != -1:
                    print(prev_word + "|" + title + "|" + genre + "|" + str(decade) + "|" + str(ave_rating))
                title = ""
                decade = -1
                genre = ""

            prev_word = fields[0]
            ave_rating = fields[1]