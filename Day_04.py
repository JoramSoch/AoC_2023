# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 4
https://adventofcode.com/2023/day/4
2023-12-07, 08:54; 2023-12-07, 09:09; 2013-12-09, 12:23
"""


### Load Data #################################################################

# read input
filename = 'Day_04.txt'
f = open(filename)
text = f.readlines()

# example input
# text = """
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """
# text = text.split('\n')
# text = text[1:-1]


### Part One ##################################################################

# analyze input
my_sum = 0
for line in text:
    win_str = line[line.find(':')+2 : line.find('|')-1]
    win     = [int(n) for n in win_str.split()]
    you_str = line[line.find('|')+2 : len(line)]
    you     = [int(n) for n in you_str.split()]
    num_win = sum([(n in win) for n in you])
    points  = [0,2**(num_win-1)][int(num_win>0)]
    my_sum  = my_sum + points
print(my_sum)


### Part Two ##################################################################

# analyze input
my_sum = 0
copies = [1 for line in text]
for i, line in enumerate(text):
    win_str = line[line.find(':')+2 : line.find('|')-1]
    win     = [int(n) for n in win_str.split()]
    you_str = line[line.find('|')+2 : len(line)]
    you     = [int(n) for n in you_str.split()]
    num_win = sum([(n in win) for n in you])
    for j in range(copies[i]):
        for k in range(1,num_win+1):
            if i+k < len(text):
                copies[i+k] = copies[i+k] + 1
print(sum(copies))