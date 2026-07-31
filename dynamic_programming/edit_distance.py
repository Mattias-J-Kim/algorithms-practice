"""
Edit Distance (Levenshtein Distance)
========================================

Note:
    Same table shape as LCS, Longest Common Substring and Sequence
    Alignment, differing only in the objective and the set of choices:
        - Edit Distance: MIN over substitute / insert / delete
        - LCS:           MAX, extend diagonal on a match
        - Alignment:     MAX over match / gap-in-seq1 / gap-in-seq2

    The base cases are what encode the meaning of the table. dp[i][0] = i
    says "turning the first i characters of s1 into an empty string costs
    i deletions"; dp[0][j] = j is the same claim in the other direction.
    Filling them with 0 instead is the usual first mistake, because it
    silently asserts that deleting characters is free.

    On a match the cost carries over unchanged from the diagonal — no +1 —
    since no edit is performed. The +1 in the mismatch branch is applied
    once to whichever of the three predecessors is cheapest.

Problem:
    Given two strings, find the minimum number of single-character
    insertions, deletions or substitutions needed to turn one into the
    other.

    Example:
        s1 = "ABC"
        s2 = "ABCD"
        answer = 1   (insert "D")

DP table definition:
    dp[i][j] = edit distance between s1[0..i) and s2[0..j)

Recurrence:
    if s1[i-1] == s2[j-1]:
        dp[i][j] = dp[i-1][j-1]
    else:
        dp[i][j] = min(dp[i-1][j-1],   # substitute
                       dp[i][j-1],     # insert
                       dp[i-1][j]      # delete
                       ) + 1

Base cases:
    dp[i][0] = i
    dp[0][j] = j
"""


def edit_distance(s1, s2):
    dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
    for j in range(0, len(s2)+1):
        dp[0][j] = j
    for i in range(0, len(s1)+1):
        dp[i][0] = i

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
    return dp[len(s1)][len(s2)]


s1 = "ABC"
s2 = "ABCD"
print(edit_distance(s1, s2))
