# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 18
https://adventofcode.com/2023/day/18
2023-12-18, 21:53; 2023-12-19, 00:46
"""


### Load Data #################################################################

# read input
filename = 'Day_18.txt'
f = open(filename)
text = f.readlines()
text = [line[:-1] for line in text]

# example input
# text = """
# R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)
# """
# text = text.split('\n')
# text = text[1:-1]


### Part One ##################################################################

# generate map
import numpy as np
N   = 600
x   = int(N/2-1)
y   = int(N/2-1)
dig = np.zeros((N,N))
dig[y,x] = 1
for line in text:
    parts = line.split()
    steps = int(parts[1])
    for j in range(steps):
        if parts[0] == 'U':
            y = y - 1
        if parts[0] == 'R':
            x = x + 1
        if parts[0] == 'D':
            y = y + 1
        if parts[0] == 'L':
            x = x - 1
        dig[y,x] = 1

# # fill area (left to right)
# dig1 = dig.copy()
# for i in range(N):
#     ss = 0
#     for j in range(1,N):
#         if dig1[i,j] == 1 and dig1[i,j-1] != 1:
#             ss = ss + 1
#         if dig1[i,j] == 0 and ss % 2 == 1:
#             dig1[i,j] = -1

# # fill area (top to bottom)
# dig2 = dig.copy()
# for j in range(N):
#     ss = 0
#     for i in range(1,N):
#         if dig2[i,j] == 1 and dig2[i-1,j] != 1:
#             ss = ss + 1
#         if dig2[i,j] == 0 and ss % 2 == 1:
#             dig2[i,j] = -1

# # visualize fillings
# import matplotlib.pyplot as plt
# fig = plt.figure(figsize=(16,9))
# axs = fig.subplots(1,2)
# for i in range(2):
#     if i == 0: pcm = axs[i].pcolor(dig1, cmap='bwr', vmin=-1, vmax=1)
#     if i == 1: pcm = axs[i].pcolor(dig2, cmap='bwr', vmin=-1, vmax=1)
#     axs[i].invert_yaxis()
#     axs[i].set_xlabel('column', fontsize=16)
#     axs[i].set_ylabel('row', fontsize=16)
#     if i == 0: axs[i].set_title('AoC 2023, Day 18: Lavaduct Lagoon, Part 1', fontweight='bold', fontsize=20)
#     fig.colorbar(pcm, ax=axs[i])

# save grid as image
import imageio
imageio.imsave('Day_18_(1).png', dig)

# edit and load image
# Fill black area inside white lines with red color.
img = imageio.imread('Day_18_(2).png')

# output result
my_sum = 0
for i in range(N):
    for j in range(N):
        if np.any(img[i,j,0:3] != np.array([0,0,0])):
            my_sum = my_sum + 1
print(my_sum)


### Part Two ##################################################################

# generate map
import numpy as np
N   = 10000
x   = int(N/2-1)
y   = int(N/2-1)
dig = np.zeros((N,N))
dig[y,x] = 1
dirs     = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
for line in text:
    parts = line.split()
    steps = int(parts[2][2:-2], 16)
    dirl  = dirs[parts[2][-2]]
    for j in range(steps):
        if dirl == 'U':
            y = y - 1
        if dirl == 'R':
            x = x + 1
        if dirl == 'D':
            y = y + 1
        if dirl == 'L':
            x = x - 1
        dig[y,x] = 1