"""node class used for creating new node states"""


class Node:
    """node class used for creating new node states"""
    def __init__(self, environment):
        self.start_state = environment
        self.empty_spot = self.find_empty_position()
        self.depth = 0
        self.heuristic = 0
        self.is_visited = False
        self.path = []

    def find_empty_position(self):
        """find the empty position of the node's state"""
        empty_position = -1
        for i in range(10):
            if self.start_state[i] == 0:
                empty_position = i
        return empty_position

    def set_is_visited(self):
        """set the visited boolean to true"""
        self.is_visited = True

    def set_path(self, previous_node):
        """set the path of the open position"""
        if not previous_node.path:
            self.path.append(self.empty_spot)
        else:
            self.path.append(previous_node.path)
            self.path.append(self.empty_spot)
