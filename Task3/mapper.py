#!/usr/bin/python2.7
# mapper.py
# cat reducer_input.xdfnghxbxdflhkgndkljgncdfkl | ./reducer.py
import sys

from collections import defaultdict

a = "tt1927164\tmovie\t\N\tThe Zombies Are Coming to Town!\t0\t\N\t\N\t64\t\N" \
    "\ntt8342104\tmovie\tKing of the Valley\tKing of the Valley\t0\t1909\t\N\t97\tDrama\ntt0057028\t" \
    "movie\tEleven Years and One Day\tElf Jahre und ein Tag\t0\t1963\t\N\t100\tDrama\ntt0061438\tmovie\tThe " \
    "Man Who Betrayed the Mafia\tL'homme qui trahit la mafia\t0\t1967\t\N\t90\tDrama,Thriller\ntt1140875\tmovie\t" \
    "Sell Out! (The Student Films of Don Swanson)\tSell Out! (The Student Films of Don Swanson)\t0\t2007\t\N\t" \
    "180\tComedy,Drama,Horror\ntt1642662\tmovie\tThe Works of Darren McGannon\tThe Works of Darren McGannon\t" \
    "0\t2010\t\N\t91\tComedy,Drama,Romance"

def get_decade(year):
    if 1900 <= year <= 1909:
        return 0
    if 1910 <= year <= 1919:
        return 1
    if 1920 <= year <= 1929:
        return 2
    if 1930 <= year <= 1939:
        return 3
    if 1940 <= year <= 1949:
        return 4
    if 1950 <= year <= 1959:
        return 5
    if 1960 <= year <= 1969:
        return 6
    if 1970 <= year <= 1979:
        return 7
    if 1980 <= year <= 1989:
        return 8
    if 1990 <= year <= 1999:
        return 9

for line in a.split("\n"):
    fields = line.strip().split('\t')  # Split the line to fields
    if len(fields) == 9:
        if fields[1] == "movie" and fields[2] != "\\N" and fields[5] != "\\N" and (
                int(fields[5]) >= 1900 and int(fields[5]) <= 1999) and fields[8] != "\\N":
            decade = get_decade(int(fields[5]))
            for genre in fields[8].strip().split(','):
                print(fields[0] + "|" + fields[2] + "|" + str(decade) + "|" + genre)
        else:
            continue
    else:
        print(fields[0] + "|" + fields[1])
