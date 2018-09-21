class Node:
    def __init__(self, point, map):
        self.location = point
        self.data = map[point][1]
        self.path = [] #path holds the inclusive list of positions the program has taken to arrive at this location


    def setVisited(self, map):
        map[self.location][2] = True


    def setPath(self, previousNode):
        if previousNode.path == []:
            self.path.append(self.location)
        else:
            for each in previousNode.path:
                self.path.append(each)
            self.path.append(self.location)

        return self.path

