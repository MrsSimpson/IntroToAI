import time
from subpackages.breadth_first_search import begin_breadth_first_search
from subpackages.depth_first_search import begin_depth_first_search
from subpackages.solve_the_puzzle import create_random_environment, create_user_defined_environment
from subpackages.node import Node


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

    user_search_choice(get_user_input(choice))
    replay_choice = ""
    print("\nWould you like to play again?\n")
    replay_choice = input("Y for Yes\nN for No\n")
    while not(replay_choice in ('Y', 'N', 'y', 'n')):
        print("Please select either Y or N")
        replay_choice = input("Y for Yes\nN for No\n")

    while not(replay_choice in ('N', 'n')):
        menu()
        user_search_choice(get_user_input(choice))
        print("\nWould you like to play again?\n")
        replay_choice = input("Y for Yes\nN for No\n")
        if replay_choice == 'N' or 'n':
            break
        if not (replay_choice in ('Y', 'N', 'y', 'n')):
            print("Please select either Y or N")
            replay_choice = input("Y for Yes\nN for No\n")
        if replay_choice == 'N' or 'n':
            break


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


def user_search_choice(environment):
    """Menu for the user to decide which type of search they would like to perform"""
    user_choice = ''
    print("\nPlease select which search you would like to perform.")
    user_choice = input("1. Select 1 for breadth first search.\n"
          "2. Select 2 for depth first search\n")
    while not (user_choice in ('1', '2')):
        print("\nYou did not select a valid option.")
        user_choice = input("1. Select 1 for breadth first search\n"
          "2. Select 2 for depth first search\n")

    if(user_choice == '1'):
        visited_map = {}
        start_time = time.clock()
        current_node = Node(environment)
        current_node.empty_spot = current_node.find_empty_position()
        current_node.create_state_string()
        visited_map.update({current_node.state_string: 1})
        begin_breadth_first_search(current_node, visited_map, start_time)

    if(user_choice == '2'):
        visited_map = {}
        start_time = time.clock()
        current_node = Node(environment)
        current_node.empty_spot = current_node.find_empty_position()
        current_node.create_state_string()
        visited_map.update({current_node.state_string: 1})
        #user_search_choice(current_node, visited_map, start_time)
        begin_depth_first_search(current_node, visited_map, start_time)