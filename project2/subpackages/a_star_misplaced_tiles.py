"""A* search uses a heuristic and priority queue to evaluate which states get chosen"""
from __future__ import print_function
import time
import heapq as Q
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


def begin_a_star_misplaced_tiles(initial_node, visited_map, start_time):
    """function to use a* search with misplaced tiles as heuristic search to
       solve the slider puzzle"""
    queue = create_queue(initial_node)
    initialize_global_counter()
    depth = 0
    while queue:  # while the queue still contains elements
        current_node = pop_from_queue(queue)
        if not check_goal_state(current_node):  # if goal state was not found
            depth += 1
            move_to_top(current_node, visited_map, queue, depth)
            move_to_right(current_node, visited_map, queue, depth)
            move_to_bottom(current_node, visited_map, queue, depth)
            move_to_left(current_node, visited_map, queue, depth)

        else:
            print("The Solution was found: ")
            print_the_game(current_node.start_state)
            print("It took", "%s seconds to find the solution" % (time.clock() - start_time))
            the_string = ""
            for number in current_node.start_state:
                the_string += str(number)
            print(COUNTER, "nodes were produced before the solution was found")
            print("The depth of the solution was found at: ", current_node.depth)
            print("The solution was found at the", visited_map.get(the_string), "node")
            print(current_node.path)
            break

    if not queue:
        print("Puzzle was not valid. No solution could be found.")
        print(COUNTER, "nodes were produced.")
        print("%s seconds to exhaust all possibilities" % (time.clock() - start_time))


def create_queue(current_node):
    """add the node passed in to the queue"""
    queue = []
    Q.heappush(queue, (current_node.heuristic * COUNTER, COUNTER, current_node))
    Q.heapify(queue)
    return queue


def pop_from_queue(queue):
    """pop the first element in the queue"""
    popped_node = Q.heappop(queue)
    new_current = popped_node[2]
    return new_current


def move_to_top(current_node, visited_map, queue, depth):
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
        new_node.depth = depth
        new_node.heuristic = COUNTER + new_node.calculate_misplaced_tiles()
        Q.heappush(queue, (new_node.heuristic * COUNTER, COUNTER, new_node))


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
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        new_node.depth = depth
        new_node.heuristic = COUNTER + new_node.calculate_misplaced_tiles()
        Q.heappush(queue, (new_node.heuristic * COUNTER, COUNTER, new_node))


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
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        new_node.depth = depth
        new_node.heuristic = COUNTER + new_node.calculate_misplaced_tiles()
        Q.heappush(queue, (new_node.heuristic * COUNTER, COUNTER, new_node))


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
        new_node.set_path = new_node.set_path(current_node, new_empty_spot)
        new_node.depth = depth
        new_node.heuristic = COUNTER + new_node.calculate_misplaced_tiles()
        Q.heappush(queue, (new_node.heuristic * COUNTER, COUNTER, new_node))

