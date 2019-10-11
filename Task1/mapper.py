#!/usr/bin/python2.7
# mapper.py
import sys

from collections import defaultdict

# a= "tt1927164\tmovie\tThe Zombies Are Coming to Town!\tThe Zombies Are Coming to Town!\t0\t2011\t\N\t64\t\N" \
# "\ntt8342104\tmovie\tKing of the Valley\tKing of the Valley\t0\t2018\t\N\t97\tDrama\ntt0057028\t" \
# "movie\tEleven Years and One Day\tElf Jahre und ein Tag\t0\t1963\t\N\t100\tDrama\ntt0061438\tmovie\tThe " \
# "Man Who Betrayed the Mafia\tL'homme qui trahit la mafia\t0\t1967\t\N\t90\tDrama,Thriller\ntt1140875\tmovie\t" \
# "Sell Out! (The Student Films of Don Swanson)\tSell Out! (The Student Films of Don Swanson)\t0\t2007\t\N\t" \
# "180\tComedy,Drama,Horror\ntt1642662\tmovie\tThe Works of Darren McGannon\tThe Works of Darren McGannon\t" \
# "0\t2010\t\N\t91\tComedy,Drama,Romance"

combiner_dict = defaultdict(list)
MAX_SIZE = 100

def mapper_function(line):
    fields  = line.strip().split('\t')  # Split line to fields
    genres  =   fields[8]  # Gets all the genres in the dataset
    runtime = -1 if fields[7] == "\\N" else fields[7]  # Gets the runtime for the movie title
    if genres != "\N":
        for genre in genres.strip().split(','):
            yield genre, int(runtime)
    else:
        yield None, int(runtime)

for line in a.split("\n"):
    # Call the map function for each line in the input
    for key, value in mapper_function(line):
        if key is None or value == -1:
            continue
        if key in combiner_dict:
            combiner_dict[key][0] += value
            combiner_dict[key][1] += 1
            combiner_dict[key][2] = value if value > combiner_dict[key][2] else combiner_dict[key][2]
            combiner_dict[key][3] = value if value < combiner_dict[key][3] else combiner_dict[key][3]

        else:
            combiner_dict[key] = [0, 0, 0, 0]
            combiner_dict[key][0] += value
            combiner_dict[key][1] += 1
            combiner_dict[key][2] = value
            combiner_dict[key][3] = value
            # To keep O(1) space, we bound the size of our memory footprint
        if len(combiner_dict) > MAX_SIZE:
            for key, value in combiner_dict.items():
                print(key + "|" + str(combiner_dict[key][0])+ "|" + str(combiner_dict[key][1])+ "|" +str(combiner_dict[key]))

            combiner_dict.clear()


# Emit leftover key-value pairs and use '|' as the delimiter
for key, value in combiner_dict.items():
    print(key + "|" + str(combiner_dict[key][0])+ "|" + str(combiner_dict[key][1])+ "|" +str(combiner_dict[key][2])+ "|" +str(combiner_dict[key][3]))