# -*- coding: utf-8 -*-

# 2018-2019 Programação 2 LTI
# Grupo 70
# 49269 Mário Gil Oliveira
# 53340 Francisco do Ó

class Node(object):
    def __init__(self, id, name, power, generation):
        """
        Requires: id is int
        Requires: name is str
        Requires: power is int
        Requires: generation is int (97, 98 or 99)
        Ensures: The creation of a Node object
        """
        self._id = id
        self._name = name
        self._power = power
        self._generation = generation

    def getID(self):
        return self._id

    def getName(self):
        return self._name

    def getPower(self):
        return self._power

    def getGeneration(self):
        return self._generation

    def setID(self, id):
        """
        Requires: id of the node
        """
        self._id = id

    def setName(self, name):
        """
        Requires: name of the node
        """
        self._name = name

    def setPower(self, power):
        """
        Requires: power of the node
        """
        self._power = power

    def setID(self, generation):
        """
        Requires: type of generation of the node
        """
        self._generation = generation

    def __str__(self):
        return str(self.getID()) + " - " + str(self.getName()) + " - " + \
               str(self.getPower()) + " - " + str(self.getGeneration())