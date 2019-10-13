#!/usr/bin/python2.7
# memory-efficient_reducer.py
#cat title.basics.tsv | ./mapper.py | sort -t'|' -k./reducer.py

import sys

pre_Decade = ""
pre_Genre = ""
for line in sys.stdin:
    decade, genre, rating, title = line.split("|")

    if pre_Decade == decade and pre_Genre == genre:
        continue
    else:
        print(decade+"|"+genre+"|"+title)
        pre_Decade = decade
        pre_Genre = genre