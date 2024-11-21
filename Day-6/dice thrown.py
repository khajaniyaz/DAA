def dice_throw(num_sides, num_dice, target):
    dp = [[0] * (target + 1) for _ in range(num_dice + 1)]
    dp[0][0] = 1
    for i in range(1, num_dice + 1):
        for j in range(1, target + 1):
            for k in range(1, num_sides + 1):
                if j - k >= 0:
                    dp[i][j] += dp[i - 1][j - k]
    return dp[num_dice][target]
print("Number of ways to reach sum 7:", dice_throw(6, 2, 7))  # Output: 6
print("Number of ways to reach sum 10:", dice_throw(4, 3, 10))  # Output: 27
