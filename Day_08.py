# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 8
https://adventofcode.com/2023/day/8
2023-12-08, 17:28; 2023-12-08, 17:45
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
# print(nodes)

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
# steps = 14025644071
# nxt   = ['DVG', 'XXC', 'JRX', 'MSB', 'DCJ', 'HKJ']
while not all([key.endswith('Z') for key in nxt]):
    nxt   = [nodes[key][dirs[steps % len(dirs)]] for key in nxt]
    steps = steps + 1
    if steps % 1000000 == 0: print('{}, '.format(steps), end='')
print('end.')
print(steps)

# Note: This routine has not stopped after 14,025,644,071 iterations,
# but I also don't know how to simplify the algorithm.