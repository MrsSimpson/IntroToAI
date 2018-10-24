"""File that contains the breadth first search for the slider puzzle"""


from collections import deque
from subpackages.solve_the_puzzle import *


def add_to_queue(current_node):
    """add the node passed in to the queue"""
    queue = deque(current_node)
    return queue


def pop_from_queue(queue):
    """pop the first element in the queue"""
    popped_node = queue.popleft()
    return popped_node


def begin_breadth_first_search(initial_node):
    """function to use breadth first search to solve the slider puzzle"""
    queue = add_to_queue(initial_node)
    while not queue:  # while the queue still contains elements
        current_node = pop_from_queue(queue)
        if not check_goal_state(current_node):  # if goal state was not found
            empty_spot = find_starting_position(current_node.start_state)
