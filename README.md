# EE-418-WirelessRouting
Part 2 of the final project for UW EE 418
Project by Michael Von Hippel and Max Golub

Part 2 of project by Michael Von Hippel, using Python.

Compatibility:
Python 2.7 and up,

Usage instructions:
Dependencies install used pypi
install networkx
install matplotlib
To install matplotlib on a windows device, you may need to download the microsoft visual compiler. Once installed, plotting functions should work

To run simulation, run the command python ./simulation.py
Eventually, the plotted results will be displayed, which can be verified against those in the report.

network.py contains an object for the network, composed on nodes which have a subset of keys distributed to the network. To test the network, one can be initialzed by the following code:

from network import Network

N = Network(size=250, width=2500, keyPoolSize=1000, keysPerNode=30, commRange=400)

This class contains methods for calculating edge weights with different metrics.