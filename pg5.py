import numpy as np

# 1. Physical Data (Mass & Stiffness matrices for a 2-degree system)
M = np.array([[2, 0], [0, 1]])
K = np.array([[6, -2], [-2, 4]])

# 2. GA Parameters
pop_size = 20
generations = 30

# 3. Initialize Population (Random 2D displacement vectors)
pop = np.random.uniform(0.1, 1.0, (pop_size, 2))


# 4. Rayleigh Quotient Function (Lower score = Better)
def get_rayleigh(x):
    return (x @ K @ x) / (x @ M @ x)


# 5. Evolution Loop
for gen in range(generations):
    # Calculate scores (Rayleigh values) for everyone
    scores = np.array([get_rayleigh(ind) for ind in pop])

    # Print the best result of this generation
    best_idx = np.argmin(scores)
    if gen % 10 == 0 or gen == generations - 1:
        print(
            f"Gen {gen:02d} | Best Vector: {np.round(pop[best_idx], 3)} | Min Frequency Value: {scores[best_idx]:.4f}"
        )

    # Selection: Pick the top 50% individuals to be parents
    parents = pop[np.argsort(scores)[: pop_size // 2]]

    # Breeding: Next generation starts with current parents
    next_pop = list(parents)

    # Create children until the population is full
    while len(next_pop) < pop_size:
        p1, p2 = parents[np.random.choice(len(parents), 2, replace=False)]

        # Crossover (Mix vectors) & Mutation (Add small random change)
        child = np.array([p1[0], p2[1]]) + np.random.normal(0, 0.05, 2)
        next_pop.append(np.clip(child, 0.01, 2.0))  # Keep values positive

    pop = np.array(next_pop)
