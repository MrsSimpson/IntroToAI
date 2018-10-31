"""Run the slider 8 program"""


from subpackages.user_menu import menu
from subpackages.solve_the_puzzle import *
from subpackages.node import *
from subpackages.breadth_first_search import *
from subpackages.depth_first_search import *
from subpackages.a_star_manhattan_distance import *
from subpackages.a_star_misplaced_tiles import *
import time


def main():
    """Main will run the slider 8 puzzle program by calling necessary functions."""
    #menu()

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
