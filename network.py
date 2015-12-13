import networkx as nx
import random

class Network:
	def __init__(size, width, keyPoolSize, keysPerNode, commRange):
		self.G = nx.Graph()
		self.size = size
		self.width = width
		self.keyPoolSize = keyPoolSize
		self.keyPoolNode = keysPerNode
		self.commRange = commRange
		# Generate all nodes within the network
		genNodes()
		# Add edges for all nodes which are in range of each other
		addEdges()

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
				if node != otherNode and !self.G.has_edge(node[0], otherNode[0]) and inRange(node, otherNode)
					self.G.add_edge(node, otherNode)

	# Returns true if the nodes are in commsRange of each other
	def inRange(node1, node2):
		xDistance = node1['x'] - node2['x']
		yDistance = node1['y'] - node2['x']
		distance = math.sqrt(xDistance * xDistance + yDistance * yDistance)
		return distance <= self.commRange