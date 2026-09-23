/*
Stack (ADT)
============

Interface for a LIFO stack of chars. Implemented by ArrayStack.

Operations:
    size()     number of stored elements
    isEmpty()  true if size() == 0
    top()      return the most recently pushed element without removing it
    push(o)    insert o on top; returns o
    pop()      remove and return the top element
*/

public interface Stack {
    public int size();
    public boolean isEmpty();
    public char top();
    public char push(char o);
    public char pop();
}
