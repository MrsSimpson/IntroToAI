'''Created by Lacy Simpson
Class: CSC 414 Intro to Artificial Intelligence
Assignment #1 The Maze
Date: September 20, 2018
'''

'''The Node class contains the location, the data, and the path at the location passed in.
Each node is created with the passed in parameters point, and map.
The Node class also has methods to set the Visited state to true when called.
A method to set the path by appending the previous nodes path and the current nodes position.'''


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

