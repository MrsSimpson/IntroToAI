
from source.newNode import *
from source.mazeRunner import *
from source.breadthFirstSearch import *
from source.depthFirstSearch import DFS


def main():
    file = "maze.txt"
    theMaze = createMaze(readInFile(file))
    displayMaze(theMaze)

    map = createMap(theMaze)

    BFS(map)

    map2 = createMap(theMaze)
    DFS(map2)



main()