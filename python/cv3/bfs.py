def bfs_tower_of_hanoi(n, source, auxiliary, target):
    """
  Vyřeší věž Hanoi pomocí prohledávání do šířky.

  Args:
    n: Počet disků.
    source: Počáteční tyč.
    auxiliary: Pomocná tyč.
    target: Cílová tyč.

  Returns:
    Posloupnost stavů (kroků) vedoucích k cílovému stavu.
  """

    queue = [(n, source, auxiliary, target)]
    visited = set()

    while queue:
        n, source, auxiliary, target = queue.pop(0)
        state = (source, auxiliary, target)

        if state in visited:
            continue

        visited.add(state)

        if n == 1:
            return [(1, source, target)]

        # Přidejte do fronty všechny možné tahy
        queue.append((n - 1, source, target, auxiliary))
        queue.append((1, source, auxiliary, target))
        queue.append((n - 1, auxiliary, source, target))


# Příklad použití
n_disks = 3
start_state = (['A', 'B', 'C'], [], [])
goal_state = ([], [], ['A', 'B', 'C'])

solution = bfs_tower_of_hanoi(n_disks, *start_state)
print(f"Řešení věže Hanoi pomocí BFS ({n_disks} disků):")
for step in solution:
    print(f"Přesuňte disk {step[0]} z tyče {step[1]} na tyč {step[2]}.")
