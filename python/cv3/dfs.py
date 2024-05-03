def move_disk(n, source, target):
    """Prints the instruction to move a disk."""
    print(f"Move disk {n} from {source} to {target}")


def tower_of_hanoi(n, source, auxiliary, target, start_state, goal_state):
    """Solves the Tower of Hanoi problem with custom start and goal states."""

    # Check if the current state matches the goal state
    if start_state == goal_state:
        return

    # Recursive helper function
    def _hanoi(n, source, auxiliary, target):
        if n == 1:
            move_disk(1, source, target)
            start_state[source].pop()
            start_state[target].append(1)
            return

        # Move smaller disks to the auxiliary rod
        _hanoi(n - 1, source, target, auxiliary)

        # Move the largest disk to the target rod
        move_disk(n, source, target)
        start_state[source].pop()
        start_state[target].append(n)

        # Move smaller disks back to the source rod on top of the largest disk
        _hanoi(n - 1, auxiliary, source, target)

    # Start the solving process
    _hanoi(n, source, auxiliary, target)


# Example usage:
n_disks = 3
start_state = [[3, 2, 1], [], []]
goal_state = [[], [], [3, 2, 1]]

print("Tower of Hanoi using recursion:")
tower_of_hanoi(n_disks, 'A', 'B', 'C', start_state.copy(), goal_state.copy())
