def maximum_capacity(n, capacity, weights):
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + weights[i])

    return dp[capacity]

n = 4
capacity = 10
weights = [2, 3, 4, 5]
print("Maximum Capacity:", maximum_capacity(n, capacity, weights))
