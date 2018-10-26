"""solve the slider puzzle"""

from __future__ import print_function
import random


def menu():
    """Give the user a choice on how to create the puzzle."""
    choice = ''
    print("       Welcome to Slider 8\n")
    choice = input("Please select one of the following choices. \n1. Press 1 to create a completely random puzzle.\n"
                   "2. Press 2 to pick the empty space for a random puzzle.")
    while not (choice in ('1', '2')):
        print("You did not select a valid option, please select 1 or 2.")
        choice = input("Please select one of the following choices. \n"
                       "1. Create Random Starting State.\n"
                       "2. Pick a Starting Space.\n")

    return get_user_input(choice)


def get_user_input(choice):
    """do something with the users choice"""
    if choice == '1':
        rand_environment = create_random_environment()
        print("Random Start State Created", rand_environment)
        return rand_environment

    if choice == '2':
        choice2 = ''
        choice2 = input("\nPlease select an an empty position.\n"
                        "1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9\n")
        while not (choice2 in ('1', '2', '3', '4', '5', '6', '7', '8', '9')):
            print("\nYou did not select a valid option, please select a single number in the range 1 - 9")
            choice2 = input("Please select an an empty position.\n"
                            "1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 \n")
        rand_environment = create_random_environment()
        user_environment = create_user_defined_environment(rand_environment, int(choice2))
        return user_environment


def create_random_environment():
    """create a random puzzle board for the game"""
    rand_environment = []
    for i in range(9):
        rand_environment.append(i)
        random.shuffle(rand_environment)

    return rand_environment


def create_user_defined_environment(rand_environment, user_choice):
    """create a random environment with the users choice of the empty space"""
    empty_position = 0
    for i in range(9):
        if rand_environment[i] == 0:
            empty_position = i

    user_environment = swap_empty_position(rand_environment, empty_position, user_choice-1)
    print("Random Start State Created with your choice of the empty space", user_environment)
    return user_environment


def pick_a_search():
    """Give the user a choice on which search to perform."""
    print ("Please select one of the following choices to solve the slider puzzle.")
    print ("1. Solve using breadth first search")
    print ("2. Solve using depth first search")
    print ("3. Solve with A* Search using the number of misplaced tiles.")
    print ("4. Solve with A* Search using the manhattan distance")


def create_starting_state():
    """Create the starting state of the puzzle."""
    environment = [2, 7, 5, 1, 4, 3, 6, 0, 8]
    #environment = [7, 8, 3, 4, 1, 5, 6, 0, 2]
    return environment


def find_starting_position(environment):
    """Locate the starting position to begin the search"""
    for i in range(9):
        if environment[i] == 0:
            starting_point = i
            return starting_point
    return None


def check_goal_state(current_node):
    """Check to see if the current node is the goal state"""
    if current_node.start_state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        return True

    return False


def check_visited(visited, new_state):
    """Check to see if the start has been visited already"""
    new_state_string = ""
    for number in new_state:
        new_state_string += str(number)

    if new_state_string in visited:
        return True

    return False


def add_to_visited(visited, new_state, counter):
    """add the string of integers to the dictionary with the counter"""
    environment_string = ""
    for number in new_state:
        environment_string += str(number)

    visited.update({environment_string: counter})


def swap_empty_position(new_state, empty_spot, new_empty_spot):
    """Swap the positions in the new environment"""
    new_state[empty_spot], new_state[new_empty_spot] = \
        new_state[new_empty_spot], new_state[empty_spot]
    return new_state
