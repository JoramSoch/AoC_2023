# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 9
https://adventofcode.com/2023/day/9
2023-12-09, 11:36; 2023-12-09, 11:43
"""


### Load Data #################################################################

# read input
filename = 'Day_09.txt'
f = open(filename)
text = f.readlines()

# example input
# text = ['0 3 6 9 12 15', \
#         '1 3 6 10 15 21', \
#         '10 13 16 21 30 45']

# difference function
def diff(nums):
    diffs = [nums[i+1]-nums[i] for i in range(len(nums)-1)]
    return diffs


### Part One ##################################################################

# analyze data
my_sum = 0
for line in text:
    
    # calculate differences
    diffs = []
    nums  = [int(s) for s in line.split()]
    diffs.append(nums)
    while not all([n==0 for n in nums]):
        nums  = diff(nums)
        diffs.append(nums)
    
    # predict next value
    number = sum([diffs[i][-1] for i in range(len(diffs)-1,-1,-1)])
    my_sum = my_sum + number

# output result
print(my_sum)


### Part Two ##################################################################

# analyze data
my_sum = 0
for line in text:
    
    # calculate differences
    diffs = []
    nums  = [int(s) for s in line.split()]
    diffs.append(nums)
    while not all([n==0 for n in nums]):
        nums  = diff(nums)
        diffs.append(nums)
    
    # predict first value
    number = 0
    for i in range(len(diffs)-1,-1,-1):
        number = diffs[i][0] - number
    my_sum = my_sum + number

# output result
print(my_sum)