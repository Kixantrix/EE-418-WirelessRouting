#!/usr/bin/python

import networkx as nx
import random

class Network:
	def __init__(size, width, keyPoolSize, keysPerNode, commRange):
		self.G = nx.Graph() 			# Graph of nodes
		self.size = size 				# Number of nodes in graph
		self.width = width 				# Width in meters of sides
		self.keyPoolSize = keyPoolSize 	# Number of keys in total pool
		self.keyPoolNode = keysPerNode 	# Number of pools per node
		self.commRange = commRange 		# Range in meters of communication
		# Generate all nodes within the network
		genNodes()
		# Add edges for all nodes which are in range of each other
		addEdges()
		# Add calculated LKVM values
		calcAllLKVM()

	# Calculates all lkvm values and stores them to each node
	def calcAllLKVM():
		for edge in self.G.edges()
			calcLKVM

	# Calculates lkvm for an edge and stores it to the edge
	def calcLKVM(edge):
		i = edge[0]
		j = edge[1]
		iKeys = self.G.nodes(1)[i][1]['keys']
		jKeys = self.G.nodes(1)[j][1]['keys']
		# Find shared keys along edge
		sharedKeys = iKeys.intersection(jKeys)
		# Empty set to keys acquired until same as shared keys
		c = set()
		# lkvm cost to add to
		lkvm = 0
		# Iterate while sharedKeys aren't within c
		while(!sharedKeys.issubset(c))
			randNodeIndex = random.randint(0, self.size)
			c.union(self.G.nodes(1)[randNodeIndex][1]['keys']
			lkvm = lkvm + 1
		self[i][j]['lkvm'] = lkvm

	# Generates the nodes within the network
	def genNodes():
		for i in range(self.size)
			addNewNode()

	# Adds a new node to the graph with random values within parameters
	def addNewNode(index):
		x = random.randint(0, self.width)
		y = random.randint(0, self.width)
		keys = set()
		while len(keys) < self.keysPerNode
			keys.add(random.randint(0, self.keyPoolSize))
		self.G.add_node(index, x = x, y = y, keys = keys)
	
	# Adds edges for all nodes which are in range of each other
	def addEdges():
		for node in self.G.nodes(1)
			for otherNode in self.G.nodes()
				# Add edge if not the same node, if there is an edge, and if in range
				if node != otherNode and !self.G.has_edge(node[0], otherNode[0]) and inRange(node[1], otherNode[1])
					self.G.add_edge(node[0], otherNode[0])

	# Returns true if the nodes are in commsRange of each other
	def inRange(node1, node2):
		xDistance = node1['x'] - node2['x']
		yDistance = node1['y'] - node2['x']
		distance = math.sqrt(xDistance * xDistance + yDistance * yDistance)
		return distance <= self.commRange