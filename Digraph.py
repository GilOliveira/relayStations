# -*- coding: utf-8 -*-

# 2018-2019 Programação 2 LTI
# Grupo 70
# 49269 Mário Gil Oliveira
# 53340 Francisco do Ó

from Node import Node
from Edge import Edge

class Digraph(object):
    #nodes is a list of the nodes in the graph
    #edges is a dict mapping each node to a list of its children

    def __init__(self):
        self.nodes = []
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
           raise ValueError('Node not in graph')
        if dest not in self.edges[src]:
            self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def getNodeList(self):
        """
        Ensures: A list of Node objects in the graph
        """
        return self.nodes

    def getNodeByID(self, id):
        """
        Requires: The ID of a node in the graph
        Ensures: A Node object with the specified ID
        """
        for i in self.getNodeList():
            if i.getID() == id:
                return i

    def getNodeByName(self, name):
        for i in self.getNodeList():
            if i.getName() == name:
                return i
        else:
            return name

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                + dest.getName() + '\n'
        return result