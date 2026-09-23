/*
Array Stack
============

Note:
    A fixed-capacity array plus a single index, top, pointing at the
    most recent element. top starts at -1 so that size() is simply
    top + 1 and the empty check is top < 0; no separate counter is
    needed.

    pop() does not clear the vacated slot; the old value stays in the
    array and is overwritten by the next push. For a char array this
    is harmless (nothing to garbage-collect).

    Underflow and overflow are reported with unchecked exceptions
    (EmptyStackException, FullStackException, defined below) rather
    than returning a sentinel char, since every char value is a valid
    element.

Problem:
    Implement the Stack interface on a char array of given capacity.

    Example:
        push a, b, c -> size 3, top c
        pop x3       -> c, b, a
        isEmpty      -> true

Complexity:
    Time  O(1) per operation
    Space O(capacity)
*/

public class ArrayStack implements Stack {
    private char[] S;

    private int top = -1;

    public ArrayStack(int capacity) {
        S = new char[capacity];
    }

    public int size() {
        return top + 1;
    }

    public boolean isEmpty() {
        return top < 0;
    }

    public char top() {
        if (isEmpty())
            throw new EmptyStackException("Empty stack: cannot top");
        return S[top];
    }

    public char push(char o) {
        if (size() == S.length)
            throw new FullStackException("Full stack: cannot push");
        top = top + 1;
        S[top] = o;
        return o;
    }

    public char pop() {
        if (isEmpty())
            throw new EmptyStackException("Empty stack: cannot pop");
        char temp = S[top];
        top = top - 1;
        return temp;
    }

    public static void main(String[] args) {
        ArrayStack s = new ArrayStack(10);
        s.push('a');
        s.push('b');
        s.push('c');
        System.out.println("size: " + s.size());         // 3
        System.out.println("top: " + s.top());           // c
        System.out.println("pop: " + s.pop());           // c
        System.out.println("pop: " + s.pop());           // b
        System.out.println("pop: " + s.pop());           // a
        System.out.println("isEmpty: " + s.isEmpty());   // true
    }
}

class EmptyStackException extends RuntimeException {
    public EmptyStackException(String msg) {
        super(msg);
    }
}

class FullStackException extends RuntimeException {
    public FullStackException(String msg) {
        super(msg);
    }
}
