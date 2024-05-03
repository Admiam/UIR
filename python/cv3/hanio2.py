class HanoiSolver:

    def __init__(self):
        self.goal_state = ['C', 'C', 'C']
        self.num_rods = 3
        self.visited = set()
        self.path = []

    def solve_hanoi_dfs(self, state):
        stack = [Node(None, State(state))]
        self.visited.add(toStringMuj(state))
        possible_moves = []

        while stack:
            current_state = stack.pop()

            if current_state.is_done(self.goal_state):
                print(toStringMuj(current_state.s.state))
                print("Solution found.")
                self.print_path(current_state)
                return

            possible_moves = self.get_possible_moves(current_state.s.state)

            for move in possible_moves:
                print(f"Adding to stack: {toStringMuj(move)}")
                new_state = move.copy()
                next_state = State(new_state)
                next_node = Node(current_state, next_state)
                next_node.parent = current_state
                stack.append(next_node)

            print("---")

    def get_possible_moves(self, state):
        possible_moves = []

        for i in range(self.num_rods):
            disk = state[i]
            top_element_in_rod = self.get_top_element_in_rod(disk, state)

            for j in range(3):
                other_disk = chr(ord('A') + j)
                top_element_in_other_rod = self.get_top_element_in_rod(other_disk, state)

                if top_element_in_rod < top_element_in_other_rod and not self.is_anyone_above(i, state):
                    new_state = state.copy()
                    new_state[i] = other_disk
                    print(toStringMuj(new_state))

                    if toStringMuj(new_state) not in self.visited:
                        possible_moves.append(new_state)
                        self.visited.add(toStringMuj(new_state))

        return possible_moves

    def is_anyone_above(self, rod, state):
        disk_at_rod = state[rod]

        if rod == 0:
            return False
        elif rod == 1:
            return disk_at_rod == state[0]
        else:
            return disk_at_rod == state[0] or disk_at_rod == state[1]

    def print_path(self, node):
        current_node = node

        while current_node.parent:
            self.path.append(toStringMuj(current_node.s.state))
            current_node = current_node.parent

        for i in range(len(self.path) - 1, -1, -1):
            print(self.path[i])

    def get_top_element_in_rod(self, disk, state):
        for i in range(self.num_rods):
            if state[i] == disk:
                return i

        return float('inf')

    def toStringMuj(self, state):
        return ''.join(state)


def main():
    solver = HanoiSolver()
    initial_state = ['A', 'B', 'C']
    solver.solve_hanoi_dfs(initial_state)


if __name__ == "__main__":
    main()
