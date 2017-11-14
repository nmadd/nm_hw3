values = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
utilities = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
prices = [0, 0, 0]

seedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3}, 'values': values, 'utilities': utilities}
from random import randint
from copy import deepcopy
def constructGraph(size):
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    values = {}
    X = set()
    Y= set()
    for i in range(0, size):
        letter = ascii_uppercase[i]
        X.add(letter)
        Y.add(i + 1)
        values[letter] = []
        # assign random values per good
        for i in range (0, size):
            values[letter].append(randint(0, 50))
    utilities = deepcopy(values)
    graph = {'X': X, 'Y': Y, 'values': values, 'utilities': utilities}
    return graph

def constructPrices(size):
    prices = [0 for i in range(0, size)]
    return prices
