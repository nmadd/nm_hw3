import copy
from flow import Flow
from market_equilib import getMarketEquilibrium

def VCG(seedData, prices):
    vcgPrices = {}
    matches = getMarketEquilibrium(seedData, prices)
    present = 0
    notPresent = 0
    for person in matches:
        # with person present
        for p in seedData['values'].keys():
            if p != person:
                present += seedData['values'][p][matches[p] -1]
        # without person present
        newSeedData = copy.deepcopy(seedData)
        newSeedData['X'].remove(person)
        augmentedMatches = getMarketEquilibrium(newSeedData, [0 for i in range(0, len(prices))])
        for j in augmentedMatches.keys():
            if j != person:
                notPresent += seedData['values'][j][augmentedMatches[j] -1]
        vcgPrices[matches[person]] = notPresent - present
        present = 0
        notPresent = 0
    return vcgPrices
