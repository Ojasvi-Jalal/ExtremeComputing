#!/usr/bin/python2.7
# memory-efficient_reducer.py
import sys

#Input: [genre:str|sum_of_all_runtimes:float|count:int|max_runtime:int|min_runtime:int]
#Output: [avg_runtime:float|max_runtime:int|min_runtime:int|genre:str]

#used for the memory efficient in-mapper combiner
prev_word = None
sum_total = 0
count_total = 0
max_overall = 0
min_overall = 0

for line in sys.stdin:  # For every line in the input from stdin
    line = line.strip()  # Remove trailing characters
    genre, sum, count, max, min = line.split("|")
    sum = int(sum)
    count = int(count)
    max = int(max)
    min = int(min)

    # Hadoop sorts mapper output by key, and the reducer takes these keys sorted
    if prev_word == genre:
        sum_total += sum
        count_total += count
        max_overall = max if max > max_overall else max_overall
        min_overall = min if min < min_overall else min_overall
    else:
        if prev_word != None:  # Write result to stdout
            average = float(sum_total) / count_total
            print(str('{0:.2f}'.format(average)) + "|" + str(max_overall) + "|" + str(min_overall) + "|" + prev_word)
            sum_total = 0
            count_total = 0
            max_overall = 0
            min_overall = 0

        sum_total = sum
        count_total = count
        max_overall = max
        min_overall = min
        prev_word = genre

if prev_word == genre:  # Don't forget the last key/value pair
    average = float(sum_total) / count_total
    print(str('{0:.2f}'.format(average)) + "|" + str(max_overall) + "|" + str(min_overall) + "|" + prev_word)
