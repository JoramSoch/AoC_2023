# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 1
https://adventofcode.com/2023/day/1
2023-12-04, 15:45; 2023-12-04, 23:35; 2023-12-09, 12:11
"""


### Load Data #################################################################

# read input
filename = 'Day_01.txt'
f = open(filename)
text = f.readlines()

# example input (1)
# text = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']

# example input (2)
# text = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']


### Part One ##################################################################

# analyze input
my_sum = 0
for line in text:
    digits = [c for c in line if c in '0123456789']
    number = int(digits[0]+digits[-1])
    my_sum = my_sum + number
print(my_sum)


### Part Two ##################################################################

# analyze input
my_sum  = 0
digits  =  '123456789'
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for line in text:
    num_chars = len(line)
    first = ''
    last  = ''
    found = False
    for i in range(num_chars):
        if line[i] in digits:
            first = line[i]
            found = True
        for j, number in enumerate(numbers):
            if line[i:(i+len(number))] == number:
                first = str(j+1)
                found = True
        if found: break
    found = False
    for i in range(num_chars-1,-1,-1):
        if line[i] in digits:
            last = line[i]
            found = True
        for j, number in enumerate(numbers):
            if line[i:(i+len(number))] == number:
                last = str(j+1)
                found = True
        if found: break
    number = int(first+last)
    my_sum = my_sum + number
print(my_sum)