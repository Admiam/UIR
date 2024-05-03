import random

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def create_population(num_items):
    return [random.randint(0, 1) for _ in range(num_items)]

def fitness_function(chromosome, items, capacity):
    total_weight = 0
    total_value = 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_weight += items[i].weight
            total_value += items[i].value
            if total_weight > capacity:
                return 0
    return total_value

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(chromosome, mutation_rate):
    mutated_chromosome = []
    for gene in chromosome:
        if random.random() < mutation_rate:
            mutated_chromosome.append(int(not gene))
        else:
            mutated_chromosome.append(gene)
    return mutated_chromosome

def genetic_algorithm(items, capacity, population_size=100, generations=100, crossover_rate=0.8, mutation_rate=0.01):
    population = [create_population(len(items)) for _ in range(population_size)]

    for _ in range(generations):
        population = sorted(population, key=lambda x: fitness_function(x, items, capacity), reverse=True)
        new_population = [population[0]]

        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population[:10], k=2)

            offspring1, offspring2 = crossover(parent1, parent2)
            offspring1 = mutate(offspring1, mutation_rate)
            offspring2 = mutate(offspring2, mutation_rate)

            new_population.extend([offspring1, offspring2])
        population = new_population

    best_solution = max(population, key=lambda x: fitness_function(x, items, capacity))
    selected_items = [items[i] for i in range(len(best_solution)) if best_solution[i] == 1]
    return selected_items, best_solution

def read_file(file_name):
    with open(file_name, 'r') as f:
        f.readline()
        capacity = int(f.readline())
        f.readline()
        items = []

        for line in f:
            parts = line.strip().split(";")
            items.append(Item(int(parts[1]), int(parts[2])))

    return capacity, items



def main():
    capacity, items = read_file("cv6_vstup.txt")
    total_weight, total_value = 0, 0
    print(capacity)
    print(items)

    selected_items, best_solution = genetic_algorithm(items, capacity)
    print("Selected items in the backpack:")
    for item in selected_items:
        print(f"Weight: {item.weight}, Value: {item.value}")
        total_weight += item.weight
        total_value += item.value

    print(f"Total weight: {total_weight}")
    print(f"Total value: {total_value}")
    print(best_solution)

if __name__ == "__main__":
    main()
