#!/usr/bin/python

import networkx as nx
import random
from network import Network

# first network to test attacks on
N = Network(size=250, width=500, keyPoolSize=1000, keysPerNode=30, commRange=400)

# Try 100 values of gamma for tpvm test
gArray = range(100)
# Resulting array of average hops
gAvgHopsArray = []
# Resulting array of average number of captures needed to compromise a path
gAvgCapArray = []
for gamma in gArray:
	# We use tpvm, so we must calculate it for new value
	N.calcAllTPVM(gamma)
	# We don't want repeated paths, so use a set
	paths = set()
	totalHops = 0;
	# Generate 30 paths
	while len(paths) < 30):
		start = random.randint(0, 250)
		end = randint.randint(0, 250)
		# add path find path if start and end are different
		if(start != end)
			shortestPath = nx.shortest_path(N.G, start, end, 'tpvm')
			# add path if not already added. If path is impossible, will cause exception
			if(shortestPath not in paths:
				paths = paths + [shortest_path]
				totalHops = totalHops + len(shortest_path)
	# Average totalHops for the gamma and add to array of averages
	gAvgHopsArray = gAvgHopsArray + [1.0 * totalHops / 30]
	# simulate attack on these paths and add average captures to array
	gAvgCapArray = gAvgCapArray + [simAttack(paths)]

# Try 100 values of l for wlpvm test
lArray = range(100)
# Resulting array of average hops
lAvgHopsArray = []
# Resulting array of average number of captures needed to compromise a path
lAvgCapArray = []
for l in lArray:
	# We use tpvm, so we must calculate it for new value
	N.calcAllWLPVM(l)
	simAttack('wlpvm')

# a) find the number of keys per node
N1 = Network(size=100, width=1500, keyPoolSize=1000, keysPerNode=30, commRange=500)

# b) find number of keys per node
N2 = Network(size=1000, width=1000, keyPoolSize=1200, keysPerNode=30, commRange=100)

# Returns the number of node capt
def simAttack(paths, metric);