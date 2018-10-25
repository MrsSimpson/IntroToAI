"""File that contains the breadth first search for the slider puzzle"""


from collections import deque
from subpackages.solve_the_puzzle import *
from subpackages.node import Node
import time

COUNTER = 1


def set_glob_counter():
    """increment the global counter"""
    global COUNTER
    COUNTER += 1


def create_queue(current_node):
    """add the node passed in to the queue"""
    queue = deque()
    queue.append(current_node)
    return queue


def pop_from_queue(queue):
    """pop the first element in the queue"""
    popped_node = queue.popleft()
    return popped_node


def begin_breadth_first_search(initial_node, visited_map, start_time):
    """function to use breadth first search to solve the slider puzzle"""
    queue = create_queue(initial_node)
    while queue:  # while the queue still contains elements
        current_node = pop_from_queue(queue)
        if not check_goal_state(current_node):  # if goal state was not found
            move_to_top(current_node, visited_map, queue)
            move_to_right(current_node, visited_map, queue)
            move_to_bottom(current_node, visited_map, queue)
            move_to_left(current_node, visited_map, queue)

        else:
            print("You Won")
            print(current_node.start_state)
            print("%s seconds to find the solution" % (time.clock() - start_time))
            the_string = ""
            for number in current_node.start_state:
                the_string += str(number)
            print(visited_map.get(the_string))
            break

    if not queue:
        print("Puzzle was not valid. No solution could be found.")
        print("%s seconds to find the solution" % (time.clock() - start_time))


def move_to_top(current_node, visited_map, queue):
    """function moves the empty state up one position"""
    if (current_node.empty_spot - 3) < 0:
        return

    new_empty_spot = current_node.empty_spot - 3
    new_state = current_node.start_state[:]
    new_state = swap_empty_position(new_state, current_node, new_empty_spot)

    if not(check_visited(visited_map, new_state)):
        set_glob_counter()
        add_to_visited(visited_map, new_state, COUNTER)
        new_node = Node(new_state)
        new_node.empty_spot = new_node.find_empty_position()
        queue.append(new_node)


def move_to_right(current_node, visited_map, queue):
    """function moves the empty state right one position"""
    if ((current_node.empty_spot + 1) % 3) == 0:
        return

    new_empty_spot = current_node.empty_spot + 1
    new_state = current_node.start_state[:]
    new_state = swap_empty_position(new_state, current_node, new_empty_spot)

    if not(check_visited(visited_map, new_state)):
        set_glob_counter()
        add_to_visited(visited_map, new_state, COUNTER)
        new_node = Node(new_state)
        new_node.empty_spot = new_node.find_empty_position()
        queue.append(new_node)


def move_to_bottom(current_node, visited_map, queue):
    """function moves the empty state down one position"""
    if (current_node.empty_spot + 3) > 8:
        return

    new_empty_spot = current_node.empty_spot + 3
    new_state = current_node.start_state[:]
    new_state = swap_empty_position(new_state, current_node, new_empty_spot)

    if not(check_visited(visited_map, new_state)):
        set_glob_counter()
        add_to_visited(visited_map, new_state, COUNTER)
        new_node = Node(new_state)
        new_node.empty_spot = new_node.find_empty_position()
        queue.append(new_node)


def move_to_left(current_node, visited_map, queue):
    """function moves the empty state left one position if possible."""
    if (current_node.empty_spot % 3) == 0:
        return

    new_empty_spot = current_node.empty_spot - 1
    new_state = current_node.start_state[:]
    new_state = swap_empty_position(new_state, current_node, new_empty_spot)

    if not(check_visited(visited_map, new_state)):
        set_glob_counter()
        add_to_visited(visited_map, new_state, COUNTER)
        new_node = Node(new_state)
        new_node.empty_spot = new_node.find_empty_position()
        queue.append(new_node)