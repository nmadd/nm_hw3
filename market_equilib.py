# -*- coding: utf-8 -*-
from flow import Flow

# values = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
# utilities = {'A': [4, 12, 5], 'B': [7, 10, 9], 'C': [7, 7, 10]}
# prices = [0, 0, 0]
#
# seedData = {'X': {'A', 'B', 'C'}, 'Y': {1, 2, 3}, 'values': values, 'utilities': utilities}

def getMarketEquilibrium(seedData, prices):
    # initialize the graph and find the constritcted set of items
    testGraph = Flow(seedData, prices, True)
    constSet = testGraph.findConstrictedSet()
    # print(constSet)
    prices = prices
    while len(constSet) > 0:
        # raise the price by 1 for every item in the constricted set
        for y in constSet:
            currentPrice = prices[y - 1]
            newPrice = currentPrice + 1
            prices[y - 1] = newPrice
        if min(prices) > 0:
            downShiftedPrices = [p - 1 for p in prices]
            print('SHIFTING', prices, downShiftedPrices)
            prices = downShiftedPrices
        testGraph = Flow(seedData, prices, True)
        constSet = testGraph.findConstrictedSet()
    return testGraph.findPerfectMatching()
    # print(prices)

# getMarketEquilibrium(seedData, prices)
