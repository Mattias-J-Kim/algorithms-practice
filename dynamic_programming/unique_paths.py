def unique_paths(m, n):
    dp = [[0]*(m) for _ in range(n)]

    for i in range(0, m):
        dp[0][i] = 1
    for j in range(0, n):
        dp[j][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[j][i] = dp[j-1][i] + dp[j][i-1]
    return dp[n-1][m-1]


print(unique_paths(3, 3))
