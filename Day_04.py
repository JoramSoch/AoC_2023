# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 4
https://adventofcode.com/2023/day/4
2023-12-07, 08:54; 2023-12-07, 09:09
"""


### Part One ##################################################################

# read input
filename = 'Day_04_input.txt'
f = open(filename)
text = f.readlines()

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

# read input
filename = 'Day_04_input.txt'
f = open(filename)
text = f.readlines()

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