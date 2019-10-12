#!/usr/bin/python2.7
# mapper.py
# cat reducer_input.xdfnghxbxdflhkgndkljgncdfkl | ./reducer.py
import sys

from collections import defaultdict

for line in sys.stdin:
    fields = line.strip().split('|')
    decade = fields[3]
    genre = fields[2]
    title = fields[1]
    ave_rating = fields[4]
    print(decade + "|" + genre + "|" + title + "|" + ave_rating)