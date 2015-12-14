#!/usr/bin/python

import networkx as nx
import random
import matplotlib.pyplot as plt
from network import Network



# noinspection PyPep8Naming
def main():
    # first network to test attacks on
    N = Network(size=250, width=2500, keyPoolSize=1000, keysPerNode=30, commRange=400)

    # Try 100 values of gamma for tpvm test
    gArray = range(1, 101)
    # Resulting array of average hops
    gAvgHopsArray = []
    # Resulting array of average number of captures needed to compromise a path
    gAvgCapArray = []
    for gamma in gArray:
        # We use tpvm, so we must calculate it for new value
        N.calcAllTPVM(gamma)
        # We don't want repeated paths, so use a set
        paths = []
        totalHops = 0
        # Generate 30 paths
        while len(paths) < 30:
            start = random.randint(0, 250 - 1)
            end = random.randint(0, 250 - 1)
            # add path find path if start and end are different
            if not start == end and nx.has_path(N.G, start, end):
                shortestPath = nx.shortest_path(N.G, start, end, 'tpvm')
                # add path if not already added. If path is impossible, will cause exception
                if not listInCollection(shortestPath, paths):
                    paths += [shortestPath]
                    totalHops += len(shortestPath)
        # Average totalHops for the gamma and add to array of averages
        gAvgHopsArray = gAvgHopsArray + [1.0 * totalHops / 30]
        # simulate attack on these paths and add average captures to array
        gAvgCapArray = gAvgCapArray + [simAttack(N.G, paths)]

    # Try 100 values of l for wlpvm test
    lArray = range(1, 101)
    # Resulting array of average hops
    lAvgHopsArray = []
    # Resulting array of average number of captures needed to compromise a path
    lAvgCapArray = []
    for l in lArray:
        # We use tpvm, so we must calculate it for new value
        N.calcAllWLPVM(l)
        # We don't want repeated paths, so use a set
        paths = []
        totalHops = 0
        # Generate 30 paths
        while len(paths) < 30:
            start = random.randint(0, 250 - 1)
            end = random.randint(0, 250 - 1)
            # add path find path if start and end are different
            if not start == end and nx.has_path(N.G, start, end):
                shortestPath = nx.shortest_path(N.G, start, end, 'wlpvm')
                # add path if not already added. If path is impossible, will cause exception
                if not listInCollection(shortestPath, paths):
                    paths += [shortestPath]
                    totalHops += len(shortestPath)
        # Average totalHops for the gamma and add to array of averages
        lAvgHopsArray = lAvgHopsArray + [1.0 * totalHops / 30]
        # simulate attack on these paths and add average captures to array
        lAvgCapArray = lAvgCapArray + [simAttack(N.G, paths)]

    # plot retults
    plt.figure(1)
    plt.subplot(211)
    plt.title('Captures to Compromise in TPVM')
    plt.plot(gArray, gAvgCapArray, 'bs')
    plt.xlabel('Gamma')
    plt.ylabel('Average # Captures to Compromise')
    plt.subplot(212)
    plt.title('Number of Hops in TPVM')
    plt.plot(gArray, gAvgHopsArray, 'bs')
    plt.xlabel('Value of Gamma')
    plt.ylabel('Average # Hops in Path')
    plt.show()
    plt.figure(1)
    plt.subplot(211)
    plt.title('Captures to Compromise in WLPVM')
    plt.plot(lArray, lAvgCapArray, 'bs')
    plt.xlabel('Lambda')
    plt.ylabel('Average # Captures to Compromise')
    plt.subplot(212)
    plt.title('Number of Hops in WLPVM')
    plt.plot(lArray, lAvgHopsArray, 'bs')
    plt.xlabel('Lambda')
    plt.ylabel('Average # Hops in Path')
    plt.show()

# Returns the average number of node captures required to each path.
# Does this by selecting a node, compromising its keys, then continuing until
# links are compromised, and then finally a path is compromised.
# paths are uncompromised paths
# noinspection PyPep8Naming
def simAttack(G, paths):
    # Total number of captures per each compromised path
    totalCaptures = 0
    # Set of all nodes which have been compromised
    compromisedNodes = set()
    # Set of all keys which have been compromised
    compromisedKeys = set()
    # Compromise more nodes while paths has uncompromised paths
    while len(paths) > 0:
        compromisedNode = random.randint(0, 250 - 1)
        if compromisedNode not in compromisedNodes:
            # add noe to compromised set
            compromisedNodes.add(compromisedNode)
            # add keys from captured node
            compromisedKeys = compromisedKeys.union(G.nodes(1)[compromisedNode][1]['keys'])
            # Iterate through paths to see if any are compromised
            index = 0;
            while (not len(paths) == 0) and index < len(paths):
                # Iterate through edges in path to see if path is compromised
                for i in range(0, len(paths[index]) - 1):
                    node1 = paths[index][i]
                    node2 = paths[index][i + 1]
                    if G[node1][node2] and compromisedKeys.issuperset(G[node1][node2]['keys']):
                        totalCaptures += len(compromisedNodes)
                        del paths[index]
                        index -= 1;
                        break;
                index += 1
    # Return average number of captures per path
    return 1.0 * totalCaptures / 30

# Since lists are unhashable, need this helper method
def listInCollection(testList, testCollection):
    for collectionList in testCollection:
        if collectionList == testList:
            return True
    return False


if __name__ == "__main__":
    main()