from vcg import VCG

q91values = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
q91utilities = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
q91prices = [0, 0, 0]

q91SeedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3}, 'values': q91values, 'utilities': q91utilities}

q92values = {'A': [2, 4, 6, 8, 10], 'B': [10, 8, 6, 4, 2], 'C': [2, 2, 10, 2, 2], 'D': [3, 10, 3, 4, 5], 'E': [3, 9, 4, 5, 7]}
q92utilities = {'A': [2, 4, 6, 8, 10], 'B': [10, 8, 6, 4, 2], 'C': [2, 2, 10, 2, 2], 'D': [3, 10, 3, 4, 5], 'E': [3, 9, 4, 5, 7]}
q92prices = [0, 0, 0, 0, 0]

q92SeedData = {'X': {'A', 'B', 'C', 'D', 'E'}, 'Y': {1, 2, 3, 4, 5}, 'values': q92values, 'utilities': q92utilities}

q93values = {'A': [10, 20, 15], 'B': [0, 3, 2], 'C': [5, 7, 6]}
q93prices = [0, 0, 0]

q93SeedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3, 4, 5}, 'values': q93values, 'utilities': deepcopy(q93values)}

print(VCG(q91SeedData))
