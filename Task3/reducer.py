#!/usr/bin/python2.7
# memory-efficient_reducer.py
import sys

prev_word = None
title = ""
genre = ""
decade = -1
ave_rating = 0.0

for line in sys.stdin:
    line = line.strip()
    fields = line.split("|")

    if len(fields) == 4:
        if prev_word == fields[0]:
            title = fields[1]
            decade = fields[2]
            genre = fields[3]

        else:
            if prev_word != None and ave_rating != 0.0:
                print(prev_word + "|" + title + "|" + genre + "|" + str(decade) + "|" + str(ave_rating))

            prev_word = fields[0]
            title = fields[1]
            decade = fields[2]
            genre = fields[3]

    else:
        if prev_word == fields[0]:
            ave_rating = fields[1]

        else:
            if prev_word != None and title != "" and genre != "" and decade != -1:
                print(prev_word + "|" + title + "|" + genre + "|" + str(decade) + "|" + str(ave_rating))

            prev_word = fields[0]
            ave_rating = fields[1]