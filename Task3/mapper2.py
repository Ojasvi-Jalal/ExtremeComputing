#!/usr/bin/python2.7
# mapper.py
# cat reducer_input.xdfnghxbxdflhkgndkljgncdfkl | ./reducer.py
import sys

from collections import defaultdict

for line in sys.stdin:
    fields = line.strip().split('|')
    print(fields[0] + "|" + fields[1] + "|" + fields[3] + "|" + fields[2]) # Prints: "Decade|Genre|Title|Rating"