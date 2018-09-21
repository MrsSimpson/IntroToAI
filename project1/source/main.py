from source.mazeRunner import *
from source.breadthFirstSearch import breadthFirstSearch
from source.depthFirstSearch import depthFirstSearch


def main():
    file = "maze.txt"
    theMaze = createMaze(readInFile(file))


    map = createMap(theMaze)
    displayMaze(map)
    breadthFirstSearch(map)

    map2 = createMap(theMaze)
    depthFirstSearch(map2)

main()