#!/usr/bin/python2.7
# combiner


import sys

#Input: "Decade|Genre|Title|Rating"
#Output: only if combination possible: decade+"|"+genre+"|"+rating+"|"+title+"|c"
#   else: skip

pre_Decade = None
pre_Genre = None
pre_Rating = None
pre_Title = None
for line in sys.stdin:
    decade, genre, rating, title = line.strip().split("|")

    if pre_Decade == decade and pre_Genre == genre:
        continue
    else:
        print(decade+"|"+genre+"|"+rating+"|"+title+"|c")
        pre_Decade = decade
        pre_Genre = genre