from source.newNode import *
from source.mazeRunner import *


#createNode = to the entry point
#mark the node as visited
#put the node in the queue
#enter do while loop.
    #check to see if front of queue is goal.
        #if not, continue
        #if so, break and print the location

    #inner loop
    #check the neighboring nodes for possible paths.
        #check topNeighbor. If we have not visited it yet, create a node to represent topNeighbor and put in queue and mark that it has been visited
        #check rightNeighbor. If we have not visited it yet, create a node to represent rightNeighbor and put in q. Mark as visited.
        #check bottomNeighbor. ""
        #check leftNeighbor. ""
#back in the main loop, pop front of the queue. and set as previousNode. (bc initialPosition has been explored.)

#now we return to the top of the do while loop.
def breadthFirstSearch(map):
    entryPoint = findEntryPoint(map)
    theQ = createQueue(entryPoint, map)

    while len(theQ) != 0:
        previous = theQ.pop(0)
        if previous.data == 'X':
            print("Breadth First Search Found A Path: " + str(previous.path))
            break
        else:
            findValidNeighbors(previous, theQ, map)


def createRoot(point, map):
    root = Node(point, map)
    root.setVisited(map)
    root.path = root.setPath(root)
    return root


def createQueue(point, map):
    theQ = []
    if isQueueEmpty(theQ) == True:
        root = createRoot(point, map)
        theQ.append(root)

    return theQ


def isQueueEmpty(theQ):
    if theQ == []:
        return True
    else:
        return False

def findTopNeighbor(point, map):
    if (not((point - 10) < 0)) and (map[point - 10][1] != 'W') and (map[point-10][2] == False):
        topNeighbor = point - 10
        return topNeighbor

def findRightNeighbor(point, map):
    remainder = (point + 1) % 10
    if (remainder != 0) and (map[point + 1][1] != 'W') and (map[point + 1][2] == False):
        rightNeighbor = point + 1
        return rightNeighbor

def findBottomNeighbor(point, map):
    if (not (point + 10) > 99) and (map[point + 10][1] != 'W') and (map[point + 10][2] == False):
        bottomNeighbor = point + 10
        return bottomNeighbor

def findLeftNeighbor(point, map):
    if ((point % 10 != 0) and (map[point - 1][1] != 'W')) and (map[point -1][2] == False):
        leftNeighbor = point - 1
        return leftNeighbor

def findValidNeighbors(previous, theQ, map):
    topNeighbor = findTopNeighbor(previous.location, map)
    if topNeighbor != None:
        topNode = Node(topNeighbor, map)
        topNode.setVisited(map)
        topNode.setPath(previous)
        theQ.append(topNode)

    rightNeighbor = findRightNeighbor(previous.location, map)
    if rightNeighbor != None:
        rightNode = Node(rightNeighbor, map)
        rightNode.setVisited(map)
        rightNode.setPath(previous)
        theQ.append(rightNode)

    bottomNeighbor = findBottomNeighbor(previous.location, map)
    if bottomNeighbor != None:
        bottomNode = Node(bottomNeighbor, map)
        bottomNode.setVisited(map)
        bottomNode.setPath(previous)
        theQ.append(bottomNode)

    leftNeighbor = findLeftNeighbor(previous.location, map)
    if leftNeighbor != None:
        leftNode = Node(leftNeighbor, map)
        leftNode.setVisited(map)
        leftNode.setPath(previous)
        theQ.append(leftNode)

