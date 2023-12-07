# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 6
https://adventofcode.com/2023/day/6
2023-12-07, 21:45; 2023-12-07, 21:51
"""


### Load Data #################################################################

# read input
filename = 'Day_06.txt'
f = open(filename)
text = f.readlines()

# example input
# text = ['Time:      7  15   30\n', \
#         'Distance:  9  40  200\n']

# extract numbers
def str2list(my_str):
    my_list = [int(n) for n in my_str.split()]
    return my_list


### Part One ##################################################################

# extract data
times = str2list(text[0][text[0].find(':')+1 : -1])
dists = str2list(text[1][text[1].find(':')+1 : -1])
ways  = [0 for t in times]

# analyze data
my_prod = 1
for i in range(len(times)):
    for j in range(0,times[i]+1):
        if ((times[i]-j) * j) > dists[i]:
            ways[i] = ways[i] + 1
    my_prod = my_prod * ways[i]
print(my_prod)


### Part Two ##################################################################

# extract data
time = int(text[0][text[0].find(':')+1 : -1].replace(' ', ''))
dist = int(text[1][text[1].find(':')+1 : -1].replace(' ', ''))
ways = 0

# analyze data
for j in range(0,time+1):
    if ((time-j) * j) > dist:
        ways = ways + 1
print(ways)