"""contains necessary functions to perform depth first search. Uses the stack data structure."""

from __future__ import print_function
import time
from subpackages.solve_the_puzzle import check_goal_state, check_visited, add_to_visited, \
    swap_empty_position, print_the_game
from subpackages.node import Node
import csv


COUNTER = 0

def initialize_global_counter():
    """Set the global counter back to zero"""
    global COUNTER
    COUNTER = 1

def set_glob_counter():
    """increment the global counter"""
    global COUNTER
    COUNTER += 1


def begin_depth_first_search(initial_node, visited_map, start_time):
    """function to use depth first search to solve the slider puzzle"""
    #The function checks to see if the move is valid (if it is on the board),
    #if the move left is valid, it will create a temporary new_state and it will
    #call the function to swap the empty position with the left position. The new_state is returned and if
    #that state has not been previously visited, the counter is incremented for nodes created and the node is put into
    #the stack. This process is the same for each possible position: right, down, and left. The only change is
    #math that is done to look at each position.

    stack = []
    initialize_global_counter()
    stack.append(initial_node)
    current_node = initial_node
    while stack:  # while the queue still contains elements
        current_node = pop_from_queue(stack)
        if not check_goal_state(current_node):  # if goal state was not found
            move_to_top(current_node, visited_map, stack)
            move_to_right(current_node, visited_map, stack)
            move_to_bottom(current_node, visited_map, stack)
            move_to_left(current_node, visited_map, stack)

        else:
            my_timer = str((time.clock() - start_time))
            with open('report.csv', 'a', newline='') as file:
                line_write = csv.writer(file)
                line_write.writerow(
                    ['DFS', initial_node.start_state, 'True', current_node.depth, '', COUNTER, my_timer])
            print("The Solution was found: ")
            print_the_game(current_node.start_state)
            print("It took", "%s seconds to find the solution" % (time.clock() - start_time))
            the_string = ""
            for number in current_node.start_state:
                the_string += str(number)
            print(COUNTER, "nodes were produced before the solution was found")
            print("The depth of the solution was found at:", current_node.depth)
            print("The solution was found at the", visited_map.get(the_string), "node")
            break

    if not stack:
        my_timer = str((time.clock() - start_time))
        with open('report.csv', 'a', newline='') as file:
            line_write = csv.writer(file)
            line_write.writerow(['DFS', initial_node.start_state, 'False', current_node.depth, '', COUNTER, my_timer])
        print("Puzzle was not valid. No solution could be found.")
        print(COUNTER, "nodes were produced.")
        print("%s seconds to exhaust all possibilities" % (time.clock() - start_time))


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
        new_node.depth = new_node.set_depth(current_node)
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
        new_node.depth = new_node.set_depth(current_node)
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
        new_node.depth = new_node.set_depth(current_node)
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
        new_node.depth = new_node.set_depth(current_node)
        stack.append(new_node)
