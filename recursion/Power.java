/*
Power (Repeated Squaring)
==========================

Note:
    The naive version, x^n = x * x^(n-1), makes n recursive calls. This
    version halves n on every call instead, so only O(log n) calls are
    made. The odd case is the only non-obvious part: (n-1)/2 is used so
    that the remaining single factor of x is multiplied back in once,
    after squaring.

    The result is a 64-bit long and overflows silently once x^n exceeds
    Long.MAX_VALUE (5^27 still fits, 5^28 does not).

Problem:
    Compute x^n for an integer x and a non-negative integer n.

    Example:
        power(5, 16) = 152587890625

Recurrence:
    power(x, n) = 1                              if n == 0
                = x * power(x, (n-1)/2)^2        if n is odd
                = power(x, n/2)^2                if n is even

Recursion trace of power(5, 16):
    power(5,16) -> power(5,8) -> power(5,4) -> power(5,2) -> power(5,1) -> power(5,0)
    returns:        1  ->  5*1*1 = 5  ->  5*5 = 25  ->  25*25 = 625
                    ->  625*625 = 390625  ->  390625*390625 = 152587890625

Complexity:
    Time  O(log n)
    Space O(log n)   recursion depth
*/

public class Power {

    public static long power(int x, int n) {
        if (n == 0) {
            return 1;
        }
        if (n % 2 != 0) {
            long y = power(x, (n - 1) / 2);
            return x * y * y;
        } else {
            long y = power(x, n / 2);
            return y * y;
        }
    }

    public static void main(String[] args) {
        int x = 5;
        int n = 16;
        System.out.println(power(x, n));
    }
}
