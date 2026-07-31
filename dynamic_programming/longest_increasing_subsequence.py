"""
Longest Increasing Subsequence (LIS)
=======================================

Learning note:
    Solved with much less guidance than earlier DP problems in this repo —
    derived the recurrence and the "take max over all valid j < i" idea
    largely on my own after working through Knapsack and Coin Change.
    (Those two were earlier exercises and are not included in this
    repository; they are referenced below only as points of contrast.)

    What I actually learned:
    - dp[i] does NOT mean "LIS length using the first i elements" the way
      Knapsack's dp[i] meant "using the first i items". Instead it means
      "the LIS length that ENDS exactly at index i". This distinction is
      why the final answer is max(dp), not dp[-1] — the longest subsequence
      doesn't have to end at the last element of the array.
    - The recurrence only needs ONE previous value (best dp[j] among valid
      j < i), unlike 2D problems (Knapsack, LCS) that compare two axes.

Problem:
    Given an integer array, find the length of the longest strictly
    increasing subsequence (order preserved, elements need not be
    contiguous).

    Example:
        arr = [10, 9, 2, 5, 3, 7, 101, 18]
        answer = 4   (e.g. 2, 3, 7, 101)

DP table definition:
    dp[i] = length of the longest increasing subsequence that ENDS at
            index i (arr[i] is the last element of that subsequence)

Recurrence:
    dp[i] = max(dp[i], dp[j] + 1)  for every j < i where arr[j] < arr[i]
    dp[i] starts at 1 (the element by itself is a valid subsequence)

Final answer:
    max(dp) over the whole array — NOT dp[last index], since the longest
    increasing subsequence can end anywhere in the array.
"""


def longest_increasing_subsequence(arr: list[int]) -> int:
    dp = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence(arr))
