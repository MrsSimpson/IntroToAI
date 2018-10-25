"""node class used for creating new node states"""


class Node:
    """node class used for creating new node states"""
    def __init__(self, environment):
        self.start_state = environment
        self.state_string = ""
        self.empty_spot = None
        self.depth = 0
        self.heuristic = 0
        self.is_visited = False
        self.path = []

    def find_empty_position(self):
        """find the empty position of the node's state"""
        for i in range(10):
            if self.start_state[i] == 0:
                empty_position = i
                return empty_position
        return None

    def create_state_string(self):
        """create string of integers found in the array for start_state"""
        for number in self.start_state:
            self.state_string += str(number)
        return self.state_string

    def set_path(self, previous_node):
        """set the path of the open position"""
        if not previous_node.path:
            self.path.append(self.empty_spot)
        else:
            self.path.append(previous_node.path)
            self.path.append(self.empty_spot)
