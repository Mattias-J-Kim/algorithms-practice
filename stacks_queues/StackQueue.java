/*
Queue Using Two Stacks
=======================

Note:
    A stack reverses order, so passing elements through two stacks
    reverses them twice and restores FIFO order. New elements are
    always pushed onto inStack; removals always pop from outStack.

    The important detail is in transfer(): elements are moved from
    inStack to outStack ONLY when outStack is empty. If outStack still
    held older elements, pushing newer ones on top of them would put
    the newer elements in front and break FIFO order.

    Each element is pushed and popped at most twice in total (once per
    stack), so although a single dequeue can trigger a transfer of up
    to n elements, the cost per operation is O(1) amortized.

    Known edge case: capacity applies to EACH stack, not to the queue.
    enqueue() only fails when inStack is full, so a StackQueue(10) can
    hold up to 19-20 elements if some are already in outStack
    (e.g. enqueue 10, dequeue 1, enqueue 10 -> size 19).

Problem:
    Implement the Queue interface using only two ArrayStacks.

    Example (from main):
        enqueue a..e, dequeue x3, enqueue f..j, dequeue x3,
        enqueue k..o, dequeue x6, then drain the rest
        output: m n o

Complexity:
    Time  O(1) amortized per operation, O(n) worst case for one dequeue/front
    Space O(capacity)
*/

public class StackQueue implements Queue {
    ArrayStack inStack;
    ArrayStack outStack;

    public StackQueue(int capacity) {
        inStack = new ArrayStack(capacity);
        outStack = new ArrayStack(capacity);
    }

    public int size() {
        return inStack.size() + outStack.size();
    }

    public boolean isEmpty() {
        return inStack.isEmpty() && outStack.isEmpty();
    }

    private void transfer() {
        if (outStack.isEmpty()) {
            while (!inStack.isEmpty()) {
                outStack.push(inStack.pop());
            }
        }
    }

    public char front() {
        if (isEmpty())
            throw new EmptyQueueException("Empty queue: cannot front");
        transfer();
        return outStack.top();
    }

    public void enqueue(char o) {
        try {
            inStack.push(o);
        } catch (FullStackException e) {
            throw new FullQueueException("Full queue: cannot enqueue");
        }
    }

    public char dequeue() {
        if (isEmpty())
            throw new EmptyQueueException("Empty queue: cannot dequeue");
        transfer();
        return outStack.pop();
    }

    public static void main(String[] args) {
        StackQueue q = new StackQueue(10);

        for (char c = 'a'; c <= 'e'; c++)
            q.enqueue(c);

        for (int i = 0; i < 3; i++)
            q.dequeue();

        for (char c = 'f'; c <= 'j'; c++)
            q.enqueue(c);

        for (int i = 0; i < 3; i++)
            q.dequeue();

        for (char c = 'k'; c <= 'o'; c++)
            q.enqueue(c);

        for (int i = 0; i < 6; i++)
            q.dequeue();

        while (!q.isEmpty())
            System.out.print(q.dequeue() + " ");
        System.out.println();
    }
}

class EmptyQueueException extends RuntimeException {
    public EmptyQueueException(String msg) {
        super(msg);
    }
}

class FullQueueException extends RuntimeException {
    public FullQueueException(String msg) {
        super(msg);
    }
}
