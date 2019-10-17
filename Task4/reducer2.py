#!/usr/bin/python2.7
# mapper.py
# cat reducer_input.xdfnghxbxdflhkgndkljgncdfkl | ./reducer.py

import sys

n = 0

for line in sys.stdin:
    if n<10:
        print line
        n = n+1