# -*- coding: utf-8 -*-

# 2018-2019 Programação 2 LTI
# Grupo 70
# 49269 Mário Gil Oliveira
# 53340 Francisco do Ó

from timeCalculator import timeCalculator
from timeCalculator import checkCompatibility

def DFS(graph, start, end, path, pathTime, shortestPath, shortestTime):
    """
    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph
    """
    path = path + [start]
    if len(path) > 1:
        previousNode = path[-2]
        pathTime = pathTime + timeCalculator(previousNode, start)
    if start == end:
        return path, pathTime
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if (shortestPath is None or pathTime < shortestTime) \
                    and checkCompatibility(start, node):
                outTuple = DFS(graph, node, end, path, pathTime, shortestPath, shortestTime)
                newPath = outTuple[0]
                newTime = outTuple[1]
                if newPath is not None:
                    shortestPath = newPath
                    shortestTime = newTime
    return shortestPath, shortestTime

def search(graph, start, end):
    """
    Requires:
    graph  a Digraph;
    start and end are nodes
    Ensures:
    shortest path from start to end in graph
    """
    if checkCompatibility(start, end):
        return DFS(graph, start, end, [], 0, None, 0)
    else:
        return None, start.getName() + ' and ' + end.getName() + ' do not communicate'

def printPath(path):
    """
    Requires: path a list of nodes
    """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result

def runRequests(graph, requestsList):
    resultsList = []
    for request in requestsList:
        if type(request[0]) is str:
            resultsList.append(request[0] + ' out of the network')
        elif type(request[1]) is str:
            resultsList.append(request[1] + ' out of the network')
        else:
            resultsList.append(search(graph, request[0], request[1])[1])
    return resultsList