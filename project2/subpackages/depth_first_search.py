"""contains necessary functions to perform depth first search"""

from __future__ import print_function
import time
from subpackages.solve_the_puzzle import check_goal_state, check_visited, add_to_visited, \
    swap_empty_position, print_the_game
from subpackages.node import Node


COUNTER = 1


def set_glob_counter():
    """increment the global counter"""
    global COUNTER
    COUNTER += 1


def begin_depth_first_search(initial_node, visited_map, start_time):
    """function to use breadth first search to solve the slider puzzle"""

    stack = []

    stack.append(initial_node)

    while stack:  # while the queue still contains elements
        current_node = pop_from_queue(stack)
        if not check_goal_state(current_node):  # if goal state was not found
            move_to_top(current_node, visited_map, stack)
            move_to_right(current_node, visited_map, stack)
            move_to_bottom(current_node, visited_map, stack)
            move_to_left(current_node, visited_map, stack)

        else:
            print("The Solution was found: ")
            print_the_game(current_node.start_state)
            print("It took", "%s seconds to find the solution" % (time.clock() - start_time))
            the_string = ""
            for number in current_node.start_state:
                the_string += str(number)
            print(COUNTER, "nodes were produced before the solution was found")
            print("The solution was found at the", visited_map.get(the_string), "node")
            break

    if not stack:
        print("Puzzle was not valid. No solution could be found.")
        print("%s seconds to find the solution" % (time.clock() - start_time))


def pop_from_queue(stack):
    """pop the first element in the queue"""
    popped_node = stack.pop()
    return popped_node


def move_to_top(current_node, visited_map, stack):
    """function moves the empty state up one position"""
    if (current_node.empty_spot - 3) < 0:
        return

    new_empty_spot = current_node.empty_spot - 3
    new_state = current_node.start_state[:]
    new_state = swap_empty_position(new_state, current_node.empty_spot, new_empty_spot)

    if not check_visited(visited_map, new_state):
        set_glob_counter()
        add_to_visited(visited_map, new_state, COUNTER)
        new_node = Node(new_state)
        new_node.empty_spot = new_node.find_empty_position()
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        stack.append(new_node)


def move_to_right(current_node, visited_map, stack):
    """function moves the empty state right one position"""
    if ((current_node.empty_spot + 1) % 3) == 0:
        return

    new_empty_spot = current_node.empty_spot + 1
    new_state = current_node.start_state[:]
    new_state = swap_empty_position(new_state, current_node.empty_spot, new_empty_spot)

    if not check_visited(visited_map, new_state):
        set_glob_counter()
        add_to_visited(visited_map, new_state, COUNTER)
        new_node = Node(new_state)
        new_node.empty_spot = new_node.find_empty_position()
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        stack.append(new_node)


def move_to_bottom(current_node, visited_map, stack):
    """function moves the empty state down one position"""
    if (current_node.empty_spot + 3) > 8:
        return

    new_empty_spot = current_node.empty_spot + 3
    new_state = current_node.start_state[:]
    new_state = swap_empty_position(new_state, current_node.empty_spot, new_empty_spot)

    if not check_visited(visited_map, new_state):
        set_glob_counter()
        add_to_visited(visited_map, new_state, COUNTER)
        new_node = Node(new_state)
        new_node.empty_spot = new_node.find_empty_position()
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        stack.append(new_node)


def move_to_left(current_node, visited_map, stack):
    """function moves the empty state left one position if possible."""
    if (current_node.empty_spot % 3) == 0:
        return

    new_empty_spot = current_node.empty_spot - 1
    new_state = current_node.start_state[:]
    new_state = swap_empty_position(new_state, current_node.empty_spot, new_empty_spot)

    if not check_visited(visited_map, new_state):
        set_glob_counter()
        add_to_visited(visited_map, new_state, COUNTER)
        new_node = Node(new_state)
        new_node.empty_spot = new_node.find_empty_position()
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        stack.append(new_node)
