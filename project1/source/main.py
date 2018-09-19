
from source.newNode import *
from source.mazeRunner import *


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
        print(map[(n)], map[n+1], map[n+2], map[n+3], map[n+4], map[n+5], map[n+6], map[n+7], map[n+8], map[n+9])

    prevVisited = [60]
    point = findEntryPoint(map)
    initialPosition = Node(point, map)
    #initialPosition.setNewNode(point, map)
    data = map[point][1]
    initialPosition.findValidNeighbors(point, map)
    initialPosition.setPath(initialPosition)
    initialPosition.visited = initialPosition.isVisited(prevVisited)
    print(initialPosition.location)
    print(initialPosition.data)
    print(initialPosition.path)
    print(initialPosition.visited)
    print(initialPosition.neighbors)


main()