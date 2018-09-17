from source.breadthFirstSearch.py import *
class Node:
    def __init__(self):
        self.location = 0
        self.data = ''
        self.fringe = []
        self.visited = False
        self.path = []

    def getLocation(self, point):
        self.location = point

    def getData(self, theMap, n):
        self.data = theMap[n][1]

    def getNeighbors(self, Node):
        if Node not in self.fringe:
            self.fringe.append(Node)

    def isVisited(self, visited):
        for number in visited:
            if self.location == number:
                return True
            else:
                return False
    def setPath(self, previousNode):
        if previousNode == None:
            self.path.append(self.location)
        else:
            self.path.append(previousNode.path)

    def findValidNeighbors(self):
        if ((self.location != 0) and (self.location % 10 != 0) and (self.data == 'P' or self.data == 'X')):
            leftNeighbor = self.location - 1
            self.getNeighbors(leftNeighbor)

        if (not(self.location < 0)) and (self.data == 'P' or self.data == 'X'):
            topNeighbor = self.location - 10
            self.getNeighbors(topNeighbor)

        remainder = (self.location + 1) % 10
        if (remainder != 0) and (self.data == 'P' or self.data == 'X'):
            rightNeighbor = self.location + 1
            self.getNeighbors(rightNeighbor)

        if (not (self.location + 10) > 99) and (self.data == 'P' or self.data == 'X'):
            bottomNeighbor = self.location + 10
            self.getNeighbors(bottomNeighbor)