# -*- coding: utf-8 -*-

# 2018-2019 Programação 2 LTI
# Grupo 70
# 49269 Mário Gil Oliveira
# 53340 Francisco do Ó

from Node import Node

def checkCompatibility(sender, receiver):
    """
    Checks if both sender and receiver station have the same generation.
    Requires: sender station and receiver station.
    """
    return not ((sender.getGeneration() == 97 and receiver.getGeneration() != 97) or
                (sender.getGeneration() != 97 and receiver.getGeneration() == 97))
                #since stations from the 97th generation can only comunicate with a 97th generation station.

def timeCalculator(sender, receiver):
    """
    Adds the times between the sender and the receiver nodes.
    Requires: sender station and receiver station
    """
    if sender.getGeneration() == 99 and receiver.getGeneration() == 99:
        return sender.getPower()**(-1)
    elif (sender.getGeneration() == 98 or receiver.getGeneration() == 98) and\
        sender.getGeneration != 97 and receiver.getGeneration() != 97:
        return 2 * sender.getPower()**(-1)
    else:
        return 4 * sender.getPower()**(-1)

