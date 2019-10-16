#!/usr/bin/python2.7
# memory-efficient_reducer.py
#cat title.basics.tsv | ./mapper.py | sort -t'|' -k./reducer.py

import sys

# prev_word = None
# title = ""
# genre = ""
# decade = -1
# ave_rating = -1.0


#for line in a.split("\n"):
# for line in sys.stdin:
#     line = line.strip()
#     fields = line.split("|")
#
#     if len(fields) == 4:
#         if prev_word == fields[0] and ave_rating == -1.0:
#             title = fields[1]
#             decade = fields[2]
#             genre = fields[3]
#
#         if prev_word == fields[0] and ave_rating != -1.0:
#             if title != "" and genre != "" and decade != -1:
#                 print(str(decade) + "|" + genre + "|" + title + "|" + str(ave_rating))
#             title = fields[1]
#             decade = fields[2]
#             genre = fields[3]
#
#         else:
#             if prev_word is not None and ave_rating != -1.0:
#                 if title != "" and genre != "" and decade != -1:
#                     print(str(decade) + "|" + genre + "|" + title + "|" + str(ave_rating))
#                 ave_rating = -1.0
#
#             prev_word = fields[0]
#             title = fields[1]
#             decade = fields[2]
#             genre = fields[3]
#
#     else:
#         if prev_word == fields[0]:
#             ave_rating = fields[1]
#
#         else:
#             if prev_word != None and title != "" and genre != "" and decade != -1:
#                 if ave_rating != -1:
#                     print(str(decade) + "|" + genre + "|" + title + "|" + str(ave_rating))
#                 title = ""
#                 decade = -1
#                 genre = ""
#
#             prev_word = fields[0]
#             ave_rating = fields[1]
a = "tt0010764|Theodora|2|Drama,Comedy\ntt0010764|9.2\ntt0010766|The Test of Honor|1|Drama\ntt0010793|7.2"

prev_tconst = None
prev_title = None
prev_genres = None
prev_decade = None
prev_ave_rating = None

for line in sys.stdin:
#for line in a.split("\n"):
    line = line.strip()
    fields = line.split("|")

    if len(fields) == 4:
        tconst = fields[0]
        title  = fields[1]
        decade = fields[2]
        genres = fields[3]
        if prev_tconst==tconst and prev_ave_rating is not None:
            for genre in genres.strip().split(","):
                print(str(decade) + "|" + genre + "|" + title + "|" + str(prev_ave_rating))
            prev_ave_rating = None

        else:
            prev_tconst = tconst
            prev_title = title
            prev_genres = genres
            prev_decade = decade

    else:
        tconst = fields[0]
        ave_rating = fields[1]
        if prev_tconst == tconst:
            for genre in prev_genres.strip().split(","):
                print(str(prev_decade) + "|" + genre + "|" + prev_title + "|" + str(ave_rating))
            prev_decade = None
            prev_genres = None
            prev_title = None
            prev_tconst = None
        else:
            prev_tconst = tconst
            prev_ave_rating = ave_rating


