# -*- coding: utf-8 -*-
from edge import Edge
import random
import sys

sys.setrecursionlimit(5000)

class Flow:
    def __init__(self, graphSeedData, prices, directed=False):
        self.graph = {}
        self.graphSeedData = graphSeedData
        self.X = graphSeedData['X']
        self.Y = graphSeedData['Y']
        self.values = graphSeedData['values']
        self.utilities = graphSeedData['utilities']
        self.prices = prices
        self.flow = 0
        self.paths = None
        self.maxUtils = None
        # boolean to flag if graph is directed or undirected
        self.directed = directed
        self.initGraph()

    def addNode(self, node):
        self.graph[node] = []

    def addEdge(self, source, sink, capacity):
        newEdge = Edge(source, sink, capacity)
        newReverseEdge = Edge(sink, source, capacity) if self.directed == False else Edge(sink, source, 0)
        newEdge.reverseEdge = newReverseEdge
        newReverseEdge.reverseEdge = newEdge
        self.graph[source].append(newEdge)
        self.graph[sink].append(newReverseEdge)

    # create a graph of x size and with y probability that each node is connected
    def initGraph(self):
        self.addNode('s')
        self.addNode('t')
        for node in self.graphSeedData['X']:
            self.addNode(node)
            self.addEdge('s', node, 1)
        for node in self.graphSeedData['Y']:
            self.addNode(node)
            self.addEdge(node, 't', 1)

    def printGraph(self):
        print('GRAPH', self.graph)

    def getGraph(self):
        return self.graph

    def getMaxUtils(self):
        maxUtils = {}
        for person in self.X:
            # {key: None, val: 0}
            newUtils = []
            for i in range(len(self.values[person])):
                # print('MAX UTILS', maxUtils)
                utility = self.values[person][i] - self.prices[i]
                newUtils.append(utility)
                if person not in maxUtils:
                    maxUtils[person] = []
                if len(maxUtils[person]) == 0:
                    maxUtils[person].append({'key': i + 1, 'val': utility})
                elif utility > maxUtils[person][0]['val']:
                    maxUtils[person] = [{'key': i + 1, 'val': utility}]
                elif utility == maxUtils[person][0]['val']:
                    maxUtils[person].append({'key': i + 1, 'val': utility})
            self.utilities[person] = newUtils
        return maxUtils


    def match(self, maxUtils):
        for x in maxUtils.keys():
            for i in range(len(maxUtils[x])):
                # print(maxUtils[x][i])
                self.addEdge(x, maxUtils[x][i]['key'], 100000000000)



    def get_path(self, source, sink, path, visited_paths):
        # base case
        if source == sink:
            return path
        for edge in self.graph[source]:
            residual = edge.capacity - edge.flow
            # check that vert has not been previously visited (keep moving forward)
            if residual > 0 and edge.sink not in visited_paths:
                visited_paths.add(source)
                result = self.get_path(edge.sink, sink, path + [(edge, residual)], visited_paths)
                if result != None:
                    return result

    def maxFlow(self, source, sink):
        result = 0
        path = self.get_path(source, sink, [], set())
        paths = []
        while path != None:
            flow = min(residual for edge, residual in path) if len(path) > 0 else 0
            for edge, res in path:
                edge.flow += flow
                edge.reverseEdge.flow -= flow
            result += flow
            paths.append(path)
            path = self.get_path(source, sink, [], set())
        # print('PATHS', paths)
        self.paths = paths
        return {'result': result, 'paths': paths}

    def returnConstrictedSet(self, maxFlow, maxUtils):
        # print('SDJNKSDKSD', maxFlow['paths'])
        # pathsWithFlow = [x['sink'] for x in  maxFlow['paths'] ]
        constrictedSet = set()
        matchedPeople = []
        for path in maxFlow['paths']:
            for edge in path:
                if edge[0].source in self.X:
                    matchedPeople.append(edge[0].source)
        for person in self.X:
            if person not in matchedPeople:
                for util in maxUtils[person]:
                    constrictedSet.add(util['key'])
        # print('CONSTRICTED', constrictedSet)
        file = open('q9a_logs.txt', 'w')
        return constrictedSet

    def raisePrices(self, constrictedSet, prices):
        for y in constrictedSet:
            currentPrice = prices[y]
            newPrice = currentPrice + 1
            prices[y] = newPrice

    def findPerfectMatching(self):
        perfectMatchings = {}
        for path in self.paths:
            for edge in path:
                if edge[0].source in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
                    perfectMatchings[edge[0].source] = edge[0].sink
        return perfectMatchings

    def findConstrictedSet(self):
        savedMaxUtils = self.getMaxUtils()
        self.match(savedMaxUtils)
        savedMaxFlow = self.maxFlow('s', 't')
        return self.returnConstrictedSet(savedMaxFlow, savedMaxUtils)
