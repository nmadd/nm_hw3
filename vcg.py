import copy
from flow import Flow
from q9 import getMarketEquilibrium

def VCG(seedData, prices):
    vcgPrices = {}
    matches = getMarketEquilibrium(seedData, prices)
    present = 0
    notPresent = 0
    for person in matches:
        # print('sdASfsdfasz', person)
        # with person present
        for p in seedData['values'].keys():
            if p != person:
                present += seedData['values'][p][matches[p] -1]
        # without person present
        newSeedData = copy.deepcopy(seedData)
        newSeedData['X'].remove(person)
        augmentedMatches = getMarketEquilibrium(newSeedData, prices)
        # print('augy', augmentedMatches)
        for j in seedData['values'].keys():
            # print(j)
            if j != person:
                notPresent += seedData['values'][j][augmentedMatches[j] -1]
        # print(present)
        # print(notPresent)
        vcgPrices[matches[person]] = notPresent - present
        present = 0
        notPresent = 0
    return vcgPrices
