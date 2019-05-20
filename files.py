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

    entryCollection = []
    for i in range(fileLen-1):
        entry = file.readline().replace(', ', ',')\
            .replace('(', '').replace(')', '').replace('\n','').split(",")
        entryCollection.append(entry)


    for entry in entryCollection:
        towerID = int(entry[0])
        towerName = entry[1]
        towerPower = int(entry[2])
        towerGen = int(entry[3])
        currentNode = Node(towerID, towerName, towerPower, towerGen)
        outGraph.addNode(currentNode)

    for entry in entryCollection:
        currentNode = outGraph.getNodeByID(int(entry[0]))
        connections = entry[4:]
        for nodeID in connections:
            outGraph.addEdge(Edge(currentNode, outGraph.getNodeByID(int(nodeID))))

    file.close()
    file2.close()
    return outGraph

def readRequests(requestsFile, graph):
    outList = []
    file = open(requestsFile, 'r')
    file2 = open(requestsFile, 'r')
    fileLen = len(file2.readlines())

    for i in range(fileLen):
        currentPair = file.readline().replace('\n','').split(' ')
        nodePair = []
        for i in currentPair:
            nodePair.append(graph.getNodeByName(i))
        nodePair = tuple(nodePair)
        outList.append(nodePair)

    return outList

def filesWriting(results):
    
    