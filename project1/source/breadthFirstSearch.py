from source.newNode import *
from source.mazeRunner import *


def createRoot(point, map):
    nullMap = {0: [0, 'W', False]}
    previousNode = Node(0, nullMap)
    root = Node(point, map)
    root.findValidNeighbors(point, map)
    root.setPath(previousNode)
    return root



def createQueue(point, map):
    theQ = []
    prevVisited = []
    if isQueueEmpty(theQ) == True:
        root = createRoot(point, map)
        prevVisited.append(root.location)
        theQ.append(root)
        theQ[0].visited = theQ[0].isVisited(prevVisited)

    return theQ


def isQueueEmpty(theQ):
    if theQ == []:
        return True
    else:
        return False

def beginSearch(map):
    entryPoint = findEntryPoint(map)
    theQ = createQueue(entryPoint, map)
    print(theQ[0].location, theQ[0].data, theQ[0].neighbors, theQ[0].visited, theQ[0].path)
    previous = theQ.pop(0)
    for all in previous.neighbors:
        newNode = Node(all, map)
        theQ.append(newNode)

    i = 0
    while i < len(theQ):
        print(theQ[i].location, theQ[i].data)
        i += 1

    while theQ != []:
        current = theQ[0]
        point = current.location
        current.findValidNeighbors(point, map)
        print(current.neighbors)
        theQ.pop(0)







