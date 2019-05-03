# 2018-2019 Programação 2 LTI
# Grupo 70
# 49269 Mário Gil Oliveira
# 53340 Francisco do Ó

from Node import Node
from Edge import Edge
from copy import deepcopy
from Graph import Graph

def readStations(stationsFile):
    outGraph = Graph()
    edgeList = []
    file = open(stationsFile, 'r')
    file2 = open(stationsFile, 'r')
    file.readline() # Ignore first line
    fileLen = len(file2.readlines())

    for i in range(fileLen-1):
        entry = file.readline().replace(', ', ',')\
            .replace('(', '').replace(')', '').replace('\n','').split(",")
        towerID = int(entry[0])
        towerName = entry[1]
        towerPower = int(entry[2])
        towerGen = int(entry[3])
        connections = entry[4:]
        outGraph.addNode(Node(towerID, towerName, towerPower, towerGen))
        for j in connections:
            edgeList.append(Edge(towerID, int(j)))
    for i in edgeList:
        outGraph.addEdge(i)
    file.close()
    file2.close()
    return(outGraph)

