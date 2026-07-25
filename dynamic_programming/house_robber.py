"""
House Robber
=============

Learning note:
    First draft of this problem tried to look 3 steps back (dp[i-3]) and
    hard-coded dp[2] as "always rob house 0 and house 2" instead of
    comparing against skipping. Fixing it required going back to the
    actual rule of the problem (skip only directly adjacent houses) and
    re-deriving the recurrence from that, rather than pattern-matching
    off of Knapsack/Coin Change's two-branch structure.

    What I actually learned:
    - dp[i] means "the max amount obtainable considering houses 0..i" —
      it does NOT mean "house i is definitely robbed". That's why dp[1]
      must be max(houses[0], houses[1]), not just houses[1]: house 0
      might be worth more.
    - Only two candidates ever need to be compared: rob house i (add to
      dp[i-2]) or don't rob house i (carry over dp[i-1]). No need to look
      further back than i-2.

Problem:
    Given the amount of money in each house along a street, find the
    maximum amount that can be robbed without robbing two directly
    adjacent houses.

    Example:
        houses = [2, 7, 9, 3, 1]
        answer = 12   (houses[0] + houses[2] + houses[4] = 2 + 9 + 1)

DP table definition:
    dp[i] = max amount obtainable considering only houses[0..i]

Recurrence:
    dp[i] = max(dp[i-2] + houses[i], dp[i-1])
                    ^rob house i        ^skip house i
    Base cases:
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])
"""


def house_robber(houses: list[int]) -> int:
    dp = [0] * len(houses)
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        dp[i] = max(dp[i - 2] + houses[i], dp[i - 1])

    return dp[len(houses) - 1]


houses = [2, 7, 9, 3, 1]
print(house_robber(houses))
