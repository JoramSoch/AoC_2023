# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 2
https://adventofcode.com/2023/day/2
2023-12-05, 15:24; 2023-12-05, 18:02; 2023-12-09, 12:15
"""


### Load Data #################################################################

# read input
filename = 'Day_02.txt'
f = open(filename)
text = f.readlines()

# example input
# text = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', \
#         'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', \
#         'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', \
#         'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', \
#         'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']


### Part One ##################################################################

# analyze input
bag = {'red': 12, 'green': 13, 'blue': 14}
my_sum = 0
for line in text:
    game_id = int(line[line.find('Game ')+len('Game '):line.find(':')])
    valid   = True
    for i in range(len(line)):
        for color in bag.keys():
            if line[i:(i+len(color))] == color:
                balls = int(line[(i-3):i])
                if balls > bag[color]:
                    valid = False
    if valid: my_sum = my_sum + game_id
print(my_sum)


### Part Two ##################################################################

# analyze input
import numpy as np
colors = ['red', 'green', 'blue']
my_sum = 0
for line in text:
    game  = 0
    balls = np.zeros((10,len(colors)), dtype=int)
    for i in range(len(line)):
        if line[i] == ';':
            game = game + 1
        for color in colors:
            if line[i:(i+len(color))] == color:
                balls[game,colors.index(color)] = int(line[(i-3):i])
    power  = np.prod(np.max(balls, axis=0))
    my_sum = my_sum + power
print(my_sum)