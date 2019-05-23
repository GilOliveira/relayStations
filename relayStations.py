# -*- coding: utf-8 -*-

# 2018-2019 Programação 2 LTI
# Grupo 70
# 49269 Mário Gil Oliveira
# 53340 Francisco do Ó

import sys
import files
from pathCalculator import *
from Node import Node
from Edge import Edge
from copy import deepcopy
from Graph import Graph


# ---- PROGRAM START ----

# Import the files names for the list of stations, the connection requests
# and the output file from the terminal
stationNetwork, stationPairs, outputFile = sys.argv[1:]

# Reading the list of stations and storing the graph in stationsGraph
stationsGraph = files.readStations(stationNetwork)

# Reading the list of requests and storing the pairs in requestsLists
requestsList = files.readRequests(stationPairs, stationsGraph)

# Calculating the paths and times into resultsList
resultsList = runRequests(stationsGraph, requestsList)

# Writing the results to a file
files.filesWriting(resultsList, outputFile)
