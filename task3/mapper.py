#!/usr/bin/python2.7
# mapper.py
import sys

#coverts year to its decade
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

#Output: movies of each genre for each decade between 1990 and 1999 or tconst|rating
for line in sys.stdin:
    fields = line.strip().split('\t')  # Split the line to fields
    if len(fields) == 9:
        if fields[1] == "movie" and fields[2] != "\\N" and fields[5] != "\\N" and (
                int(fields[5]) >= 1900 and int(fields[5]) <= 1999) and fields[8] != "\\N":
            decade = get_decade(int(fields[5]))
            print(fields[0] + "|" + fields[2] + "|" + str(decade) + "|" + fields[8].strip())
        else:
            continue
    else:
        print(fields[0] + "|" + fields[1])
