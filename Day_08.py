# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 8
https://adventofcode.com/2023/day/8
2023-12-08, 17:28; 2023-12-08, 17:45; 2023-12-09, 12:00
"""


### Load Data #################################################################

# read input
filename = 'Day_08.txt'
f = open(filename)
text = f.readlines()

# example input (1)
# text = ['LLR\n', \
#         '\n', \
#         'AAA = (BBB, BBB)\n', \
#         'BBB = (AAA, ZZZ)\n', \
#         'ZZZ = (ZZZ, ZZZ)\n']

# example input (2)
# text = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""
# text = text.split('\n')
# text = [line+'\n' for line in text]


### Part One ##################################################################

# analyze nodes
nodes = {}
for line in text[2:]:
    node  = line[ : line.find('=')-1]
    left  = line[line.find('(')+1 : line.find(',')]
    right = line[line.find(',')+2 : line.find(')')]
    nodes[node] = {'L': left, 'R': right}

# analyze routes
dirs  = text[0][:-1]
steps = 0
nxt   = 'AAA'
while nxt != 'ZZZ':
    nxt   = nodes[nxt][dirs[steps % len(dirs)]]
    steps = steps + 1
print(steps)


### Part Two ##################################################################

# analyze nodes
nodes = {}
for line in text[2:]:
    node  = line[ : line.find('=')-1]
    left  = line[line.find('(')+1 : line.find(',')]
    right = line[line.find(',')+2 : line.find(')')]
    nodes[node] = {'L': left, 'R': right}
# print(nodes)

# analyze routes
dirs  = text[0][:-1]
steps = 0
nxt   = [key for key in nodes.keys() if key.endswith('A')]
stops = [0 for key in nxt]
while not all([s!=0 for s in stops]):
    nxt   = [nodes[key][dirs[steps % len(dirs)]] for key in nxt]
    steps = steps + 1
    for i, key in enumerate(nxt):
        if stops[i] == 0 and key.endswith('Z'):
            stops[i] = steps

# compute steps
import math
total = math.lcm(*stops)
print(total)

# Note: This is the first time I needed a hint to solve.
# I got the LCM suggestion from https://www.reddit.com/r/adventofcode/.