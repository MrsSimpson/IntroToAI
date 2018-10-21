"""solve the slider puzzle"""


def create_starting_state():
    """Create the starting state of the puzzle."""
    environment = [7, 8, 3, 4, 1, 5, 6, 0, 2]
    return environment


def find_starting_position(environment):
    """Locate the starting position to begin the search"""
    starting_point = None
    for i in range(10):
        if environment[i] == 0:
            starting_point = i

    return starting_point


def check_visited(visited, current_node):
    """Check to see if the start has been visited already"""

    for element in visited:
        if element == current_node.start_state:
            return True

    return False
