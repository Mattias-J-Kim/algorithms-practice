"""
Longest Palindromic Subsequence (LPS)
========================================

Learning note:
    The key insight — that LPS(s) = LCS(s, reverse(s)) — was given as a
    starting hint, but the DP table itself was built from scratch by
    directly reusing the LCS recurrence from earlier work in this repo
    (longest_common_subsequence.py). Two bugs came up while adapting
    it, both worth recording:

    Bug 1: On a match, briefly tried
        dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
    This happened to give the right answer on the first test string, but
    failed on a harder case (e.g. "AABBAABA" gives 7 instead of the
    correct 6). The reason: dp[i-1][j] and dp[i][j-1] represent states
    where only ONE of the two strings has advanced — adding +1 to them
    on a match assumes a matched pair without actually consuming both
    characters, which inflates the count.

    Bug 2 (a milder version of the same mistake): tried
        dp[i][j] = max(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
    on a match. Same root problem — +1 must ONLY ever be added to the
    diagonal dp[i-1][j-1], because that's the only state where "both
    characters were already consumed before this match."

    Fix: on a match, there is exactly ONE correct predecessor —
        dp[i][j] = dp[i-1][j-1] + 1   (no max/min needed here at all)
    max() is only needed in the mismatch branch, where a real choice
    (skip one character from either side) exists.

Problem:
    Given a string, find the length of the longest subsequence (order
    preserved, not necessarily contiguous) that reads the same forwards
    and backwards.

    Example:
        s = "BBABCBCAB"
        answer = 7

Reduction to LCS:
    A palindromic subsequence of s is, by definition, a subsequence that
    equals its own reverse. So the longest palindromic subsequence of s
    is exactly the longest common subsequence between s and reverse(s).

DP table definition:
    dp[i][j] = LCS length between s[0..i) and reverse(s)[0..j)

Recurrence:
    if s[i-1] == reverse(s)[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1        # exactly one predecessor
    else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
"""


def longest_palindromic_subsequence(s: str) -> int:
    s_rev = s[::-1]
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s_rev[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][n]


s = "BBABCBCAB"
print(longest_palindromic_subsequence(s))
