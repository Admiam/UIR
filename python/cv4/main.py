import networkx as nx
import heapq

def heuristic(node, heuristic_values):
    """
    Heuristická funkce, která poskytuje odhadovanou vzdálenost mezi uzly.
    Zde můžete implementovat například Euklidovskou vzdálenost, Manhattan vzdálenost, atd.
    """
    # Příklad: Euklidovská vzdálenost
    if (heuristic_values == None):
        return 0
    return heuristic_values[node]

def astar(graph, start, goal):
    """
    A* algoritmus pro hledání nejkratší cesty v ohodnoceném grafu.
    """
    # Prioritní fronta pro udržení uzlů k prozkoumání
    open_list = []
    heapq.heappush(open_list, (0, start))  # (f(n), uzel)

    # Slovník pro udržení délky cesty od startovního uzlu
    g_scores = {start: 0}

    # Slovník pro udržení rodičovského uzlu pro každý uzel
    parents = {start: None}

    while open_list:
        # Vyber uzel s nejnižší hodnotou f(n)
        current_cost, current_node = heapq.heappop(open_list)

        # Pokud dosáhneme cílového uzlu, končíme
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parents[current_node]
            return path[::-1], g_scores  # Vrátíme cestu od startu ke cíli

        # Procházej všechny sousední uzly
        for neighbor in graph.neighbors(current_node):
            # Spočítej novou délku cesty
            new_g = g_scores[current_node] + graph[current_node][neighbor].get('weight', 1)

            # Pokud sousední uzel ještě nebyl objeven nebo nová cesta je kratší
            if neighbor not in g_scores or new_g < g_scores[neighbor]:
                g_scores[neighbor] = new_g
                f_score = new_g + heuristic(neighbor, heuristic_values)
                heapq.heappush(open_list, (f_score, neighbor))
                parents[neighbor] = current_node

    # Pokud není nalezena žádná cesta
    return None

def load(file_name):
    graph = nx.Graph()
    fread = open(file_name, 'r')
    heuristic_values = {}

    fread.readline() # start:
    start_node = fread.readline().strip('\n') # S
    fread.readline() # cil:
    goal_node = fread.readline().strip('\n') # G
    fread.readline() # seznam sousednosti:
    line = fread.readline().strip('\n') # A;S=36;C=13;G=43

    #########   seznam osudensoti   #########
    while line != "vzdusna vzdalenost od cile:":
        graph.add_node(line[0])
        values = line.split(";")[1:]
        for x in values:
            key, value = x.split("=") # S=36;C=13;G=43
            graph.add_edge(line[0], key, weight=int(value))
        line = fread.readline().strip('\n')

    #########   vzdusna vzdalenost od cile   #########
    line = fread.readline().strip('\n')  # A=26
    while line:
        key, value = line.split("=")
        heuristic_values[key] = int(value)
        line = fread.readline().strip('\n')
    heuristic_values[goal_node] = 0
    return start_node, goal_node, graph, heuristic_values



if __name__ == '__main__':
    start_node, goal_node, graph, heuristic_values = load("cv4_vstup_test.txt")
    shortest_path, scores = astar(graph, start_node, goal_node)
    print("Nejkratší cesta: ", shortest_path)
    print("Hodnota: ", scores)
