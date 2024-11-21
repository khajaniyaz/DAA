from itertools import permutations
def tsp(cities, distances):
    min_cost = float('inf')
    for perm in permutations(cities):
        cost = sum(distances[perm[i - 1]][perm[i]] for i in range(len(cities)))
        min_cost = min(min_cost, cost + distances[perm[-1]][perm[0]])
    return min_cost

# Test case
distances = {
    'A': {'B': 10, 'C': 15, 'D': 20, 'E': 25},
    'B': {'A': 10, 'C': 35, 'D': 25, 'E': 30},
    'C': {'A': 15, 'B': 35, 'D': 30, 'E': 20},
    'D': {'A': 20, 'B': 25, 'C': 30, 'E': 15},
    'E': {'A': 25, 'B': 30, 'C': 20, 'D': 15},
}
cities = ['A', 'B', 'C', 'D', 'E']
print("Shortest route cost:", tsp(cities, distances))
