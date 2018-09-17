from source.mazeRunner import *
from source.newNode import Node


def main():
    file = "maze.txt"

    theMaze = createMaze(readInFile(file))
    displayMaze(theMaze)


    map = createMap(theMaze)
    print(findEntryPoint(map))
    # prints the values stored at each key "location"
    # use this syntax to check or change values at map key locations
    for row in range(10):
        n = 10 * row
        print(map[(n)][1], map[n+1][1], map[n+2][1], map[n+3][1], map[n+4][1], map[n+5][1], map[n+6][1], map[n+7][1], map[n+8][1], map[n+9][1])

    entryPoint = findEntryPoint(map)
    initialPosition = Node()
    initialPosition.getLocation(entryPoint)
    print(initialPosition.location)
    initialPosition.getData(map, n)
    print(initialPosition.data)


main()