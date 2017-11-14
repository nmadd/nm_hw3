##### Find exeternalities
# find externalities by removing player i and calculating the combined values v1 that all other players pay without A present
# then figure out the combined values v2 of all players with player i present
# the externality is eqwual to v1 - v2

##### Set player i's item price equal to the externality

##### Repeat for all players

# Source: figure 10.2
import copy

from flow import Flow

values = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
utilities = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
prices = [0, 0, 0]

seedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3}, 'values': values, 'utilities': utilities}

def getMarketEquilibrium(seedData, prices):
    testGraph = Flow(seedData, prices, True)
    constSet = testGraph.findConstrictedSet()
    print(constSet)
    prices = prices
    while len(constSet) > 0:
        for y in constSet:
            currentPrice = prices[y - 1]
            newPrice = currentPrice + 1
            prices[y - 1] = newPrice
        testGraph = Flow(seedData, prices, True)
        constSet = testGraph.findConstrictedSet()
    return testGraph.findPerfectMatching()
    print(prices)
    # return prices

def VCG():
    vcgPrices = {}
    matches = getMarketEquilibrium(seedData, [0, 0, 0])
    present = 0
    notPresent = 0
    for person in matches:
        print('sdASfsdfasz', person)
        # with person present
        for p in values.keys():
            if p != person:
                present += values[p][matches[p] -1]
        # without person present
        newSeedData = copy.deepcopy(seedData)
        newSeedData['X'].remove(person)
        augmentedMatches = getMarketEquilibrium(newSeedData, [0, 0, 0])
        print('augy', augmentedMatches)
        for j in values.keys():
            print(j)
            if j != person:
                notPresent += values[j][augmentedMatches[j] -1]
        print(present)
        print(notPresent)
        vcgPrices[matches[person]] = notPresent - present
        present = 0
        notPresent = 0
    print('VCG', vcgPrices)

VCG()
