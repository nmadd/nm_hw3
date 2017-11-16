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
                # get person's value for their match, which is (stupidly) accessed at a specific index, aka matches[p] - 1
                present += seedData['values'][p][matches[p] -1]
        # without person present
        newSeedData = copy.deepcopy(seedData)
        newSeedData['X'].remove(person)
        # find new matches without them present
        augmentedMatches = getMarketEquilibrium(newSeedData, [0 for i in range(0, len(prices))])
        for j in augmentedMatches.keys():
            if j != person:
                # get person's value for their match, which is (stupidly) accessed at a specific index, aka matches[p] - 1
                notPresent += seedData['values'][j][augmentedMatches[j] -1]
        vcgPrices[matches[person]] = notPresent - present
        present = 0
        notPresent = 0
    return {'matches': matches, 'prices': vcgPrices}
