##### Find exeternalities
# find externalities by removing player i and calculating the combined values v1 that all other players pay without A present
# then figure out the combined values v2 of all players with player i present
# the externality is eqwual to v1 - v2

##### Set player i's item price equal to the externality

##### Repeat for all players

# Source: figure 10.2
import copy

from flow import Flow
from q9 import getMarketEquilibrium
from vcg import VCG

values = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
utilities = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
prices = [0, 0, 0]

seedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3}, 'values': values, 'utilities': utilities}


print('sadasdsad', VCG(seedData, [0, 0, 0]))
