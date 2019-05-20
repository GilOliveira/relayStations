# 2018-2019 Programação 2 LTI
# Grupo 70
# 49269 Mário Gil Oliveira
# 53340 Francisco do Ó

from Node import Node

def checkCompatibility(sender, receiver):
    return not ((sender.getGeneration() == 97 and receiver.getGeneration() != 97) or
                (sender.getGeneration() != 97 and receiver.getGeneration() == 97))

def timeCalculator(sender, reciever):
    """
    Docstring
    """
    if sender.getGeneration() == 99 and reciever.getGeneration() == 99:
        return sender.getPower()**(-1)
    elif (sender.getGeneration() == 98 or reciever.getGeneration() == 98) and\
        sender.getGeneration != 97 and reciever.getGeneration() != 97:
        return 2 * sender.getPower()**(-1)
    else:
        return 4 * sender.getPower()**(-1)

