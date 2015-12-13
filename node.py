class Node:
	# Basic node structure for network
	def __init__(x, y, range, keys):
		self.x = x            # X position of node
		self.y = y            # Y position of node
		self.range = range;   # Range of signal from node
		self.keys = keys      # Set of keys posessed

	def hasEdge(otherNode):
		# Returns true if otherNode is within range of self
		xDistance = self.x - otherNode.x
		yDistance = self.y - otherNode.y
		distance = math.sqrt(xDistance * xDistance + yDistance * yDistance)
		return distance <= self.range