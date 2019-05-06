"""
Este ficheiro serve só para eu fazer debug ao código que faço.
- Gil
"""

from filesReading import *

graph = readStations('myStationsNetwork.txt')
requests = readRequests('mytestSet.txt', graph)


for i in requests:
    print('(')
    for j in i:
        print(j)
    print(')')
