# -*- coding: utf-8 -*-

# 2018-2019 Programação 2 LTI
# Grupo 70
# 49269 Mário Gil Oliveira
# 53340 Francisco do Ó

from Node import Node
from Edge import Edge
from copy import deepcopy
from Graph import Graph

def readStations(stationsFile):
    '''
    Reads stations from a txt file following the format specified in the project
    Requires: stationsFiles
    Ensures: digraph 
    '''
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
    '''
    Reads requested stations from a txt file following the format specified in the project.
    Requires: requestsFile and graph from the wanted stations.
    Ensures: list with current stations pair
    '''
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

def filesWriting(results, fileName):
    '''
    Writes the results from the comparison between two stations
        to an empty .txt file.
    Requires: results from the comparison between the two stations
        and fileName which gives a name to the .txt file.
    Ensures: txt file with the results from the comparison.
    '''
    createFile = open(fileName, 'w')
    for i in results:
        createFile.write(str(i))
        createFile.write('\n')
    createFile.close()
