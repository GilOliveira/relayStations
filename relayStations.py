# 2018-2019 Programação 2 LTI
# Grupo 70
# 49269 Mário Gil Oliveira
# 53340 Francisco do Ó

import sys
from filesReading import *
from pathCalculator import *


# ---- PROGRAM START ----
stationNetwork, stationPairs, outputFile = sys.argv[1:]

stationsGraph = readStations(stationNetwork)
requestsList = readRequests(stationPairs, stationsGraph)

resultsList = runRequests(stationsGraph, requestsList)