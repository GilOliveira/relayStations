# 2018-2019 Programação 2 LTI
# Grupo 70
# 49269 Mário Gil Oliveira
# 53340 Francisco do Ó

from Digraph import Digraph
from Edge import Edge
from Digraph import Digraph

class Graph(Digraph):

    def __init__(self):
        Digraph.__init__(self)

    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)