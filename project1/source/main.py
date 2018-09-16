from source.mazeRunner import *
from source.newNode import newNode


def main():
    file = "maze.txt"

    theMaze = createMaze(readInFile(file))
    displayMaze(theMaze)
    print(findEntryPoint(theMaze))

    map = createMap(theMaze)

    # prints the value stored at the key '02'
    # use this syntax to check or change values at map key locations
    for row in range(10):
        n = 10 * row
        print(map[(n)], map[n+1], map[n+2], map[n+3], map[n+4], map[n+5], map[n+6], map[n+7], map[n+8], map[n+9])

    entryRow, entryColumn = findEntryPoint(theMaze)
    print(entryRow, entryColumn)
    initialPosition = newNode(entryRow, entryColumn)
    initialPosition.data = theMaze[entryRow][entryColumn]
    print(initialPosition.location)


main()