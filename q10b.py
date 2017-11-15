##### Find exeternalities
# find externalities by removing player i and calculating the combined values v1 that all other players pay without A present
# then figure out the combined values v2 of all players with player i present
# the externality is eqwual to v1 - v2

##### Set player i's item price equal to the externality

##### Repeat for all players

# Source: figure 10.2
from copy import deepcopy

from flow import Flow
from q9 import getMarketEquilibrium
from vcg import VCG
file = open('q10b_logs.txt', 'w')

values = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
utilities = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
prices = [0, 0, 0]
seedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3}, 'values': values, 'utilities': utilities}

q92values = {'A': [2, 4, 6, 8, 10], 'B': [10, 8, 6, 4, 2], 'C': [2, 2, 10, 2, 2], 'D': [3, 10, 3, 4, 5], 'E': [3, 9, 4, 5, 7]}
q92prices = [0, 0, 0, 0, 0]
q92SeedData = {'X': {'A', 'B', 'C', 'D', 'E'}, 'Y': {1, 2, 3, 4, 5}, 'values': q92values, 'utilities': deepcopy(q92values)}

# file.write('\n Expected: A: 5, B: 1, C: 3, D: 2, E: 4, Actual: {}'.format(getMarketEquilibrium(q92SeedData, q92prices)))

q93values = {'A': [10, 20, 15], 'B': [0, 3, 2], 'C': [5, 7, 6]}
q93prices = [0, 0, 0]
q93SeedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3, 4, 5}, 'values': q93values, 'utilities': deepcopy(q93values)}


file.write('VCG prices: ' + str(VCG(seedData, [0, 0, 0])))
file.write('\n' + 'VCG prices: ' + str(VCG(q92SeedData, [0, 0, 0, 0, 0])))
file.write('\n' + 'VCG prices: ' + str(VCG(q93SeedData, [0, 0, 0])))
