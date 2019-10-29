#!/usr/bin/python2.7
# mapper.py
import sys

from collections import defaultdict

#Call the map function for each line in the input
for line in sys.stdin:
    fields = line.strip().split('\t')  # Split the line to fields
    if len(fields) == 9:
        #print the titles of movies which were released between 1990 and 2018.
        if fields[1] == "movie" and fields[2] != "\\N" and fields[5] != "\\N" and (int(fields[5]) >= 1990 and int(fields[5]) <= 2018):
            print(fields[0]+"|m|"+fields[2])

    else:
        #print the tconsts with average rating of >= 7.5 and with >= 500000 votes
        if float(fields[1]) >=7.5 and int(fields[2]) >= 500000:
            print(fields[0]+"|m")