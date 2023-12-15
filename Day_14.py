# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 14
https://adventofcode.com/2023/day/14
2023-12-15, 11:31; 2023-12-15, 12:26
"""


### Load Data #################################################################

# read input
filename = 'Day_14.txt'
f = open(filename)
text = f.readlines()

# example input
# text = """
# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....
# """
# text = text.split('\n')
# text = text[1:-1]
# text = [line+'\n' for line in text]


### Part One ##################################################################

# remove linebreaks
text = [line[:-1] for line in text]

# for each column
for j in range(len(text[0])):
    # travel through rows
    i = 0
    while i < len(text):
        if i > 0:
            if text[i][j] == 'O' and text[i-1][j] == '.':
                text[i-1] = text[i-1][:j] + 'O' + text[i-1][j+1:]
                text[i]   = text[i][:j]   + '.' + text[i][j+1:]
                i = i - 1
            else:
                i = i + 1
        else:
            i = i + 1

# for each row
my_sum = 0
for i in range(len(text)):
    for j in range(len(text[0])):
        if text[i][j] == 'O':
            my_sum = my_sum + (len(text)-i)
print(my_sum)


### Part Two ##################################################################

# re-read input
filename = 'Day_14.txt'
f = open(filename)
text = f.readlines()
text = [line[:-1] for line in text]

# prepare cycles
N     = 200
rows  = len(text)
cols  = len(text[0])
loads = [0 for n in range(N)]

# perform all cycles
for n in range(N):
    
    # roll north
    for j in range(cols):
        i = 0
        while i < rows:
            if i > 0:
                if text[i][j] == 'O' and text[i-1][j] == '.':
                    text[i-1] = text[i-1][:j] + 'O' + text[i-1][j+1:]
                    text[i]   = text[i][:j]   + '.' + text[i][j+1:]
                    i = i - 2
            i = i + 1
    
    # roll west
    for i in range(rows):
        j = 0
        while j < cols:
            if j > 0:
                if text[i][j] == 'O' and text[i][j-1] == '.':
                    text[i] = text[i][:j-1] + 'O.' + text[i][j+1:]
                    j = j - 2
            j = j + 1
    
    # roll south
    for j in range(cols):
        i = rows-1
        while i > -1:
            if i < rows-1:
                if text[i][j] == 'O' and text[i+1][j] == '.':
                    text[i+1] = text[i+1][:j] + 'O' + text[i+1][j+1:]
                    text[i]   = text[i][:j]   + '.' + text[i][j+1:]
                    i = i + 2
            i = i - 1
    
    # roll east
    for i in range(rows):
        j = cols-1
        while j > -1:
            if j < cols-1:
                if text[i][j] == 'O' and text[i][j+1] == '.':
                    text[i] = text[i][:j] + '.O' + text[i][j+2:]
                    j = j + 2
            j = j - 1
    
    # print result
    if n in []:
        print(n)
        for line in text: print(line)
        print()
    
    # calculate total load
    my_sum = 0
    for i in range(len(text)):
        for j in range(len(text[0])):
            if text[i][j] == 'O':
                my_sum = my_sum + (len(text)-i)
    loads[n] = my_sum
    print(str(n)+': '+str(my_sum))

# plot total loads
import matplotlib.pyplot as plt
plt.plot(list(range(N)), loads, '-b')

# get ultimale value
N  = 1000000000
if max(loads[100:]) > loads[0]: m1 = max(loads[100:])
else:                           m1 = min(loads[100:])
i1 = loads.index(m1)
i2 = loads[i1+1:].index(m1) + (i1+1)
i3 = (N-1-i1) % (i2-i1) + i1
print(loads[i3])