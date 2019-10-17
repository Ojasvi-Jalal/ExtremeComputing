#!/usr/bin/python2.7
# combiner.py
#cat reducer_input.xdfnghxbxdflhkgndkljgncdfkl | ./reducer.py
import sys

a = "tt1332007|m|Strangers\ntt1395039|m|Etats gnraux\ntt1553930|m|The Survivors Project: Voices from the Inside-out!\ntt1631867|m|Edge of Tomorrow\ntt1631867|m\ntt1725803|m|Delhi in a Day"
#f = open("output.out", "r")

prev_tconst = None
prev_title = None
#for line in a.split("\n"):
# for line in f:
for line in sys.stdin:
    #print("Incoming:Combiner:" + line.strip())
    fields = line.strip().split("|")
    if len(fields) == 3:
        tconst = fields[0]
        title = fields[2]
        if prev_tconst == tconst:
            print(tconst+"|c|"+title)
            prev_tconst = None
            prev_title = None
        else:
            if prev_tconst != None:
                if prev_title !=None:
                    print(prev_tconst+"|m|"+prev_title)
                else:
                    print(prev_tconst+"|m")
            prev_tconst = tconst
            prev_title = title
    else:
        tconst = fields[0]
        if prev_tconst == tconst:
            print(prev_tconst+"|c|"+prev_title)
            prev_tconst = None
            prev_title = None
        else:
            if prev_tconst != None:
                if prev_title != None:
                    print(prev_tconst+"|m|"+prev_title)
                    prev_title = None
                else:
                    print(prev_tconst+"|m")
            prev_tconst = tconst

if prev_tconst is not None:
    if prev_title is not None:
        print(prev_tconst+"|m|"+prev_title)
    else:
        print(prev_tconst+"|m")