def dfs_tower_of_hanoi(n, source, auxiliary, target):
  """
  Vyřeší věž Hanoi pomocí prohledávání do hloubky.

  Args:
    n: Počet disků.
    source: Počáteční tyč.
    auxiliary: Pomocná tyč.
    target: Cílová tyč.

  Returns:
    Posloupnost stavů (kroků) vedoucích k cílovému stavu.
  """

  def _dfs(n, source, auxiliary, target, solution):
    if n == 1:
      solution.append((1, source, target))
      return

    _dfs(n-1, source, target, auxiliary, solution)
    solution.append((1, source, target))
    _dfs(n-1, auxiliary, source, target, solution)

  solution = []
  _dfs(n, source, auxiliary, target, solution)
  return solution

# Příklad použití
n_disks = 3
start_state = (['A', 'B'], [], ['C'])
goal_state = ([], [], ['A', 'B', 'C'])

solution = dfs_tower_of_hanoi(n_disks, *start_state)
print(f"Řešení věže Hanoi pomocí DFS ({n_disks} disků):")
for step in solution:
  print(f"Přesuňte disk {step[0]} z tyče {step[1]} na tyč {step[2]}.")
