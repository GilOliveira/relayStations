# -*- coding: utf-8 -*-

# 2018-2019 Programação 2 LTI
# Grupo 70
# 49269 Mário Gil Oliveira
# 53340 Francisco do Ó

from Node import Node
from Edge import Edge


class Digraph(object):
    """
    Creates a digraph
    """
    
    def __init__(self):
        self._nodes = []     #nodes is a list of the nodes in the graph
        self._edges = {}      #edges is a dict mapping each node to a list of its children

    def addNode(self, node):
        """
        Adds node to digraph
        Requires: node
        """
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(node)
            self._edges[node] = []

    def addEdge(self, edge):
        """
        Adds edge to digraph
        Requires: edge
        """
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self._nodes and dest in self._nodes):
           raise ValueError('Node not in graph')
        if dest not in self._edges[src]:
            self._edges[src].append(dest)

    def childrenOf(self, node):
        """
        Requires: node (Node)
        Ensures: Children nodes of the inputed Node (as List)
        """
        return self._edges[node]

    def hasNode(self, node):
        """
        Requires: Node (as Node)
        Ensures: True if the node is in the graph, False otherwise (as Bool).
        """
        return node in self._nodes

    def getNodeList(self):
        """
        Ensures: A list of Node objects in the graph
        """
        return self._nodes

    def getNodeByID(self, id):
        """
        Requires: The ID of a node in the graph
        Ensures: A Node object with the specified ID
        """
        for i in self.getNodeList():
            if i.getID() == id:
                return i

    def getNodeByName(self, name):
        """
        Requires: name
        Ensures: name of the node
        """
        for i in self.getNodeList():
            if i.getName() == name:
                return i
        else:
            return name


    def __str__(self):
        """
        Ensures: The Nodes and Edges of the Graph.
        """
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result = result + src.getName() + '->'\
                + dest.getName() + '\n'
        return result