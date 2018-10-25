"""Run the slider 8 program"""

import time
from subpackages.breadth_first_search import *
from subpackages.solve_the_puzzle import *
from subpackages.node import Node



def main():
    """Main will run the slider 8 puzzle program by calling necessary functions."""
    menu()
    visited_map = {}
    initial_environment = create_starting_state()
    start_time = time.clock()
    current_node = Node(initial_environment)
    current_node.empty_spot = current_node.find_empty_position()
    current_node.create_state_string()
    visited_map.update({current_node.state_string: 1})
    begin_breadth_first_search(current_node, visited_map, start_time)


main()
