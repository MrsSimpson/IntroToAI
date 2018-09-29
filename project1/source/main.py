from mazeRunner import *
from breadthFirstSearch import breadthFirstSearch
from depthFirstSearch import depthFirstSearch
'''                                             Created by Lacy Simpson
                                     Class: CSC 414 Intro to Artificial Intelligence
                                                Assignment #1 The Maze
                                               Date: September 20, 2018
'''
'''                                            About THE MAZE Project
The purpose of this assignment is to use breadth first search and depth first search to traverse a 10X10 maze and
find valid path/s to the exit. The text file that is read in a file that contains characters E(Entrance), X(Exit), W(wall), 
and P(path). There is only one E and it will be found on the 0 column of the maze. There is only one 'X' and it can be 
found on any of the other 3 walls besides the 0 column wall. All other boarders will be 'W'. The only valid place that the 
agent can move is the 'P' locations which are spread out throughout the map. Some paths may lead to a dead end,
while others may lead to the 'X'. The program will first read in the file and then call the appropriate functions to 
create a map, display the maze, and then preform the appropriate searches.
'''
'''main() will first create a 2D list(matrix) called theMaze by calling the readInFile function. 
A map is then created with the key value pair. The index(maze location) serves as the key, and a list containing 
the location, data, and visited bool serves as the value for each key. The program will then display the maze to the console
and call the breadth First search to find a valid path out of the maze.
The map will then be reset and the call for the depth first search will be made. The appropriate information for each
 search will be made according to each finding.
 '''


def main():
    file = "maze2.txt"
    the_maze = createMaze(readInFile(file))

    map = createMap(the_maze)
    displayMaze(map)
    breadthFirstSearch(map)

    map = createMap(the_maze)
    depthFirstSearch(map)


main()
