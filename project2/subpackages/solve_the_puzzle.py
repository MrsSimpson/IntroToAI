"""solve the slider puzzle"""


def menu():
    """Give the user a choice on how to create the puzzle."""
    print("Please select one of the following choices.")
    print("1. Create Random Starting State.")
    print("2. Pick a Starting Space.")


def pick_a_search():
    """Give the user a choice on which search to perform."""
    print("Please select one of the following choices to solve the slider puzzle.")
    print("1. Solve using breadth first search")
    print("2. Solve using depth first search")
    print("3. Solve with A* Search using the number of misplaced tiles.")
    print("4. Solve with A* Search using the manhattan distance")


def create_starting_state():
    """Create the starting state of the puzzle."""
    #environment = [2, 7, 5, 1, 4, 3, 6, 0, 8]
    environment = [7, 8, 3, 4, 1, 5, 6, 0, 2]
    return environment


def find_starting_position(environment):
    """Locate the starting position to begin the search"""
    for i in range(9):
        if environment[i] == 0:
            starting_point = i
            return starting_point
    return None


def check_goal_state(current_node):
    """Check to see if the current node is the goal state"""
    if current_node.start_state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        return True

    return False


def check_visited(visited, new_state):
    """Check to see if the start has been visited already"""
    new_state_string = ""
    for number in new_state:
        new_state_string += str(number)

    if new_state_string in visited:
        return True

    return False


def add_to_visited(visited, new_state, counter):
    """add the string of integers to the dictionary with the counter"""
    environment_string = ""
    for number in new_state:
        environment_string += str(number)

    visited.update({environment_string: counter})


def inc_the_counter(counter):
    counter += 1
    return counter


def swap_empty_position(new_state, current_node, new_empty_spot):
    """Swap the positions in the new environment"""
    new_state[current_node.empty_spot], new_state[new_empty_spot] = new_state[new_empty_spot], new_state[
        current_node.empty_spot]
    return new_state
