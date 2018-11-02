"""Run the slider 8 program. Uncomment the menu to allow the user to select options. """
#If menu is commented out the main program will run all four searches and display the results.
#Lacy Simpson
#CSC 412
#October 31, 2018


import time
from subpackages.user_menu import menu
from subpackages.solve_the_puzzle import create_starting_state, print_the_game
from subpackages.node import Node
from subpackages.breadth_first_search import begin_breadth_first_search
from subpackages.depth_first_search import begin_depth_first_search
from subpackages.a_star_manhattan_distance import begin_a_star_manhattan_distance
from subpackages.a_star_misplaced_tiles import begin_a_star_misplaced_tiles



def main():
    """Main will run the slider 8 puzzle program by calling necessary functions."""
    menu()

    #This block sets up a visited dictionary to hold the visited states. It then starts the clock_time and creates the
    #initial environment to be used for the search. The initial start state is printed out and the a node is created
    #that stores the initial environments state. The empty position is then found and stored in the previously created
    #node. A string is then created from the nodes starting state array. This is to be used later for checking the
    #visited dictionary. The current_node's state string is then stored with the number node that it is.
    #the desired search is then called. This process is repeated for each block of code.
    visited_map = {}
    start_time = time.clock()
    environment = create_starting_state()
    print_the_game(environment)
    current_node = Node(environment)
    current_node.empty_spot = current_node.find_empty_position()
    current_node.create_state_string()
    visited_map.update({current_node.state_string: 1})
    begin_breadth_first_search(current_node, visited_map, start_time)

    visited_map = {}
    start_time = time.clock()
    environment = create_starting_state()
    current_node = Node(environment)
    current_node.empty_spot = current_node.find_empty_position()
    current_node.create_state_string()
    visited_map.update({current_node.state_string: 1})
    begin_depth_first_search(current_node, visited_map, start_time)

    visited_map = {}
    start_time = time.clock()
    environment = create_starting_state()
    current_node = Node(environment)
    current_node.empty_spot = current_node.find_empty_position()
    current_node.create_state_string()
    visited_map.update({current_node.state_string: 1})
    begin_a_star_misplaced_tiles(current_node, visited_map, start_time)

    visited_map = {}
    start_time = time.clock()
    environment = create_starting_state()
    current_node = Node(environment)
    current_node.empty_spot = current_node.find_empty_position()
    current_node.create_state_string()
    visited_map.update({current_node.state_string: 1})
    begin_a_star_manhattan_distance(current_node, visited_map, start_time)


main()
