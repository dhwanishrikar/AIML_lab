import random

jobs = [2, 4, 6, 8, 3]
population_size = 6
generations = 15
mutation_rate = 0.2

# Fitness
def fitness(chromosome):
    machine1 = sum(jobs[i] for i in range(5) if chromosome[i] == 0)
    machine2 = sum(jobs[i] for i in range(5) if chromosome[i] == 1)
    return 1 / max(machine1, machine2)

# Initial population
population = [
    [random.randint(0, 1) for _ in jobs]
    for _ in range(population_size)
]

print("Evolution starting...")

for generation in range(generations):

    # Select best two chromosomes
    population.sort(key=fitness, reverse=True)
    parent1 = population[0]
    parent2 = population[1]

    # Crossover
    point = random.randint(1, 3)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    # Mutation
    for child in [child1, child2]:
        if random.random() < mutation_rate:
            position = random.randint(0, 4)
            child[position] = 1 - child[position]

    # Add children and keep best 6
    population += [child1, child2]
    population.sort(key=fitness, reverse=True)
    population = population[:population_size]

    best = population[0]
    makespan = 1 / fitness(best)

    print(f"Gen {generation + 1:2}: Best {best}, Makespan = {makespan:.2f}")

# Final result
best = population[0]

machine1 = [jobs[i] for i in range(5) if best[i] == 0]
machine2 = [jobs[i] for i in range(5) if best[i] == 1]

print("\n--- Optimization Result ---")
print("Best Chromosome:", best)
print("Machine 1 Jobs:", machine1, "Total:", sum(machine1))
print("Machine 2 Jobs:", machine2, "Total:", sum(machine2))
print("Minimum Makespan Found:", max(sum(machine1), sum(machine2)))
