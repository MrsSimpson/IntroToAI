__init__ .py

import queue
import newNode
import main
'''
Function to Create a 10X10 Maze by using the 1D matrix that is passed in as a parameter
The 1D Matrix that is passed in will contain the letters W(for wall), E(entry), P(path), X(exit)
The matrix that is passed in contains a mixture of 100 of the previously stated characters
Using Nested For loops, a row of 10 characters will be read in and stored into a 1D array, which will then
be appended to the 2D matrix that will serve as the maze
'''
def createMaze(matrix):
    maze = []
    #at the end of the for loop, the 1D array called mazeRow will append 10 new characters to the maze array
    for row in range(10):
        mazeRow = []
        #in the inner for loop, 10 chars are added to the temporary 1D array called mazeRow.
        for column in range(10):
            #The character located at the nth position of matrix will be added
            n = (10 * row) + column
            mazeRow.append(matrix[n])

        maze.append(mazeRow)
    return maze

def createMap():
    map = {}
    for i in range(100):
        if i < 10:
            map.update({'0'+ str(i): 'F'})
        else:
            map.update({str(i): 'F'})
    return map

def readInFile(file):
    maze = []
    with open(file, "r") as mazeFile:
        for letter in range(100):
            line = mazeFile.readline()
            letter = line.rstrip('\n')
            letter = letter.upper()
            maze.append(letter)

    if not mazeFile.closed:
        mazeFile.close()

    return maze


def displayMaze(theMaze):
    for row in range(10):
        print(theMaze[row])

def findEntryPoint(theMaze):
    for row in range(10):
        for column in range(1):
            if theMaze[row][column] == 'E':
                entryPointRow = row
                entryPointColumn = column
                break
    return entryPointRow, entryPointColumn