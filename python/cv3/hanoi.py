from collections import deque

class State:
    def __init__(self, disks, source, destination, auxiliary):
        self.disks = disks
        self.source = source
        self.destination = destination
        self.auxiliary = auxiliary

class Node:
    def __init__(self, parent, state, move):
        self.parent = parent
        self.state = state
        self.move = move

class HanoiSolver:
    def __init__(self):
        self.final_state = ['C', 'C', 'C']
        self.num_disks = 3
        self.visited = set()

    def solve_hanoi_dfs(self, state):
        stack = []
        initial_node = Node(None, state, None)
        stack.append(initial_node)
        self.visited.add(''.join(state.disks))

        while stack:
            current_node = stack.pop()

            if current_node.state.disks == self.final_state:
                print("Found solution:")
                self.print_path(current_node)
                return

            possible_moves = self.get_possible_moves(current_node.state.disks)

            for move in possible_moves:
                new_state = State(move, current_node.state.source, current_node.state.destination, current_node.state.auxiliary)
                if ''.join(move) not in self.visited:
                    stack.append(Node(current_node, new_state, (move[-1], current_node.state.destination)))
                    self.visited.add(''.join(move))

    def solve_hanoi_bfs(self, state):
        queue = deque()
        initial_node = Node(None, state, None)
        queue.append(initial_node)
        self.visited.add(''.join(state.disks))

        while queue:
            current_node = queue.popleft()

            if current_node.state.disks == self.final_state:
                print("Found solution:")
                self.print_path(current_node)
                return

            possible_moves = self.get_possible_moves(current_node.state.disks)

            for move in possible_moves:
                new_state = State(move, current_node.state.source, current_node.state.destination, current_node.state.auxiliary)
                if ''.join(move) not in self.visited:
                    queue.append(Node(current_node, new_state, (move[-1], current_node.state.destination)))
                    self.visited.add(''.join(move))

    def get_possible_moves(self, state):
        moves = []
        for i in range(self.num_disks):
            disk = state[i]
            top_of_stack = self.get_top_of_stack(disk, state)

            for j in range(3):
                new_state = state[:]
                if j != ord(disk) - ord('A') and state[i] != state[top_of_stack]:
                    new_state[i] = chr(ord('A') + j)
                    moves.append(new_state)
        return moves

    def get_top_of_stack(self, disk, state):
        for i in range(self.num_disks):
            if state[i] == disk:
                return i
        return float('inf')

    def print_path(self, node):
        path = []
        moves = []
        while node is not None:
            path.append(''.join(node.state.disks))
            if node.move is not None:
                moves.append(node.move)
            node = node.parent
        for i in range(len(path)-1, -1, -1):
            print("Move disk from {} to {}".format(*moves.pop()))
            print(path[i])

# Example usage:
solver = HanoiSolver()
initial_state = State(['A', 'A', 'A'], 'A', 'C', 'B')
print("DFS Solution:")
solver.solve_hanoi_dfs(initial_state)
print("\nBFS Solution:")
solver.solve_hanoi_bfs(initial_state)
