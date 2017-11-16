from q11a import constructGraph, constructPrices
from vcg_bundles import VCG
from copy import deepcopy
from random import shuffle
import numpy as np
file = open('q11b_logs.txt', 'w')
file2 = open('q11c_logs.txt', 'w')

testGraph = constructGraph(20)
permutedGraph = deepcopy(testGraph)
newValues = {}
for key in permutedGraph['values'].keys():
    shuffledValues = np.random.permutation(permutedGraph['values'][key])
    newValues[key] = shuffledValues
permutedGraph['values'] = newValues



answers11b = VCG(testGraph, constructPrices(20))
file.write('Prices:')
for item in answers11b['prices']:
    file.write('\nBundle: {} Price: {}'.format(item, answers11b['prices'][item]))

file.write('\n')
file.write('Matches:')
for match in answers11b['matches']:
    file.write('\nX: {} Y: {}'.format(match, answers11b['matches'][match]))


# file.write(str(VCG(testGraph, constructPrices(20))))
answers11c = VCG(permutedGraph, constructPrices(20))
file2.write(str(VCG(permutedGraph, constructPrices(20))))

file2.write('Prices:')
for item in answers11c['prices']:
    file2.write('\nBundle: {} Price: {}'.format(item, answers11c['prices'][item]))

file2.write('\n')
file2.write('Matches:')
for match in answers11c['matches']:
    file2.write('\nX: {} Y: {}'.format(match, answers11c['matches'][match]))
