/*
Binary Sum
===========

Note:
    Linear recursion (sum = A[i] + sum of the rest) reaches a recursion
    depth of n. Splitting the range in half instead keeps the total work
    at O(n), since every element is still visited once, but reduces the
    recursion depth to O(log n).

    The two halves use ceil and floor so that odd lengths are covered
    exactly: the left half gets (n+1)/2 elements and the right half gets
    n/2, and the two always add back up to n.

    Known edge case: the only base case is n == 1, so calling with n == 0
    recurses forever ((0+1)/2 == 0) and ends in StackOverflowError.

Problem:
    Given an array A, return the sum of the n elements starting at
    index i.

    Example:
        A = [1, 2, ..., 100], i = 0, n = 100
        answer = 5050

Recurrence:
    binarySum(A, i, n) = A[i]                                       if n == 1
                       = binarySum(A, i, ceil(n/2))
                         + binarySum(A, i + ceil(n/2), floor(n/2))  otherwise

Complexity:
    Time  O(n)
    Space O(log n)   recursion depth
*/

public class BinarySum {

    public static long binarySum(int[] A, int i, int n) {
        if (n == 1) {
            return A[i];
        } else {
            return binarySum(A, i, (n + 1) / 2) + binarySum(A, i + (n + 1) / 2, n / 2);
        }
    }

    public static void main(String[] args) {
        int[] A = new int[100];
        for (int k = 0; k < 100; k++) {
            A[k] = k + 1;
        }
        System.out.println(binarySum(A, 0, A.length));
    }
}
