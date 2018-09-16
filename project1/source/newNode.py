class newNode:
    def __init__(self, row, column):
        self.location = {(10 * row) + column}
        self.fringe = []
