# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 10
https://adventofcode.com/2023/day/10
2023-12-10, 19:46; 2023-12-10, 21:49; 2023-12-11, 13:35
"""


### Load Data #################################################################

# read input
filename = 'Day_10.txt'
f = open(filename)
text = f.readlines()

# example input (1)
# text = """
# -L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF
# """
# text = text.split('\n')
# text = text[1:-1]

# example input (2)
# text = """
# 7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ
# """
# text = text.split('\n')
# text = text[1:-1]


### Part One ##################################################################

# next function (1)
def nxts(xl, yl, ch):
    if ch == 'J':
        x1c = xl
        y1c = yl - 1
        x2c = xl - 1
        y2c = yl
    elif ch == 'L':
        x1c = xl
        y1c = yl - 1
        x2c = xl + 1
        y2c = yl
    elif ch == '|':
        x1c = xl
        y1c = yl - 1
        x2c = xl
        y2c = yl + 1
    elif ch == '-':
        x1c = xl - 1
        y1c = yl
        x2c = xl + 1
        y2c = yl
    elif ch == '7':
        x1c = xl - 1
        y1c = yl
        x2c = xl
        y2c = yl + 1
    elif ch == 'F':
        x1c = xl + 1
        y1c = yl
        x2c = xl
        y2c = yl + 1
    return x1c, y1c, x2c, y2c

# next function (2)
def nxt(xl, yl, xc, yc, ch):
    if ch == 'J':
        if xl == xc - 1:
            xn = xc
            yn = yc - 1
        elif yl == yc - 1:
            xn = xc - 1
            yn = yc
    elif ch == 'L':
        if xl == xc + 1:
            xn = xc
            yn = yc - 1
        elif yl == yc - 1:
            xn = xc + 1
            yn = yc
    elif ch == '|':
        if yl == yc - 1:
            xn = xc
            yn = yc + 1
        elif yl == yc + 1:
            xn = xc
            yn = yc - 1
    elif ch == '-':
        if xl == xc - 1:
            xn = xc + 1
            yn = yc
        elif xl == xc + 1:
            xn = xc - 1
            yn = yc
    elif ch == '7':
        if xl == xc - 1:
            xn = xc
            yn = yc + 1
        elif yl == yc + 1:
            xn = xc - 1
            yn = yc
    elif ch == 'F':
        if xl == xc + 1:
            xn = xc
            yn = yc + 1
        elif yl == yc + 1:
            xn = xc + 1
            yn = yc
    return xn, yn

# remove linebreaks
text = [line.strip('\n') for line in text]

# locate S
S = [[c=='S' for c in line] for line in text]
y = [any(s) for s in S].index(True)
x = S[y].index(True)

# identify S
upper = False; left = False; right = False; lower = False
if text[y-1][x] in ['7', '|', 'F']: upper = True
if text[y][x-1] in ['L', '-', 'F']: left  = True
if text[y][x+1] in ['J', '-', '7']: right = True
if text[y+1][x] in ['J', '|', 'L']: lower = True
if upper and left:    S = 'J'
elif upper and right: S = 'L'
elif upper and lower: S = '|'
elif left  and right: S = '-'
elif lower and left:  S = '7'
elif lower and right: S = 'F'
else:                 S = '.'

# count steps
x1l, y1l = (x,y)
x2l, y2l = (x,y)
x1c, y1c, x2c, y2c = nxts(x, y, S)
steps   = 1
coords1 = [[x,y]]
coords2 = [[x,y]]
while ([x1c,y1c] != [x2c,y2c]) and ([x1c,y1c] not in coords1) and ([x2c,y2c] not in coords2):
    # print('Step {}: x1 = {}, y1 = {}; x2 = {}, y2 = {}'.format(steps, x1c, y1c, x2c, y2c))
    coords1.append([x1c, y1c])
    coords2.append([x2c, y2c])
    x1n, y1n = nxt(x1l, y1l, x1c, y1c, text[y1c][x1c])
    x2n, y2n = nxt(x2l, y2l, x2c, y2c, text[y2c][x2c])
    x1l, y1l = (x1c, y1c)
    x2l, y2l = (x2c, y2c)
    x1c, y1c = (x1n, y1n)
    x2c, y2c = (x2n, y2n)
    steps = steps + 1
print(steps)


### Part Two ##################################################################

# create loop
import numpy as np
import matplotlib.pyplot as plt
loop = np.zeros((len(text),len(text[0])))
off  = 1000
for i in range(len(coords1)):
    loop[coords1[i][1],coords1[i][0]] = +(i+off)/(steps+off)
    loop[coords2[i][1],coords2[i][0]] = -(i+off)/(steps+off)

# plot loop (1)
fig = plt.figure(figsize=(16,9))
ax  = fig.add_subplot(111)
for i in range(len(coords1)-1):
    ax.plot([coords1[i][0], coords1[i+1][0]], \
            [coords1[i][1], coords1[i+1][1]], '-b')
    ax.plot([coords2[i][0], coords2[i+1][0]], \
            [coords2[i][1], coords2[i+1][1]], '-b')

# plot loop (2)
fig = plt.figure(figsize=(16,9))
ax  = fig.add_subplot(111)
pcm = ax.pcolor(loop, cmap='bwr', vmin=-1, vmax=1)
ax.plot(x, y, '+k', linewidth=2, markersize=10)
ax.invert_yaxis()
ax.set_xlabel('column', fontsize=16)
ax.set_ylabel('row', fontsize=16)
ax.set_title('Advent of Code 2023, Day 10: Pipe Maze, Part 2', fontweight='bold', fontsize=20)
fig.colorbar(pcm, ax=ax)