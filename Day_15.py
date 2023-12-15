# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 15
https://adventofcode.com/2023/day/15
2023-12-15, 21:43; 2023-12-15, 22:26
"""


### Load Data #################################################################

# read input
filename = 'Day_15.txt'
f = open(filename)
text = f.readlines()
text = text[0][:-1]

# example input
# text = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'


### Part One ##################################################################

# analyze data
my_sum = 0
steps  = text.split(',')
for step in steps:
    value = 0
    for char in step:
        value = value + ord(char)
        value = value * 17
        value = value % 256
    my_sum = my_sum + value
print(my_sum)


### Part Two ##################################################################

# analyze data
boxes  = [{} for i in range(256)]
labels = [[] for i in range(256)]
for step in steps:
    # identify type
    if step.find('-') > -1: label = step[:step.find('-')]
    if step.find('=') > -1: label = step[:step.find('=')]
    # get box index
    index = 0
    for char in label:
        index = index + ord(char)
        index = index * 17
        index = index % 256
    # edit box contents
    if step.find('-') > -1:
        if label in labels[index]:
            labels[index].remove(label)
            boxes[index][label] = 0
    if step.find('=') > -1:
        focal = int(step[step.find('=')+1:])
        if label in labels[index]:
            boxes[index][label] = focal
        else:
            labels[index].append(label)
            boxes[index][label] = focal

# calculate focusing power
my_sum = 0
for i in range(256):
    for j, label in enumerate(labels[i]):
        my_sum = my_sum + (i+1) * (j+1) * boxes[i][label]
print(my_sum)