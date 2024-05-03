class TowerOfHanoi:
    def __init__(self, start, aux, end):
        self.start = start
        self.aux = aux
        self.end = end

    def move(self, source, dest):
        if source and (not dest or source[-1] < dest[-1]):
            dest.append(source.pop())
            return True
        return False

    def status(self):
        print("Start:", self.start)
        print("Aux:", self.aux)
        print("End:", self.end)


class HanoiSolver:
    def __init__(self, start, aux, end):
        self.start = start
        self.aux = aux
        self.end = end
        self.goal = [3, 2, 1]

    def dfs(self, source, dest, aux):
        if len(dest) == 3:
            return True
        if self.move(source, dest):
            if self.dfs(self.start, self.end, self.aux) or self.dfs(self.start, self.aux, self.end):
                return True
            self.move(dest, source)
        return False

    def bfs(self):
        queue = [(self.start, self.aux, self.end)]
        visited = set()
        while queue:
            source, aux, dest = queue.pop(0)
            if tuple(source) in visited:
                continue
            if source == self.goal:
                return True
            visited.add(tuple(source))
            for src, dst in [(source, aux), (source, dest), (aux, source), (aux, dest), (dest, source), (dest, aux)]:
                if self.move(src, dst):
                    queue.append((source[:], aux[:], dest[:]))
                    self.move(dst, src)
        return False

    def solve_dfs(self):
        print("\nDepth First Search:")
        if self.dfs(self.start, self.end, self.aux):
            self.print_result()
        else:
            print("No solution found.")

    def solve_bfs(self):
        print("\nBreadth First Search:")
        if self.bfs():
            self.print_result()
        else:
            print("No solution found.")

    def print_result(self):
        print("Solution Found:")
        print("Start:", self.start)
        print("Aux:", self.aux)
        print("End:", self.end)

    def move(self, src, dst):
        pass


if __name__ == "__main__":
    start_state = [3, 2, 1]
    aux_state = []
    end_state = []

    hanoi_solver = HanoiSolver(start_state, aux_state, end_state)
    hanoi_solver.solve_dfs()
    hanoi_solver.solve_bfs()
