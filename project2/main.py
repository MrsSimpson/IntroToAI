"""Run the slider 8 program"""

import time
from subpackages.breadth_first_search import begin_breadth_first_search
from subpackages.depth_first_search import begin_depth_first_search
from subpackages.solve_the_puzzle import create_starting_state, menu
from subpackages.node import Node


def main():
    """Main will run the slider 8 puzzle program by calling necessary functions."""
    visited_map = {}
    initial_environment = menu()
    start_time = time.clock()
    current_node = Node(initial_environment)
    current_node.empty_spot = current_node.find_empty_position()
    current_node.create_state_string()
    visited_map.update({current_node.state_string: 1})
    begin_breadth_first_search(current_node, visited_map, start_time)

   # visited_map = {}
   # start_time = time.clock()
   # visited_map.update({current_node.state_string: 1})
   # begin_depth_first_search(current_node, visited_map, start_time)


main()
