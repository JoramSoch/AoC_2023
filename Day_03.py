# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 3
https://adventofcode.com/2023/day/3
2023-12-06, 17:15; 2023-12-06, 17:47
"""


### Part One ##################################################################

# read input
filename = 'Day_03.txt'
f = open(filename)
text = f.readlines()

# analyze input
my_sum = 0
digits = '0123456789'
for i in range(len(text)):
    text[i] = '.'+text[i][:-1]+'.'
for i, line in enumerate(text):
    if i == 0: prv = '.'*len(line)
    else:      prv = text[i-1]
    if i == len(text)-1: nxt = '.'*len(line)
    else:                nxt = text[i+1]
    start = -1; stop = -1
    for j, c in enumerate(line):
        if c in digits and start == -1:
            start = j
        if start != -1 and line[j+1] not in digits:
            stop  = j+1
        if start != -1 and stop != -1:
            part  = False
            upper = prv[start-1:stop+1]
            lower = nxt[start-1:stop+1]
            left  = line[start-1]
            right = line[stop]
            if left != '.' or right != '.':
                part = True
            if any([u!='.' for u in upper]) or any([l!='.' for l in lower]):
                part = True
            if part:
                my_sum = my_sum + int(line[start:stop])
            start = -1; stop = -1
print(my_sum)


### Part Two ##################################################################

# read input
filename = 'Day_03.txt'
f = open(filename)
text = f.readlines()

# analyze input
my_sum = 0
digits = '0123456789'
for i in range(len(text)):
    text[i] = '.'+text[i][:-1]+'.'
for i, line in enumerate(text):
    if i == 0: prv = '.'*len(line)
    else:      prv = text[i-1]
    if i == len(text)-1: nxt = '.'*len(line)
    else:                nxt = text[i+1]
    start = -1
    stop  = -1
    for j, c in enumerate(line):
        if c == '*':
            left = False; right = False; upper = False; lower = False;
            u_l  = False; u_r   = False; l_l   = False; l_r   = False;
            if line[j-1] in digits: left  = True
            if line[j+1] in digits: right = True
            if prv[j] in digits:    upper = True
            else:
                if prv[j-1] in digits: u_l = True
                if prv[j+1] in digits: u_r = True
            if nxt[j] in digits:    lower = True
            else:
                if nxt[j-1] in digits: l_l = True
                if nxt[j+1] in digits: l_r = True
            if sum([left, right, upper, lower, u_l, u_r, l_l, l_r]) == 2:
                my_prod = 1
                if left:  my_prod = my_prod * int(line[line.rfind('.',0,j)+1 : j])
                if right: my_prod = my_prod * int(line[j+1 : line.find('.',j)])
                if upper: my_prod = my_prod * int(prv[prv.rfind('.',0,j)+1 : prv.find('.',j)])
                if u_l  : my_prod = my_prod * int(prv[prv.rfind('.',0,j)+1 : j])
                if u_r  : my_prod = my_prod * int(prv[j+1 : prv.find('.',j+1)])
                if lower: my_prod = my_prod * int(nxt[nxt.rfind('.',0,j)+1 : nxt.find('.',j)])
                if l_l  : my_prod = my_prod * int(nxt[nxt.rfind('.',0,j)+1 : j])
                if l_r  : my_prod = my_prod * int(nxt[j+1 : nxt.find('.',j+1)])
                my_sum = my_sum + my_prod
print(my_sum)