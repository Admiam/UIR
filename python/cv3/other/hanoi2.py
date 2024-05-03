from collections import deque


# Funkce pro zjistění následníků aktuálního stavu
def successors(state):
    successors = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j and (not state[i] or state[j] and state[i][-1] > state[j][-1]):
                new_state = state[:]
                new_state[j] = new_state[j] + [new_state[i].pop()]
                successors.append(new_state)
    return successors


# Funkce pro prohledávání do šířky
def breadth_first_search(start, goal):
    frontier = deque([(start, [start])])
    while frontier:
        state, path = frontier.popleft()
        if state == goal:
            return path
        for successor in successors(state):
            if successor not in path:
                frontier.append((successor, path + [successor]))


# Funkce pro prohledávání do hloubky
def depth_first_search(start, goal):
    frontier = [(start, [start])]
    while frontier:
        state, path = frontier.pop()
        if state == goal:
            return path
        for successor in successors(state):
            if successor not in path:
                frontier.append((successor, path + [successor]))


# Příklad použití
start_state = [[3, 2, 1], [], []]
goal_state = [[], [], [3, 2, 1]]

print("Breadth First Search:")
print(breadth_first_search(start_state, goal_state))

print("\nDepth First Search:")
print(depth_first_search(start_state, goal_state))
