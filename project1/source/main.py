from source.mazeRunner import *
from source.newNode import newNode


def main():
    file = "maze.txt"

    theMaze = createMaze(readInFile(file))
    displayMaze(theMaze)
    print(findEntryPoint(theMaze))

    map = createMap()
    print(map)

    # prints the value stored at the key '02'
    # use this syntax to check or change values at map key locations
    print(map['02'])

    entryRow, entryColumn = findEntryPoint(theMaze)
    print(entryRow, entryColumn)
    initialPosition = newNode(entryRow, entryColumn)
    initialPosition.data = theMaze[entryRow][entryColumn]
    print(initialPosition.location)


main()