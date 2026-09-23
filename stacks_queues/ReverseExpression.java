/*
Reverse Expression
===================

Note:
    Pushing every character and then popping them all yields the
    string in reverse order, since a stack is LIFO.

    Reversing alone turns "(a+b)" into ")b+a(", which is no longer a
    valid expression. Each parenthesis is therefore swapped as it is
    popped, so the result stays well-formed: "(a+b)*c" -> "c*(b+a)".

    The stack is sized to the input length, so it can never overflow.

Problem:
    Read an expression from standard input and print it reversed,
    with parentheses kept balanced.

    Example:
        Input:  (a+b)*c
        Output: c*(b+a)

Complexity:
    Time  O(n)
    Space O(n)
*/

import java.util.Scanner;

public class ReverseExpression {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Input: ");
        String input = sc.nextLine();

        ArrayStack st = new ArrayStack(input.length());

        for (int i = 0; i < input.length(); i++) {
            st.push(input.charAt(i));
        }

        System.out.print("Output: ");
        while (!st.isEmpty()) {
            char c = st.pop();
            if (c == '(') {
                c = ')';
            } else if (c == ')') {
                c = '(';
            }
            System.out.print(c);
        }
        System.out.println();
    }
}
