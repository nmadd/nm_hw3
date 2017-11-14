# -*- coding: utf-8 -*-
from flow import Flow

# values = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
# utilities = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
# prices = [0, 0, 0]
#
# seedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3}, 'values': values, 'utilities': utilities}

def getMarketEquilibrium(seedData, prices):
    testGraph = Flow(seedData, prices, True)
    constSet = testGraph.findConstrictedSet()
    # print(constSet)
    prices = prices
    while len(constSet) > 0:
        for y in constSet:
            currentPrice = prices[y - 1]
            newPrice = currentPrice + 1
            prices[y - 1] = newPrice
        testGraph = Flow(seedData, prices, True)
        constSet = testGraph.findConstrictedSet()
    return testGraph.findPerfectMatching()
    # print(prices)

# getMarketEquilibrium(seedData, prices)
