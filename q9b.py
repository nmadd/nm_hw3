from market_equilib import getMarketEquilibrium
from copy import deepcopy
from vcg import VCG
file = open('q9b_logs.txt', 'w')

# Figure 7.3 from the notes:
q91values = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
q91prices = [0, 0, 0]
q91SeedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3}, 'values': q91values, 'utilities': deepcopy(q91values)}

file.write('Expected: A: 2, B: 1, C: 3, Actual: {}'.format(getMarketEquilibrium(q91SeedData, q91prices)))

q92values = {'A': [2, 4, 6, 8, 10], 'B': [10, 8, 6, 4, 2], 'C': [2, 2, 10, 2, 2], 'D': [3, 10, 3, 4, 5], 'E': [3, 9, 4, 5, 7]}
q92prices = [0, 0, 0, 0, 0]
q92SeedData = {'X': {'A', 'B', 'C', 'D', 'E'}, 'Y': {1, 2, 3, 4, 5}, 'values': q92values, 'utilities': deepcopy(q92values)}

file.write('\n Expected: A: 5, B: 1, C: 3, D: 2, E: 4, Actual: {}'.format(getMarketEquilibrium(q92SeedData, q92prices)))

q93values = {'A': [10, 20, 15], 'B': [0, 3, 2], 'C': [5, 7, 6]}
q93prices = [0, 0, 0]
q93SeedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3, 4, 5}, 'values': q93values, 'utilities': deepcopy(q93values)}

file.write('\n Expected: A: 2, B: 3, C: 1 Actual: {}'.format(getMarketEquilibrium(q93SeedData, q93prices)))

q94values = {'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15], 'D': [4, 8, 12, 16, 20], 'E': [5, 10, 15, 20, 25]}
q94prices = [0, 0, 0, 0, 0]
q94SeedData = {'X': {'A', 'B', 'C', 'D', 'E'}, 'Y': {1, 2, 3, 4, 5}, 'values': q94values, 'utilities': deepcopy(q94values)}

file.write('\n Expected: A: 1, B: 2, C: 3 D: 4 E: 5 Actual: {}'.format(getMarketEquilibrium(q94SeedData, q94prices)))
