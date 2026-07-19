def Longest_Common_Substring(s1, s2):
    dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(0, len(s1)+1):
        dp[i][0] = 0
    for j in range(0, len(s2)+1):
        dp[0][j] = 0

    max_len = 0

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = 0
            max_len = max(max_len, dp[i][j])
    return max_len


s1 = "AXB"
s2 = "AYB"
print(Longest_Common_Substring(s1, s2))
