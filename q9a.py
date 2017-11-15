from market_equilib import getMarketEquilibrium
from copy import deepcopy
from vcg import VCG
from flow import Flow
file = open('q9a_logs.txt', 'w')

# Figure 7.3 from the notes:
q91values = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
q91prices = [0, 0, 0]
q91SeedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3}, 'values': q91values, 'utilities': deepcopy(q91values)}

testGraph = Flow(q91SeedData, q91prices)
file.write('Expected Constricted Set: 2, Actual: {}'.format(testGraph.findConstrictedSet()))

# Figure 7.3 from the notes:
q92values = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
q92prices = [0, 1, 0]
q92SeedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3}, 'values': q92values, 'utilities': deepcopy(q92values)}

testGraph2 = Flow(q92SeedData, q92prices)
print(testGraph2.findConstrictedSet())
file.write('\nExpected Constricted Set: 2,3 Actual: {}'.format(testGraph2.findConstrictedSet()))

# Figure 7.3 from the notes:
q93values = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
q93prices = [0, 2, 1]
q93SeedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3}, 'values': q93values, 'utilities': deepcopy(q93values)}

testGraph3 = Flow(q93SeedData, q93prices)
print(testGraph3.findConstrictedSet())
file.write('\nExpected Constricted Set: 2,3 Actual: {}'.format(testGraph3.findConstrictedSet()))

# Figure 7.3 from the notes:
q94values = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
q94prices = [0, 3, 2]
q94SeedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3}, 'values': q94values, 'utilities': deepcopy(q94values)}

testGraph4 = Flow(q94SeedData, q94prices)
print(testGraph4.findConstrictedSet())
print(testGraph4.findPerfectMatching())
file.write('\nExpected Constricted Set: None Actual: {}'.format(testGraph4.findConstrictedSet()))
