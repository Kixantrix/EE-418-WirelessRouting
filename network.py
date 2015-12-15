#!/usr/bin/python

import networkx as nx
import random
import math


# noinspection PyPep8Naming
class Network:
    def __init__(self, size, width, keyPoolSize, keysPerNode, commRange):
        self.G = nx.Graph()  # Graph of nodes
        self.size = size  # Number of nodes in graph
        self.width = width  # Width in meters of sides
        self.keyPoolSize = keyPoolSize  # Number of keys in total pool
        self.keysPerNode = keysPerNode  # Number of pools per node
        self.commRange = commRange  # Range in meters of communication
        # Generate all nodes within the network
        self.genNodes()
        # Add edges for all nodes which are in range of each other
        self.addEdges()
        # Add calculated LKVM values
        self.calcAllLKVM()

    # Calculates all lkvm values and stores them to each node
    def calcAllLKVM(self):
        for edge in self.G.edges():
            self.calcLKVM(edge)

    # Calculates all WLPVM values based on already calculated LKVM and l
    def calcAllWLPVM(self, l):
        for edge in self.G.edges():
            self.calcWLPVM(edge, l)

    # Calculates all TPVM values based on already calculated LKVM and gamma
    def calcAllTPVM(self, gamma):
        for edge in self.G.edges():
            self.calcTPVM(edge, gamma)

    # # Calculates lkvm for an edge and stores it to the edge
    # def calcLKVM(self, edge):
    #     i = edge[0]
    #     j = edge[1]
    #     iKeys = self.G.nodes(1)[i][1]['keys']
    #     jKeys = self.G.nodes(1)[j][1]['keys']
    #     # Find shared keys along edge
    #     sharedKeys = iKeys.intersection(jKeys)
    #     # Empty set to keys acquired until same as shared keys
    #     c = set()
    #     # lkvm cost to add to
    #     lkvm = 0
    #     # Iterate while sharedKeys aren't within c
    #     while not sharedKeys.issubset(c):
    #         randNodeIndex = random.randint(0, self.size - 1)
    #         c= c.union(self.G.nodes(1)[randNodeIndex][1]['keys'])
    #         lkvm += 1
    #     self.G[i][j]['lkvm'] = lkvm
    #     self.G[i][j]['keys'] = sharedKeys

    # Calculates lkvm for an edge and stores it to the edge
    def calcLKVM(self, edge):
        i = edge[0]
        j = edge[1]
        iKeys = self.G.nodes(1)[i][1]['keys']
        jKeys = self.G.nodes(1)[j][1]['keys']
        # Find shared keys along edge
        sharedKeys = iKeys.intersection(jKeys)
        # lkvm cost to add to
        lkvm = 0
        # Increment for every node which has an intersection
        numSharedNodes = 0
        N = len(self.G.nodes())
        for node in self.G.nodes(1):
            intersection = sharedKeys.intersection(node[1]['keys'])
            if bool(intersection):
                cardT = len(intersection)
                lkvm += 2 * ((cardT) % 2) - 1
                numSharedNodes += 1
        self.G[i][j]['lkvm'] = 1.0 * N * lkvm / numSharedNodes
        self.G[i][j]['keys'] = sharedKeys

    # Generates the nodes within the network
    def genNodes(self):
        for i in range(self.size):
            self.addNewNode(i)

    # Adds a new node to the graph with random values within parameters
    def addNewNode(self, index):
        x = random.randint(0, self.width)
        y = random.randint(0, self.width)
        keys = set()
        while len(keys) < self.keysPerNode:
            keys.add(random.randint(0, self.keyPoolSize))
        self.G.add_node(index, x=x, y=y, keys=keys)

    # Adds edges for all nodes which are in range of each other
    def addEdges(self):
        for node in self.G.nodes(1):
            for otherNode in self.G.nodes(1):
                keys1 = node[1]['keys']
                keys2 = otherNode[1]['keys']
                # Add edge if not the same node, if there is an edge, and if in range
                if not (node == otherNode) and not self.G.has_edge(node[0], otherNode[0]) and self.inRange(node[1], otherNode[1]) and bool(keys1.intersection(keys2)):
                    self.G.add_edge(node[0], otherNode[0])

    # Returns true if the nodes are in commsRange of each other
    def inRange(self, node1, node2):
        xDistance = node1['x'] - node2['x']
        yDistance = node1['y'] - node2['x']
        distance = math.sqrt(xDistance * xDistance + yDistance * yDistance)
        return distance <= self.commRange

    # Calculates 1 + l / lkvm for edge and stores it into edge attribute
    def calcWLPVM(self, edge, l):
        i = edge[0]
        j = edge[1]
        wlpvm = 1 + 1.0 * l / self.G[i][j]['lkvm']
        self.G[i][j]['wlpvm'] = wlpvm

    # Calculates TPVM for edge and gamma value
    def calcTPVM(self, edge, gamma):
        i = edge[0]
        j = edge[1]
        if self.G[i][j]['lkvm'] > gamma:
            tpvm = 1
        else:
            tpvm = float("inf")
        self.G[i][j]['tpvm'] = tpvm
