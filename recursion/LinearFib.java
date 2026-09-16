/*
Linear Fibonacci
=================

Note:
    The textbook definition F(n) = F(n-1) + F(n-2) translated directly
    into code makes two recursive calls per step, and the same
    subproblems are recomputed exponentially many times. Returning the
    PAIR {F(n), F(n-1)} removes the second call: once F(n-1) and F(n-2)
    come back together, F(n) is a single addition, and F(n-1) is passed
    up as the second element of the new pair.

    This is the same idea as a 1D DP table, but only the last two
    entries are carried, through the return value rather than an array.

    BigInteger is used because F(93) no longer fits in a long.

Problem:
    Compute the n-th Fibonacci number, with F(0) = 0 and F(1) = 1.

    Example:
        F(100) = 354224848179261915075

Recurrence:
    linearFib(n) = {n, 0}                        if n <= 1
                 = {F(n-1) + F(n-2), F(n-1)}     where {F(n-1), F(n-2)} = linearFib(n-1)

Complexity:
    Time  O(n) recursive calls
    Space O(n)   recursion depth; very large n ends in StackOverflowError
*/

import java.math.BigInteger;

public class LinearFib {

    public static BigInteger[] linearFib(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("n must be nonnegative");
        }
        if (n <= 1) {
            return new BigInteger[] { BigInteger.valueOf(n), BigInteger.ZERO };
        } else {
            BigInteger[] pair = linearFib(n - 1);
            BigInteger i = pair[0];
            BigInteger j = pair[1];
            return new BigInteger[] { i.add(j), i };
        }
    }

    public static void main(String[] args) {
        int n = 100;
        for (int k = 1; k <= n; k++) {
            System.out.println("F(" + k + ") = " + linearFib(k)[0]);
        }
    }
}
