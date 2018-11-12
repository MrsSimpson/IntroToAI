"""File that contains the breadth first search for the slider puzzle.
 Uses the queue data structure to store nodes."""


from __future__ import print_function
import time
from collections import deque
from subpackages.solve_the_puzzle import check_goal_state, check_visited, add_to_visited, \
    swap_empty_position, print_the_game, print_the_path
from subpackages.node import Node


COUNTER = 0

def initialize_global_counter():
    """Set the global counter back to zero"""
    global COUNTER
    COUNTER = 1


def set_glob_counter():
    """increment the global counter"""
    global COUNTER
    COUNTER += 1


def begin_breadth_first_search(initial_node, visited_map, start_time):
    """function to use breadth first search to solve the slider puzzle"""
    #The function creates the queue with the initial node that is passed in to the function.
    #While the queue is notempty, the node at the front of the queue is popped and the
    #function checks to see if it contains the goal state. If the node does not contain the
    #goal state, the function checks the top position, right position, bottom position,
    #and the left position. If the solution is found, the results are printed to the screen.
    #If the queue is empty and the result was not found, a message is displayed saying that
    #the state was not valid.
    initialize_global_counter()
    depth = 0
    queue = create_queue(initial_node)
    while queue:  # while the queue still contains elements
        current_node = pop_from_queue(queue)
        if not check_goal_state(current_node):  # if goal state was not found
            depth += 1
            move_to_top(current_node, visited_map, queue, depth)
            move_to_right(current_node, visited_map, queue, depth)
            move_to_bottom(current_node, visited_map, queue, depth)
            move_to_left(current_node, visited_map, queue, depth)

        else:
            print("The Solution using Breadth First Search was found: ")
            print_the_game(current_node.start_state)
            print("It took", "%s seconds to find the solution" % (time.clock() - start_time))
            the_string = ""
            for number in current_node.start_state:
                the_string += str(number)
            print(COUNTER, "nodes were produced before the solution was found")
            print("The depth of the solution was found at: ", current_node.depth)
            print("The solution was found at the", visited_map.get(the_string), "node")
            print_the_path(current_node.path)
            break

    if not queue:
        print("Puzzle was not valid. No solution could be found.")
        print(COUNTER, "nodes were produced.")
        print("%s seconds to exhaust all possibilities" % (time.clock() - start_time))


def create_queue(current_node):
    """add the node passed in to the queue"""
    #using the deque library to build the queue.
    queue = deque()
    queue.append(current_node)
    return queue


def pop_from_queue(queue):
    """pop the first element in the queue and return it"""
    popped_node = queue.popleft()
    return popped_node


def move_to_top(current_node, visited_map, queue, depth):
    """function moves the empty state up one position"""
    #The function checks to see if the move is valid (if it is on the board),
    #if the move left is valide, it will create a temporary new_state and it will
    #call the function to swap the empty position with the left position. The new_state is
    #returned and if that state has not been previously visited, the counter is incremented
    #for nodes created and the node is put into the queue. This process is the same for each
    #possible position: right, down, and left. The only change is math that is done to look
    #at each position.
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
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        queue.append(new_node)


def move_to_right(current_node, visited_map, queue, depth):
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
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        queue.append(new_node)


def move_to_bottom(current_node, visited_map, queue, depth):
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
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        queue.append(new_node)


def move_to_left(current_node, visited_map, queue, depth):
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
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        queue.append(new_node)
