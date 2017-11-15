from q11a import constructGraph, constructPrices
from vcg import VCG
from copy import deepcopy
from random import shuffle
import numpy as np
file = open('q11b_logs.txt', 'w')
file2 = open('q11c_logs.txt', 'w')

testGraph = constructGraph(20)
permutedGraph = deepcopy(testGraph)
print('VALS', permutedGraph['values'])
newValues = {}
for key in permutedGraph['values'].keys():
    shuffledValues = np.random.permutation(permutedGraph['values'][key])
    newValues[key] = shuffledValues
permutedGraph['values'] = newValues

print('testGraph', testGraph['values']['A'])
print('permutedGraph', permutedGraph['values']['A'])


file.write(str(VCG(testGraph, constructPrices(20))))
file2.write(str(VCG(permutedGraph, constructPrices(20))))
