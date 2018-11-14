"""solve the slider puzzle"""

from __future__ import print_function
import random
import csv


def print_the_game(environment):
    """function prints the state of the board with formatting when called."""
    print("-------------")
    print("|", environment[0], "|", environment[1], "|", environment[2], "|")
    print("|", environment[3], "|", environment[4], "|", environment[5], "|")
    print("|", environment[6], "|", environment[7], "|", environment[8], "|")
    print("-------------")

def print_the_path(solution_path):
    print("\nThe path to the solution is:")
    while solution_path:
        path1 = ""
        path2 = ""
        path3 = ""
        path4 = ""
        path1 = solution_path.pop(0)
        path1 = path1.strip("\n")
        if solution_path:
            path2 = solution_path.pop(0)
            path2 = path2.strip("\n")
            if solution_path:
                path3 = solution_path.pop(0)
                path3 = path3.strip("\n")
                if solution_path:
                    path4 = solution_path.pop(0)
                    path4 = path4.strip("\n")
        print(path1 + " " + path2 + " " + path3 + " " + path4)

def create_random_environment():
    """create a random puzzle board for the game."""
    #the function creates an array to hold a list of 9 integers. When the for loop begins, integer is appended to
    #the list and then the array is shuffled randomly. This guarentees that each integer in the list is unique and
    #that the only integers contained in the list are 0-8
    rand_environment = []
    for i in range(9):
        rand_environment.append(i)
        random.shuffle(rand_environment)

    return rand_environment


def create_user_defined_environment(rand_environment, user_choice):
    """create a random environment with the users choice of the empty space"""
    #The function first uses a for loop to find the empty position of the randomly created
    #environment. The function then calls another function to swap the current empty position with the users choice
    #of the empty spot. This ensures that the puzzle is still random but the user gets choice where their empty position
    #is. The funciton then returns the environment.
    empty_position = 0
    for i in range(9):
        if rand_environment[i] == 0:
            empty_position = i

    user_environment = swap_empty_position(rand_environment, empty_position, user_choice-1)
    return user_environment


def create_starting_state():
    """Create the starting state of the puzzle."""
    #the environment created is hard coded. Different versions can be chosen by commenting and uncommenting the
    #environment variables.
    #environment = [2, 7, 5, 1, 4, 3, 6, 0, 8]
    environment = [7, 8, 3, 4, 1, 5, 6, 0, 2]
    #environment = [3, 2, 4, 1, 5, 6, 7, 8, 0]
    return environment


def find_starting_position(environment):
    """Locates the starting position to begin the search"""
    #the function locates the element that is == 0.
    for i in range(9):
        if environment[i] == 0:
            starting_point = i
            return starting_point
    return None


def check_goal_state(current_node):
    """Check to see if the current node's start state matches the goal state"""
    if current_node.start_state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        return True

    return False


def check_visited(visited, new_state):
    """Check to see if the start has been visited already"""
    #The funciton converts the new_state array into a string of characters.
    #It then checks to see if string is already contained in the visited library and returns the appropriate boolean.
    new_state_string = ""
    for number in new_state:
        new_state_string += str(number)

    if new_state_string in visited:
        return True

    return False


def add_to_visited(visited, new_state, counter):
    """Convert add the string of integers to the dictionary along with the counter"""
    environment_string = ""
    for number in new_state:
        environment_string += str(number)

    visited.update({environment_string: counter})


def swap_empty_position(new_state, empty_spot, new_empty_spot):
    """Swap the positions in the new environment"""
    #the function takes swaps the empty_spot position with the new empty_spot position and returns a new_state.
    new_state[empty_spot], new_state[new_empty_spot] = \
        new_state[new_empty_spot], new_state[empty_spot]
    return new_state



def write_to_file(node, data_structure, COUNTER, timer, search_type):
    with open('report.csv', 'a', newline='') as file:
        line_write = csv.writer(file)
        line_write.writerow(['Search_type', 'Start State', 'Solution Found', 'Depth', 'Solution Path', 'Nodes Expanded', 'Search Time'])
    if data_structure:
        line_write.writerow([search_type, node.start_state, 'True', print_the_path(node.path), COUNTER, timer])


    else:
        line_write.writerow([search_type, node.start_state, 'False'])

