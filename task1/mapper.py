#!/usr/bin/python2.7
# task1
# mapper.py
import sys
from collections import defaultdict

#Input: title.basics.csv
#Output: [genre:str|sum_of_all_runtimes:float|count:int|max_runtime:int|min_runtime:int]
#used for the memory efficient in-mapper combiner
combiner_dict = defaultdict(list)
MAX_SIZE = 100

def mapper_function(line):
    fields = line.strip().split('\t')  # Split line to fields
    genres = fields[8]  # Gets all the genres in the dataset
    runtime = -1 if fields[7] == "\\N" else fields[7]  # Gets the runtime for the movie title

    if genres != "\\N" and runtime != -1:  # Only yeilds the genres and runtime if both of them have a valid value
        for genre in genres.strip().split(','):
            yield genre, int(runtime)


# in-mapper combiner - being used to save time and reduce network traffic
for line in sys.stdin:
    # Call the map function for each line in the input
    for key, value in mapper_function(line):

        # there is already an entry of the genre in the dict
        if key in combiner_dict:
            combiner_dict[key][0] += value
            combiner_dict[key][1] += 1
            combiner_dict[key][2] = value if value > combiner_dict[key][2] else combiner_dict[key][2]
            combiner_dict[key][3] = value if value < combiner_dict[key][3] else combiner_dict[key][3]

        # there's no entry for the genre in the dict
        else:
            combiner_dict[key] = [0, 0, 0, 0]
            combiner_dict[key][0] += value  # sum of all the runtimes per genre
            combiner_dict[key][1] += 1      # count of the number of times the genre appears in order to calculate the average later
            combiner_dict[key][2] = value   # max runtime per genre
            combiner_dict[key][3] = value   # min runtime per genre

        # To keep O(1) space, we bound the size of our memory footprint
        # and emit the key/value pairs if ot gets too large
        if len(combiner_dict) > MAX_SIZE:
            for key, value in combiner_dict.items():
                print(key + "|" + str(combiner_dict[key][0]) + "|" + str(combiner_dict[key][1]) + "|" + str(
                    combiner_dict[key][2]) + "|" + str(combiner_dict[key][3]))

            combiner_dict.clear()

# Emit leftover key-value pairs and use '|' as the delimiter
for key, value in combiner_dict.items():
    print(key + "|" + str(combiner_dict[key][0]) + "|" + str(combiner_dict[key][1]) + "|" + str(
        combiner_dict[key][2]) + "|" + str(combiner_dict[key][3]))
