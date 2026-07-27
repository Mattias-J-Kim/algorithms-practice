"""
Longest Common Subsequence (LCS)
==============================================================
Learning note:
    This came together faster than Sequence Alignment did. The DP
    table setup (base cases, two nested loops, i/j indexing into
    seq1/seq2) followed the exact same shape as Edit Distance and
    Sequence Alignment, so most of the structure was already familiar
    before writing a single line. The only genuinely new part was the
    recurrence itself — deciding what to do on a match vs a mismatch.

Problem:
    Given two DNA sequences, find the length of the longest sequence
    of characters that appears in both, in the same relative order,
    but not necessarily contiguously (i.e. a subsequence, not a
    substring — gaps between matched characters are allowed).

    Example:
        seq1 = "AGCAT"
        seq2 = "GAC"
        LCS length = 2   (e.g. "GA" or "AC")

Relationship to Edit Distance / Sequence Alignment:
    All three problems share the same DP table shape and the same
    "look at seq1[i-1] vs seq2[j-1]" comparison at each cell. The
    difference is in the recurrence's objective and choices:
        - Edit Distance: MIN over substitute/insert/delete
        - Sequence Alignment: MAX over match/gap-in-seq1/gap-in-seq2
        - LCS: on a match, extend the diagonal by 1; on a mismatch,
          take the best of skipping a character from either sequence
    LCS has no "gap penalty" concept — mismatches simply don't extend
    the count, they just fall back to the best subproblem already
    computed.

DP table definition:
    dp[i][j] = length of the longest common subsequence between
               seq1[0..i) and seq2[0..j)

Recurrence:
    dp[i][j] = dp[i-1][j-1] + 1                  if seq1[i-1] == seq2[j-1]
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])       otherwise

Base cases:
    dp[i][0] = 0
    dp[0][j] = 0

Biological relevance:
    LCS models similarity that survives insertions/deletions between
    two sequences — useful for detecting a conserved pattern between
    two sequences descended from a common ancestor, even when
    mutations have shifted or removed characters in between.
"""

def longest_common_subsequence(seq1, seq2):
    dp = [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]

    for i in range(0, len(seq1) + 1):
        dp[i][0] = 0
    for j in range(0, len(seq2) + 1):
        dp[0][j] = 0

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(seq1)][len(seq2)]


seq1 = "AGCAT"
seq2 = "GAC"

print(longest_common_subsequence(seq1, seq2))
