'''                                             Created by Lacy Simpson
                                    Class: CSC 414 Intro to Artificial Intelligence
                                                Assignment #1 The Maze
                                               Date: September 20, 2018
'''

from newNode import *
from mazeRunner import *


'''The breadthFirstSearch function finds the entry point marked 'E' on the map. The entry point will be used to create
the Queue. The program will then drop into the while loop as long as the length of theQ is not equal to 0. The previous
variable will be set by popping the 0 index of the Queue. The program will then check to see if previous contains the
desired state. If it does the results will be displayed and the program will break from the while loop. If not, the 
function to find valid neighbors of the node in previous is called. If the while loop ends, a check is made to see if the Q is 
empty and the previous node popped from the X contained the 'X'. If it did not, we know that a valid path was not found
for the maze.'''
def breadthFirstSearch(map):
    entryPoint = findEntryPoint(map)
    theQ = createQueue(entryPoint, map)
    previous = theQ[0]

    while len(theQ) != 0:
        previous = theQ.pop(0)
        if previous.data == 'X':
            print("Breadth First Search Found A Valid Path: " + str(previous.path))
            break
        else:
            findValidNeighbors(previous, theQ, map)

    if len(theQ) == 0 and previous.data != 'X':
        print("Breadth First Search did not find a valid path to exit the maze.")

#function creates the root node. It sets the visited state of the node to True and also sets the path for arriving at
#that node.
def createRoot(point, map):
    root = Node(point, map)
    root.setVisited(map)
    root.path = root.setPath(root)
    return root

#This function creates the Q that is used when traversing the maze. If the Q is empty, we know that the first node to be
#added to the Q is the root(entry point).
def createQueue(point, map):
    theQ = []
    if isQueueEmpty(theQ) == True:
        root = createRoot(point, map)
        theQ.append(root)

    return theQ

#Function checks to see if the Queue is empty
def isQueueEmpty(theQ):
    if theQ == []:
        return True
    else:
        return False


'''funciton used to find the top neighbor from the point that is passed in. The if statement checks to see if the point 
being checked is on the board. If the point - 10 is a negative value, then we know we have moved off the board.
The second check in the if statement checks to make sure that the data contained is not a 'W'. Finally the third condition
in the if statement checks the map to make sure that the visited value is = to False. If it is equal to true, then we
know that it has already been visited. If all of these conditions are met, the location for the top neighbor is returned.'''
def findTopNeighbor(point, map):
    if (not((point - 10) < 0)) and (map[point - 10][1] != 'W') and (map[point-10][2] == False):
        topNeighbor = point - 10
        return topNeighbor


'''funciton used to find the right neighbor from the point that is passed in. The if statement checks to see if the point 
being checked is on the board. If the (point + 1) modulus 10 has a 0 remainder, then we know we have moved off the board.
The second check in the if statement checks to make sure that the data contained is not a 'W'. Finally the third condition
in the if statement checks the map to make sure that the visited value is = to False. If it is equal to true, then we
know that it has already been visited. If all of these conditions are met, the location for the top neighbor is returned.'''
def findRightNeighbor(point, map):
    remainder = (point + 1) % 10
    if (remainder != 0) and (map[point + 1][1] != 'W') and (map[point + 1][2] == False):
        rightNeighbor = point + 1
        return rightNeighbor

'''funciton used to find the bottom neighbor from the point that is passed in. The if statement checks to see if the point 
being checked is on the board. If the point + 10 is greater than 99, then we know we have moved off the board.
The second check in the if statement checks to make sure that the data contained is not a 'W'. Finally the third condition
in the if statement checks the map to make sure that the visited value is = to False. If it is equal to true, then we
know that it has already been visited. If all of these conditions are met, the location for the top neighbor is returned.'''
def findBottomNeighbor(point, map):
    if (not (point + 10) > 99) and (map[point + 10][1] != 'W') and (map[point + 10][2] == False):
        bottomNeighbor = point + 10
        return bottomNeighbor


'''funciton used to find the left neighbor from the point that is passed in. The if statement checks to see if the point 
being checked is on the board. If the point modulus 10 is = to 0, then we know we have moved off the board.
The second check in the if statement checks to make sure that the data contained is not a 'W'. Finally the third condition
in the if statement checks the map to make sure that the visited value is = to False. If it is equal to true, then we
know that it has already been visited. If all of these conditions are met, the location for the top neighbor is returned.'''
def findLeftNeighbor(point, map):
    if ((point % 10 != 0) and (map[point - 1][1] != 'W')) and (map[point -1][2] == False):
        leftNeighbor = point - 1
        return leftNeighbor


'''Function will check the top, right, bottom, and then left neighbor of the node previously popped from the Queue. If
there is a valid neighboring location from any of these locations, a node will be created for that state, the path to
that node will be set, and then the node will be added to the Queue using the FIFO approach. '''
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

