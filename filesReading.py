# 2018-2019 Programação 2 LTI
# Grupo 70
# 49269 Mário Gil Oliveira
# 53340 Francisco do Ó

from Node import Node
from Edge import Edge

def readStations(stationsFile):
    file = open(stationsFile, 'r')
    file.readline()  # Ignore first line
    fileLen = len(file.readlines())

    for i in range(fileLen-1):
        entry = file.readline().replace(', ', ',')\
            .replace(' (', '').replace(')', '').split(",")
        towerID = entry[0]
        towerFreq = entry[1]
        towerGen = entry[2]
        connections = entry[3:]
        currentNode = Node()
