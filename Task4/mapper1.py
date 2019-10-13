#!/usr/bin/python2.7
# mapper.py
# cat reducer_input.xdfnghxbxdflhkgndkljgncdfkl | ./reducer.py
import sys

for line in sys.stdin:
    fields = line.strip().split('\t')  # Split the line to fields
    if len(fields) == 6:
        if fields[1] != "\\N" and fields[5] != "\\N":
            for known_For_Title in fields[5].strip().split(','):
                print(known_For_Title + "|" + fields[0] + "|" + fields[1])
        else:
            continue

    else:
        if fields[2].isdigit():
            print(fields[0] + "|" + fields[2])
        else:
            if fields[2] != "\\N":
                for writer in fields[2].strip().split(','):
                    print(fields[0] + "|" + writer)
