# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 2
https://adventofcode.com/2023/day/2
2023-12-05, 15:24; 2023-12-05, 18:02
"""


### Part One ##################################################################

# read input
filename = 'Day_02_input.txt'
f = open(filename)
text = f.readlines()

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

# import modules
import numpy as np

# read input
filename = 'Day_02_input.txt'
f = open(filename)
text = f.readlines()

# analyze input
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