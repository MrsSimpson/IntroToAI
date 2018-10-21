"""Run the slider 8 program"""


from subpackages.solve_the_puzzle import create_starting_state


def main():
    """Main will run the slider 8 puzzle program by calling necessary functions."""
    menu()
    initial_environment = create_starting_state()


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


main()
