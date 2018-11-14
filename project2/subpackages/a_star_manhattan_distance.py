"""A* search uses a heuristic and priority queue to evaluate which states get chosen"""
from __future__ import print_function
import time
import heapq as Q
from subpackages.solve_the_puzzle import check_goal_state, check_visited, add_to_visited, \
     swap_empty_position, print_the_game, print_the_path
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


def begin_a_star_manhattan_distance(initial_node, visited_map, start_time):
    """function to use a* search with misplaced tiles as heuristic search to solve the
    slider puzzle"""
    # The function checks to see if the move is valid (if it is on the board),
    # if the move left is valid, it will create a temporary new_state and it will
    # call the function to swap the empty position with the left position. The new_state is returned and if
    # that state has not been previously visited, the counter is incremented for nodes created and the node is put into
    # the priority queue. This process is the same for each possible position: right, down, and left. The only change is
    # math that is done to look at each position.

    initialize_global_counter()
    queue = create_queue(initial_node)
    current_node = initial_node
    while queue:  # while the queue still contains elements
        current_node = pop_from_queue(queue)
        if not check_goal_state(current_node):  # if goal state was not found
            # check all possible moves
            move_to_top(current_node, visited_map, queue)
            move_to_right(current_node, visited_map, queue)
            move_to_bottom(current_node, visited_map, queue)
            move_to_left(current_node, visited_map, queue)

        else: #The solution was found
            print("The Solution using A* Manhattan Distance was found: ")
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

    if not queue: #The solution was not found so puzzle must have been invalid due to all possibilities being searched
        print("Puzzle was not valid. No solution could be found.")
        print(COUNTER, "nodes were produced.")
        print("%s seconds to exhaust all possibilities" % (time.clock() - start_time))


def create_queue(current_node):
    """add the node passed in to the queue"""
    queue = []
    Q.heappush(queue, (current_node.heuristic, COUNTER, current_node))
    Q.heapify(queue)
    return queue


def pop_from_queue(queue):
    """pop the first element which is a tuple from the queue"""
    popped_node = Q.heappop(queue)
    # grab the node element from the tuple that was popped from the queue
    new_current = popped_node[2]
    return new_current


def move_to_top(current_node, visited_map, queue):
    """function moves the empty state up one position"""
    if (current_node.empty_spot - 3) < 0:
        return

    new_empty_spot = current_node.empty_spot - 3
    # copies the current state to a temporary variable called new_state
    new_state = current_node.start_state[:]
    # makes the swap for the empty position and tile above the empty spot
    new_state = swap_empty_position(new_state, current_node.empty_spot, new_empty_spot)

    # if the new_state is not in the visited map then proceed with making a new node and adding it to the queue
    if not check_visited(visited_map, new_state):
        set_glob_counter()
        add_to_visited(visited_map, new_state, COUNTER)
        new_node = Node(new_state)
        new_node.empty_spot = new_node.find_empty_position()
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        new_node.depth = new_node.set_depth(current_node)
        new_node.heuristic = new_node.calculate_manhattan_distance()
        Q.heappush(queue, (new_node.heuristic, COUNTER, new_node))


def move_to_right(current_node, visited_map, queue):
    """function moves the empty state right one position"""
    if ((current_node.empty_spot + 1) % 3) == 0:
        return
    # from this point, the same steps are repeated as the move_to_up function, but now swapping right
    new_empty_spot = current_node.empty_spot + 1
    new_state = current_node.start_state[:]
    new_state = swap_empty_position(new_state, current_node.empty_spot, new_empty_spot)

    if not check_visited(visited_map, new_state):
        set_glob_counter()
        add_to_visited(visited_map, new_state, COUNTER)
        new_node = Node(new_state)
        new_node.empty_spot = new_node.find_empty_position()
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        new_node.depth = new_node.set_depth(current_node)
        new_node.heuristic =new_node.calculate_manhattan_distance()
        Q.heappush(queue, (new_node.heuristic, COUNTER, new_node))


def move_to_bottom(current_node, visited_map, queue):
    """function moves the empty state down one position"""
    if (current_node.empty_spot + 3) > 8:
        return

    new_empty_spot = current_node.empty_spot + 3
    new_state = current_node.start_state[:]
    new_state = swap_empty_position(new_state, current_node.empty_spot, new_empty_spot)
    # from this point, the same steps are repeated as the move_to_up function, but now swapping down
    if not check_visited(visited_map, new_state):
        set_glob_counter()
        add_to_visited(visited_map, new_state, COUNTER)
        new_node = Node(new_state)
        new_node.empty_spot = new_node.find_empty_position()
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        new_node.depth = new_node.set_depth(current_node)
        new_node.heuristic = new_node.calculate_manhattan_distance()
        Q.heappush(queue, (new_node.heuristic, COUNTER, new_node))


def move_to_left(current_node, visited_map, queue):
    """function moves the empty state left one position if possible."""
    if (current_node.empty_spot % 3) == 0:
        return
    # from this point, the same steps are repeated as the move_to_up function, but now swapping left
    new_empty_spot = current_node.empty_spot - 1
    new_state = current_node.start_state[:]
    new_state = swap_empty_position(new_state, current_node.empty_spot, new_empty_spot)

    if not check_visited(visited_map, new_state):
        set_glob_counter()
        add_to_visited(visited_map, new_state, COUNTER)
        new_node = Node(new_state)
        new_node.empty_spot = new_node.find_empty_position()
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        new_node.depth = new_node.set_depth(current_node)
        new_node.heuristic = new_node.calculate_manhattan_distance()
        Q.heappush(queue, (new_node.heuristic, COUNTER, new_node))
