/*
Queue (ADT)
============

Interface for a FIFO queue of chars. Implemented by StackQueue.

Operations:
    size()      number of stored elements
    isEmpty()   true if size() == 0
    front()     return the oldest element without removing it
    enqueue(o)  insert o at the rear
    dequeue()   remove and return the front element
*/

public interface Queue {
    public int size();
    public boolean isEmpty();
    public char front();
    public void enqueue(char o);
    public char dequeue();
}
