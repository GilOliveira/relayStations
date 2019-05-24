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
        """
        Ensures: the station ID (int)
        """
        return self._id

    def getName(self):
        """
        Ensures: the station name (str)
        """
        return self._name

    def getPower(self):
        """
        Ensures: the the station power (int)
        """
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

    def __eq__(self, other):
        """
        Overrides the '==' operator.
        Requires: other is Node
        Ensures: True if both nodes have the same ID, False otherwise
                (as bool)
        """

        if self.getID() == other.getID():
            return True
        else:
            return False

    def __lt__(self, other):
        """
        Overrides the '<' and '>' operators
        Requires: other is Node
        Ensures: True if self has a smaller ID, False otherwise
                (as bool)
        """

        if self.getID() < other.getID():
            return True
        else:
            return False

    def __str__(self):
        """
        Makes the string output with the attributes of the node.
        """
        return str(self.getID()) + " - " + str(self.getName()) + " - " + \
               str(self.getPower()) + " - " + str(self.getGeneration())