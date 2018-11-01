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

main()
