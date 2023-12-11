# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 11
https://adventofcode.com/2023/day/11
2023-12-11, 08:32; 2023-12-11, 09:12
"""


### Load Data #################################################################

# read input
filename = 'Day_11.txt'
f = open(filename)
text = f.readlines()

# example input
# text = """
# ...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....
# """
# text = text.split('\n')
# text = text[1:-1]
# text = [line+'\n' for line in text]


### Part One ##################################################################

# remove linebreaks
text = [line[:-1] for line in text]

# duplicate rows
print('-> Rows: ', end='')
i = 0
while i < len(text):
    if all([c=='.' for c in text[i]]):
        txt = text[:i+1]
        txt.append(text[i])
        txt.extend(text[i+1:])
        text = txt
        print(str(i)+', ', end='')
        i = i + 2
    else:
        i = i + 1
print('end.\n')

# duplicate columns
print('-> Columns: ', end='')
j = 0
while j < len(text[0]):
    if all([line[j]=='.' for line in text]):
        text = [line[:j+1]+'.'+line[j+1:] for line in text]
        print(str(j)+', ', end='')
        j = j + 2
    else:
        j = j + 1
print('end.\n')

# enumerate galaxies
print('-> Galaxies: ', end='')
gals = []
for i, line in enumerate(text):
    for j, c in enumerate(line):
        if c=='#':
            print('['+str(i)+','+str(j)+'], ', end='')
            gals.append([i,j])
print('end.\n')

# calculate distances
my_sum = 0
# import networkx as nx
for n1 in range(len(gals)):
    print('-> from galaxy {} out of {} to galaxies '.format(n1+1, len(gals)), end='')
    for n2 in range(0,n1):
        print('{}, '.format(n2+1), end='')
        y1, x1 = (gals[n1][0], gals[n1][1])
        y2, x2 = (gals[n2][0], gals[n2][1])
        if x1 == x2:
            dist = abs(y2-y1)
        elif y1 == y2:
            dist = abs(x2-x1)
        elif abs(x2-x1) == abs(y2-y1):
            dist = 2*abs(x2-x1)
        else:
            dist = abs(x2-x1) + abs(y2-y1)
            # grid = nx.grid_2d_graph(abs(y2-y1)+1, abs(x2-x1)+1)
            # path = nx.bidirectional_shortest_path(grid, source=(0,0), target=(abs(y2-y1),abs(x2-x1)))
            # dist = len(path)-1
        my_sum = my_sum + dist
    print('end.')
print(my_sum)


### Part Two ##################################################################

# re-read input
print()
filename = 'Day_11.txt'
f = open(filename)
text = f.readlines()
text = [line[:-1] for line in text]

# find empty rows
print('-> Rows: ', end='')
rows = []
for i in range(len(text)):
    if all([c=='.' for c in text[i]]):
        print(str(i)+', ', end='')
        rows.append(i)
print('end.\n')

# find empty columns columns
print('-> Columns: ', end='')
cols = []
for j in range(len(text[0])):
    if all([line[j]=='.' for line in text]):
        print(str(j)+', ', end='')
        cols.append(j)
print('end.\n')

# enumerate galaxies
print('-> Galaxies: ', end='')
gals = []
for i, line in enumerate(text):
    for j, c in enumerate(line):
        if c=='#':
            print('['+str(i)+','+str(j)+'], ', end='')
            gals.append([i,j])
print('end.\n')

# calculate distances
factor = 1000000
my_sum = 0
for n1 in range(len(gals)):
    print('-> from galaxy {} out of {} to galaxies 1 to {} ... '.format(n1+1, len(gals), n1), end='')
    for n2 in range(0,n1):
        y1, x1 = (gals[n1][0], gals[n1][1])
        y2, x2 = (gals[n2][0], gals[n2][1])
        dist   = abs(x2-x1) + abs(y2-y1)
        for i in rows:
            if i in range(min([y1,y2]),max([y1,y2])):
                dist = dist + (factor-1)
        for j in cols:
            if j in range(min([x1,x2]),max([x1,x2])):
                dist = dist + (factor-1)
        my_sum = my_sum + dist
    print('end.')
print(my_sum)