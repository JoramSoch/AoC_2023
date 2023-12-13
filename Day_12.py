# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 12
https://adventofcode.com/2023/day/12
2023-12-12, 23:18; 2023-12-13, 00:21
"""


### Load Data #################################################################

# read input
filename = 'Day_12.txt'
f = open(filename)
text = f.readlines()

# example input
# text = """
# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1
# """
# text = text.split('\n')
# text = text[1:-1]
# text = [line+'\n' for line in text]

# convert string to list of numbers
def str2list(my_str):
    my_list = [int(s) for s in my_str.split(',')]
    return my_list


### Part One ##################################################################

# remove linebreaks
text  = [line[:-1] for line in text]
combs = [0 for line in text]

# return observed condition records
def condrec(records):
    damaged     = []
    in_damage   = False
    num_damaged = 0
    records     = '.'+records+'.'
    for i in range(1,len(records)):
        if records[i] == '#':
            num_damaged = num_damaged + 1
            if not in_damage: in_damage = True
        if records[i] == '.' and records[i-1] == '#':
            damaged.append(num_damaged)
            num_damaged = 0
            in_damage   = False
    return damaged

# analyze data
# import itertools
from sympy.utilities.iterables import multiset_permutations
my_sum = 0
for i, line in enumerate(text):
    records = line[:line.find(' ')]
    damaged = line[line.find(' ')+1:]
    damaged = str2list(damaged)
    print('-> Line {}: records: {}; damaged: {}; '. \
          format(i+1, records, line[line.find(' ')+1:]), end='')
    # num_fs  = records.count('.')
    num_ht  = records.count('#')
    num_qm  = records.count('?')
    missing = '#'*(sum(damaged)-num_ht) + '.'*(num_qm-(sum(damaged)-num_ht))
    # perms = set(itertools.permutations(missing))
    perms   = list(multiset_permutations(missing))
    compat  = 0
    print('permutations: {}; ... '.format(len(perms)), end='')
    for p in perms:
        records_p = list(records)
        q         = -1
        for j in range(len(records_p)):
            if records_p[j] == '?':
                q = q + 1
                records_p[j] = p[q]
        records_p = ''.join(records_p)
        damaged_p = condrec(records_p)
        if damaged_p == damaged:
            compat = compat + 1
    my_sum   = my_sum + compat
    combs[i] = compat
    print('compatible: {}.'.format(compat))
print(my_sum)


### Part Two ##################################################################

# analyze data
from sympy.utilities.iterables import multiset_permutations
my_sum = 0
for i, line in enumerate(text):
    records = line[:line.find(' ')]
    damaged = line[line.find(' ')+1:]
    print('-> Line {}: before unfolding: {}; ... '.format(i+1, combs[i]), end='')
    records = '?'.join([records]*2)
    damaged = ','.join([damaged]*2)
    damaged = str2list(damaged)
    num_ht  = records.count('#')
    num_qm  = records.count('?')
    missing = '#'*(sum(damaged)-num_ht) + '.'*(num_qm-(sum(damaged)-num_ht))
    perms   = list(multiset_permutations(missing))
    r_list  = list(records)
    compat  = 0
    for p in perms:
        records_p    = r_list
        records_p    = ['.']+records_p+['.']
        damaged_p    = []
        in_damage    = False
        num_damaged  = 0
        compatible   = True
        num_replaced = -1
        for j in range(1,len(records_p)):
            if records_p[j] == '?':
                num_replaced = num_replaced + 1
                records_p[j] = p[num_replaced]
            if records_p[j] == '#':
                num_damaged = num_damaged + 1
                if not in_damage: in_damage = True
            if records_p[j] == '.' and records_p[j-1] == '#':
                damaged_p.append(num_damaged)
                num_damaged = 0
                in_damage   = False
                if damaged_p != damaged[:len(damaged_p)]:
                    compatible = False
                    break
        if compatible:
            compat = compat + 1
    print('after unfolding twice: {}; '.format(compat), end='')
    compat = compat * int(compat/combs[i])**3
    print('after unfolding 5-times: {}.'.format(compat))
    my_sum = my_sum + compat
print(my_sum)