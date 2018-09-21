'''
Function to Create a 10X10 Maze by using the 1D matrix that is passed in as a parameter
The 1D Matrix that is passed in will contain the letters W(for wall), E(entry), P(path), X(exit)
The matrix that is passed in contains a mixture of 100 of the previously stated characters
Using Nested For loops, a row of 10 characters will be read in and stored into a 1D array, which will then
be appended to the 2D matrix that will serve as the maze. This is used only to print the maze to the console
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


'''Create Map takes the 2D array previously created and creates a python dictionary named map that creates a key:value pair
 Each Location is unique, therefore serves as the key, the values stored will be the location, the data located at that
 location, and the visited state. Initially all states are set to False because nothing has been visited.
 '''
def createMap(theMaze):
    map = {}
    for row in range(10):
        for column in range(10):
            n = (10 * row) + column
            map.update({n: [n, theMaze[row][column], False]})
    return map


'''
Function to read in the text file and store in a python list (array) called maze.
The new line character is stripped from each line which leaves only the data to be stored (a single character)
'''
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

'''Function to output the 2D array to the console. The console will display the character stored at each location.'''
def displayMaze(map):
    print("            THE MAZE")
    for i in range(0, 10):
        print("  " + str(i), end='')
    print()
    for row in range(10):
        n = row * 10
        print(str(row) + " " + map[n][1] + "  " + map[n +1][1] + "  " + map[n+2][1] + "  " + map[n+3][1] + "  " + map[n+4][1] +
              "  " + map[n+5][1] + "  " + map[n+6][1] + "  " + map[n+7][1] + "  " + map[n+8][1] + "  " + map[n+9][1])

'''
Function finds the entry point of the maze. The map dictionary is read in and it searches for the char E. If the E is
found, the location that E is stored in will returned.
'''
def findEntryPoint(map):
    for state in map:
        if map[state][1] == 'E':
            return map[state][0]

