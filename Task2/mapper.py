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

combiner_dict = defaultdict(list)
MAX_SIZE = 100

# def mapper_function(line):
#     fields = line.strip().split('\t')   #Split the line to fields
#     # value = ["",0]
#     # if len(fields) == 9:        #We are processing a line from title.basics.tsv
#     #     if fields[1] == "movie":
#     #         primaryTitle = fields[2] if fields[2] != "\N" else None #Gets the primary title of the movie
#     #         releaseYear = fields[5] if fields[5] != "\N" else None  #Gets the release year of the movie
#     #         if primaryTitle != None and releaseYear!= None:
#     #             value[0] = primaryTitle
#     #             value[1] = releaseYear
#     #             yield fields[0], value
#     #         else:
#     #             yield None, None
#     #     else:
#     #         yield None, None
#     #
#     # else:                       #We are processing a line from title.ratings.tsv
#     #     fields = line.strip().split('\t')
#     #     value[0] = fields[1]
#     #     value[1] = fields[2]
#     #     yield fields[0], value
#     yield fields[0]

for line in sys.stdin:
#Call the map function for each line in the input
    fields = line.strip().split('\t')  # Split the line to fields
    if len(fields) == 9:
        if fields[1] == "movie" and fields[2] != "\\N" and fields[5] != "\\N" and (int(fields[5]) >= 1990 and int(fields[5]) <= 2019):
            print(fields[0]+"|"+fields[2])
        #     if key in combiner_dict:
        #         combiner_dict[key][0] = fields[2] if fields[2] != "\\N" else None
        #         combiner_dict[key][1] = fields[5] if fields[5] != "\\N" else None
        #     else:
        #         combiner_dict[key] = ["", 0, 0.0, 0]
        #         combiner_dict[key][0] = fields[2] if fields[2] != "\\N" else None
        #         combiner_dict[key][1] = fields[5] if fields[5] != "\\N" else None
        # else:
        #     continue
    else:
        if float(fields[1]) >=7.5 and int(fields[2]) >= 500000:
            print(fields[0]+"|"+"")
    # if key in combiner_dict:
    #     combiner_dict[key][2] = fields[1]
    #     combiner_dict[key][3] = fields[2]
    # else:
    #     combiner_dict[key] = ["", 0, 0.0, 0]
    #     combiner_dict[key][2] = fields[1]
    #     combiner_dict[key][3] = fields[2]

# # To keep O(1) space, we bound the size of our memory footprint
# if len(combiner_dict) > MAX_SIZE:
#     for key, value in combiner_dict.items():
#         print(key + "|" + str(combiner_dict[key][0])+ "|" + str(combiner_dict[key][1])+ "|" +str(combiner_dict[key][2])+ "|" +str(combiner_dict[key][3]))
#
#     combiner_dict.clear()

# Emit leftover key-value pairs and use '|' as the delimiter
# for key, value in combiner_dict.items():
#     if(combiner_dict[key][0] is None or combiner_dict[key][1] is None):
#         continue
#     else:
#         print(key + "|" + str(combiner_dict[key][0])+ "|" + str(combiner_dict[key][1])+ "|" +str(combiner_dict[key][2])+ "|" +str(combiner_dict[key][3]))