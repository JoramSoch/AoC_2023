# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 13
https://adventofcode.com/2023/day/13
2023-12-13, 07:16; 2023-12-13, 08:55
"""


### Load Data #################################################################

# read input
filename = 'Day_13.txt'
f = open(filename)
text = f.readlines()

# example input
# text = """
# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#
# """
# text = text.split('\n')
# text = text[1:-1]
# text = [line+'\n' for line in text]


### Part One ##################################################################

# remove linebreaks
text = [line[:-1] for line in text]
text.append('')

# analyze data
my_sum = 0
block  = []
for line in text:
    
    # if non-empty line
    if bool(line):
        
        # extract block
        block.append(line)
    
    # if empty line
    else:
        
        # analyze rows
        num_rows = [0 for i in range(len(block)-1)]
        for i in range(len(block)-1):
            mirror = True
            for j in range(0,min([i,len(block)-i-2])+1):
                row1 = block[i-j]
                row2 = block[i+1+j]
                if row1 != row2:
                    mirror = False
            if mirror:
                num_rows[i] = 2*len(range(0,min([i,len(block)-i-2])+1))
        if any(num_rows):
            num_rows = num_rows.index(max(num_rows)) + 1
        else:
            num_rows = 0
        
        # analyze columns
        num_cols = [0 for i in range(len(block[0])-1)]
        for i in range(len(block[0])-1):
            mirror = True
            for j in range(0,min([i,len(block[0])-i-2])+1):
                col1 = ''.join([row[i-j] for row in block])
                col2 = ''.join([row[i+1+j] for row in block])
                if col1 != col2:
                    mirror = False
            if mirror:
                num_cols[i] = 2*len(range(0,min([i,len(block[0])-i-2])+1))
        if any(num_cols):
            num_cols = num_cols.index(max(num_cols)) + 1
        else:
            num_cols = 0
        
        # reset block
        my_sum = my_sum + num_rows*100 + num_cols*1
        block  = []
        
# print result
print(my_sum)      


### Part Two ##################################################################

# analyze function
def analyze(block):

    # analyze rows
    num_rows = [0 for i in range(len(block)-1)]
    for i in range(len(block)-1):
        mirror = True
        for j in range(0,min([i,len(block)-i-2])+1):
            row1 = block[i-j]
            row2 = block[i+1+j]
            if row1 != row2:
                mirror = False
        if mirror:
            num_rows[i] = 2*len(range(0,min([i,len(block)-i-2])+1))
    if any(num_rows):
        num_rows = num_rows.index(max(num_rows)) + 1
    else:
        num_rows = 0
    
    # analyze columns
    num_cols = [0 for i in range(len(block[0])-1)]
    for i in range(len(block[0])-1):
        mirror = True
        for j in range(0,min([i,len(block[0])-i-2])+1):
            col1 = ''.join([row[i-j] for row in block])
            col2 = ''.join([row[i+1+j] for row in block])
            if col1 != col2:
                mirror = False
        if mirror:
            num_cols[i] = 2*len(range(0,min([i,len(block[0])-i-2])+1))
    if any(num_cols):
        num_cols = num_cols.index(max(num_cols)) + 1
    else:
        num_cols = 0
    
    # return results
    return [num_rows,num_cols]

# analyze data
import itertools
my_sum = 0
block  = []
for line in text:
    
    # if non-empty line
    if bool(line):
        
        # extract block
        block.append(line)
    
    # if empty line
    else:
        
        # fix smudge
        num_rows_cols = analyze(block)
        # print(num_rows_cols)
        for i,j in itertools.product(range(len(block)),range(len(block[0]))):
            block_ij    = block.copy()
            block_ij[i] = block_ij[i][:j] + '.#'[int(block_ij[i][j]=='.')] + block_ij[i][j+1:]
            num_rows_cols_ij = analyze(block_ij)
            if num_rows_cols_ij != num_rows_cols and num_rows_cols_ij != [0,0]:
                break
        
        # report no fix
        if i == len(block)-1 and j == len(block[0])-1:
            print(block)
            print(num_rows_cols)
            print(block_ij)
            print(num_rows_cols_ij)
            print()

        # calculate sum
        if num_rows_cols_ij == [0,0]:
            num_rows_cols_ij = num_rows_cols
        if num_rows_cols_ij != num_rows_cols:
            if num_rows_cols_ij[0] == num_rows_cols[0]: num_rows_cols_ij[0] = 0
            if num_rows_cols_ij[1] == num_rows_cols[1]: num_rows_cols_ij[1] = 0
        my_sum = my_sum + num_rows_cols_ij[0]*100 + num_rows_cols_ij[1]*1
        
        # reset block
        block  = []
        
# print result
print(my_sum)

# Note: The problem appears to be underspecified. For example, in the second
# pattern, why does entry (2,5) have to be changed, although changing entry
# (1,5) would give rise to the same result, i.e. horizontal reflection line
# between rows 1 and 2? The reason could be that with changing entry (1,5),
# the old horizontal reflection line between rows 4 and 5 would still be valid.
# But then, in the first pattern, the old vertical reflection line between
# columns 5 and 6 is still valid, but somehow does not count into the summary.
# What is the rule for deciding which one to pick? The example takes the new
# horizontal reflection line between rows 3 and 4, but it's not clear why.
# The vertical reflection line even binds more space than the horizontal
# reflection line (8 columns vs. 6 rows). My solution always uses "the new
# different reflection lines" and gives the correct result for the example,
# but not for the entire input.