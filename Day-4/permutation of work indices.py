import itertools
# Function to calculate the total cost of a given assignment
def total_cost(assignment, cost_matrix):
    return sum(cost_matrix[i][task] for i, task in enumerate(assignment))    
# Function to find the optimal assignment using exhaustive search
def assignment_problem(cost_matrix):
    n = len(cost_matrix)
    min_cost = float('inf')
    optimal_assignment = None
    # Generate all permutations of task indices for each worker
    for assignment in itertools.permutations(range(n)):
        cost = total_cost(assignment, cost_matrix)
        if cost < min_cost:
            min_cost = cost
            optimal_assignment = assignment
    # Format the optimal assignment for display
    formatted_assignment = [(f'worker {i+1}', f'task {task+1}') for i, task in enumerate(optimal_assignment)]
    return formatted_assignment, min_cost
cost_matrix = [
    [3, 10, 7],
    [8, 5, 12],
    [4, 6, 9]
]
assignment, cost = assignment_problem(cost_matrix)
print("Optimal Assignment:", assignment)
print("Total Cost:", cost)

Output:
Optimal Assignment: [('worker 1', 'task 3'), ('worker 2', 'task 2'), ('worker 3', 'task 1')]
Total Cost: 16
