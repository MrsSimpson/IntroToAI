class Node:
    def __init__(self):
        self.location = 0
        self.data = ''
        self.fringe = []
        self.visited = False
        self.previous = []

    def getLocation(self, point):
        self.location = point

    def getData(self, theMap, n):
        self.data = theMap[n][1]

    def getFringe(self, Node):
        if Node not in self.fringe:
            self.fringe.append(Node)

    def isVisited(self, visited):
        for number in visited:
            if self.location == number:
                return True
            else:
                return False