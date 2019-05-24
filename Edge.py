# -*- coding: utf-8 -*-

# 2018-2019 Programação 2 LTI
# Grupo 70
# 49269 Mário Gil Oliveira
# 53340 Francisco do Ó

from Node import Node
class Edge(object):
    """
    Creates an Edge object.
    """

    def __init__(self, src, dest):
        """
        Requires: src and dst Nodes
        """
        self._src = src
        self._dest = dest

    def getSource(self):
        """
        Ensures: The source Node of the Edge (as Node)
        """
        return self._src

    def getDestination(self):
        """
        Ensures: The destination Node of the Edge (as Node)
        """
        return self._dest


    def __eq__(self, other):
        """
        Ensures: True if 2 edges have the same source and destination, False otherwise
                (as bool)
        """
        if self.getSource() == other.getSource() \
                and self.getDestination() == other.getDestination:
            return True
        else: return False
        
    def __str__(self):
        """
        The string representation of an Edge, in the 'src -> dest' format
        """
        return self._src.getName() + '->' + self._dest.getName()