# -*- coding: utf-8 -*-
"""
Advent of Code 2023, Day 7
https://adventofcode.com/2023/day/7
2023-12-07, 22:59; 2023-12-08, 12:18
"""


### Load Data #################################################################

# read input
filename = 'Day_07.txt'
f = open(filename)
text = f.readlines()

# example input
# text = ['32T3K 765\n', \
#         'T55J5 684\n', \
#         'KK677 28\n', \
#         'KTJJT 220\n', \
#         'QQQJA 483\n']


### Part One ##################################################################

# prepare analysis
import numpy as np
cards = 'AKQJT98765432'
games = len(text)
hands = np.zeros((games,7), dtype=int)

# analyze games
for i, line in enumerate(text):
    # segment line
    parts      = line.split()
    hand       = parts[0]
    hands[i,6] = int(parts[1])
    unique     = list(set(hand))
    occs       = [sum([h==c for h in hand]) for c in unique]
    # analyze type
    if (len(unique) == 1):
        hands[i,0] = 1
    elif (len(unique) == 2) and (4 in occs):
        hands[i,0] = 2
    elif (len(unique) == 2) and (3 in occs):
        hands[i,0] = 3
    elif (len(unique) == 3) and (3 in occs):
        hands[i,0] = 4
    elif (len(unique) == 3) and (1 in occs):
        hands[i,0] = 5
    elif (len(unique) == 4):
        hands[i,0] = 6
    else:
        hands[i,0] = 7
    # analyze cards
    for j in range(1,len(hand)+1):
        hands[i,j] = cards.index(hand[j-1])

# sort hands by quality
ind        = np.lexsort((hands[:,5], hands[:,4], hands[:,3], hands[:,2], hands[:,1], hands[:,0]))
hands_sort = hands[ind,:]

# calculate total winnings
tot_win = sum([(games-i)*hands_sort[i,6] for i in range(games)])
print(tot_win)


### Part Two ##################################################################

# prepare analysis
import numpy as np
cards = 'AKQT98765432J'

# analyze games
for i, line in enumerate(text):
    # segment line
    parts = line.split()
    hand  = parts[0]
    # analyze type
    for card in cards:
        hand_J = hand.replace('J',card)
        unique = list(set(hand_J))
        occs   = [sum([h==c for h in hand_J]) for c in unique]
        if (len(unique) == 1):
            type_J = 1
        elif (len(unique) == 2) and (4 in occs):
            type_J = 2
        elif (len(unique) == 2) and (3 in occs):
            type_J = 3
        elif (len(unique) == 3) and (3 in occs):
            type_J = 4
        elif (len(unique) == 3) and (1 in occs):
            type_J = 5
        elif (len(unique) == 4):
            type_J = 6
        else:
            type_J = 7
        # if improvement
        if type_J < hands[i,0]:
            hands[i,0] = type_J
    # analyze cards
    for j in range(1,len(hand)+1):
        hands[i,j] = cards.index(hand_J[j-1])

# sort hands by quality
ind        = np.lexsort((hands[:,5], hands[:,4], hands[:,3], hands[:,2], hands[:,1], hands[:,0]))
hands_sort = hands[ind,:]

# calculate total winnings
tot_win = sum([(games-i)*hands_sort[i,6] for i in range(games)])
print(tot_win)