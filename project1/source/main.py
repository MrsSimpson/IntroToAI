
from source.newNode import *
from source.mazeRunner import *
from source.breadthFirstSearch import *


def main():
    file = "maze.txt"
    theMaze = createMaze(readInFile(file))
    displayMaze(theMaze)

    map = createMap(theMaze)

    BFS(map)



main()