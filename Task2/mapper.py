#!/usr/bin/python2.7
# mapper.py
#cat reducer_input.xdfnghxbxdflhkgndkljgncdfkl | ./reducer.py
import sys

from collections import defaultdict

a= "tt1927164\tmovie\t\N\tThe Zombies Are Coming to Town!\t0\t\N\t\N\t64\t\N" \
"\ntt8342104\tmovie\tKing of the Valley\tKing of the Valley\t0\t2018\t\N\t97\tDrama\ntt0057028\t" \
"movie\tEleven Years and One Day\tElf Jahre und ein Tag\t0\t1963\t\N\t100\tDrama\ntt0061438\tmovie\tThe " \
"Man Who Betrayed the Mafia\tL'homme qui trahit la mafia\t0\t1967\t\N\t90\tDrama,Thriller\ntt1140875\tmovie\t" \
"Sell Out! (The Student Films of Don Swanson)\tSell Out! (The Student Films of Don Swanson)\t0\t2007\t\N\t" \
"180\tComedy,Drama,Horror\ntt1642662\tmovie\tThe Works of Darren McGannon\tThe Works of Darren McGannon\t" \
"0\t2010\t\N\t91\tComedy,Drama,Romance"

for line in sys.stdin:
#Call the map function for each line in the input
    fields = line.strip().split('\t')  # Split the line to fields
    if len(fields) == 9:
        if fields[1] == "movie" and fields[2] != "\\N" and fields[5] != "\\N" and (int(fields[5]) >= 1990 and int(fields[5]) <= 2019):
            print(fields[0]+"|m|"+fields[2])

    else:
        if float(fields[1]) >=7.5 and int(fields[2]) >= 500000:
            print(fields[0]+"|m")