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
stationNetwork, stationPairs, outputFile = sys.argv[1:]

stationsGraph = files.readStations(stationNetwork)
requestsList = files.readRequests(stationPairs, stationsGraph)

resultsList = runRequests(stationsGraph, requestsList)

files.filesWriting(resultsList, outputFile)