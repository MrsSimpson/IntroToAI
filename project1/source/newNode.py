'''                                             Created by Lacy Simpson
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
        self.path = [] #path holds the inclusive list of positions the program has taken to arrive at this nodes location



#the setVisited method checks the map to see if the nodes location has been visited.
    def setVisited(self, map):
        #set map[key][value found at the 2 index]
        map[self.location][2] = True


#setPath method checks to see if the node's path attribute contains any data, if not, the node's current location is added
#to the nodes path. If the attribute is not empty, the path from the previous node passed in is appended to the attribute
# and finally the current nodes location is appended to the end of the attribute.
    def setPath(self, previousNode):
        if previousNode.path == []:
            self.path.append(self.location)
        else:
            for each in previousNode.path:
                self.path.append(each)
            self.path.append(self.location)

        return self.path

