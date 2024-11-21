def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]

# Example usage
weights = [1, 2, 3, 8]
values = [20, 5, 10, 40]
capacity = 5
print(knapsack(weights, values, capacity))  # Output: 60
