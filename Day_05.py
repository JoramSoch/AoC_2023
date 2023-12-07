# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 5
https://adventofcode.com/2023/day/5
2023-12-07, 10:41; 2023-12-07, 12:53
"""


### Load Data #################################################################

# read input
filename = 'Day_05.txt'
f = open(filename)
text = f.readlines()

# example input
# text = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""
# text = text.split('\n')
# text = [line+'\n' for line in text]

# extract numbers
def str2list(my_str):
    my_list = [int(n) for n in my_str.split()]
    return my_list

# convert seeds
def src2dest(text, src, out=False):
    for i, line in enumerate(text):
        if line.find('map:') > -1:
            if out:
                print('\n'+line, end='')
                print('- source: {}'.format(src))
            dest = [-1 for s in src]
            j    = i+1
            while j < len(text) and text[j] != '\n':
                rng = str2list(text[j][:-1])
                for k in range(len(src)):
                    if src[k] >= rng[1] and src[k] < rng[1]+rng[2]:
                        dest[k] = rng[0] + (src[k]-rng[1])
                j = j + 1
            for k in range(len(dest)):
                if dest[k] == -1: dest[k] = src[k]
            src = dest
            if out:
                print('- destination: {}'.format(src))
    return dest


### Part One ##################################################################

# extract & convert seeds
seeds = str2list(text[0][text[0].find(':')+2 : -1])
loc   = src2dest(text, seeds, out=True)

# report lowest location
print('\nlowest location number:')
print('- seed {}: location {}'.format(loc.index(min(loc))+1, min(loc)))


### Part Two ##################################################################

# get seed ranges
import random
seeds_rng = [int(n) for n in text[0][text[0].find(':')+2 : len(text[0])].split()]
num_rnd   = int(1e3)            # number of random seeds for all ranges
step_size = int(1e3)            # initial step size for lowest ranges

# for all ranges
print('\nlowest location numbers (all ranges):')
for h in range(int(len(seeds_rng)/2)):
    
    # draw & convert seeds
    seeds = [random.randint(seeds_rng[h*2], seeds_rng[h*2]+seeds_rng[h*2+1]-1) for x in range(num_rnd)]
    loc   = src2dest(text, seeds)
            
    # report lowest location
    low = min(loc)
    if 'lowest' not in globals():
        lowest = low; h_lowest = h
    else:
        if low < lowest: lowest = low; h_lowest = h
    print('- range {}, seed {}: location {}'.format(h+1, loc.index(low)+1, low))
print('- overall lowest: location {}'.format(lowest))

# for lowest range
print('\nlowest location numbers (range {} only):'.format(h_lowest+1))
start = seeds_rng[h_lowest*2]
stop  = seeds_rng[h_lowest*2]+seeds_rng[h_lowest*2+1]
while step_size >= 1:

    # specify & convert seeds
    seeds = list(range(start, stop, step_size))
    loc   = src2dest(text, seeds)
            
    # report lowest location
    low = min(loc)
    ind = loc.index(low)
    print('- seeds = {}, ..., {}, step size = {}: location {}'.format(start, stop, step_size, low))
    
    # specify new range
    start = seeds[max([ind-10,0])]
    stop  = seeds[min([ind+10,len(seeds)-1])]
    step_size = int(step_size/10)
    lowest    = low
    
# report overall lowest
print('- overall lowest: location {}'.format(lowest))