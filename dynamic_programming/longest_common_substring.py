"""
Longest Common Substring
============================

Note:
    This differs from Longest Common Subsequence in exactly two places,
    and both differences come from the same requirement — the match must
    be contiguous.

    1. On a mismatch, dp[i][j] is reset to 0 rather than carrying over
       max(dp[i-1][j], dp[i][j-1]). Carrying over is what allows a
       subsequence to skip characters; a substring cannot skip, so any
       mismatch ends the run and the count restarts.

    2. The answer is a running maximum taken across every cell, not
       dp[len(s1)][len(s2)]. Because runs are reset, the final cell only
       holds the run ending at the last character of both strings, which
       is usually not the longest one. This is the same distinction as in
       LIS, where the answer is max(dp) rather than dp[-1].

    dp[i][j] therefore means "length of the common substring ENDING at
    s1[i-1] and s2[j-1]", not "best answer so far within the prefixes" —
    a state definition indexed by ending position rather than by prefix.

Problem:
    Given two strings, find the length of the longest string that appears
    as a contiguous block in both.

    Example:
        s1 = "AXB"
        s2 = "AYB"
        answer = 1   ("A" or "B"; "AB" is a subsequence, not a substring)

DP table definition:
    dp[i][j] = length of the common substring ending exactly at s1[i-1]
               and s2[j-1]

Recurrence:
    if s1[i-1] == s2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
    else:
        dp[i][j] = 0

Final answer:
    max over all dp[i][j] — NOT dp[len(s1)][len(s2)]
"""


def longest_common_substring(s1, s2):
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
print(longest_common_substring(s1, s2))
