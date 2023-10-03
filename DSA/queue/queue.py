#Queue
"""
A queue is a data structure which contains an ordered set of data

Three methods for interaction:

Enqueue - adds data to the back or end of queue
Dequeue - provides and removes data form the front or beginning of queue
Peek - reveals data from the front of the queue without removeing it

Mimics physical queue like a line to buy groceries. Each person has a name (the data), the first person to get in line (enqueued) is 
the front and back of the line. As each person enqueues, they become the new back of the line. When a cashier serves someone, they are
dequeued from the front of the line. If they want to know who is next in line, they can peek and get their name without removing them from
the queue.

FIRST IN FIRST OUT (FIFO) structure

Queues can be implemented using a linked list or array as the underlying data structure, the front of the queue is equivalent to
the head node of a linked list and the back of the queue is equivalent to the tail node

Since operations are only allowed to affec the front or back of the queue, any traversal or modification to other
nodes within the lniked list is diallowed. Both ends of the queue must be accessible, a reference to both
the head and tail node must be maintained

One last constraint that might be placed on a queue is its length. 
If a queue has a limit on the amount of data that can be placed into it, it is considered a bounded queue

Like stacks, attempting to enqueue data onto an already full queue will result in queue overflow. IIf you attempt to dequeue data
from an empty queue, it will result in queue underflow
"""

#Time complexity
"""
Enqueue: O(1)
Dequeue: O(1)
Front: O(1)
Back: O(1)
isEmpty: O(1)
"""

#Things to look out for
"""
Most languages don't have a built-in Queue class which can be used. Candidates often use arrays or lists. However, assuming that
the left most value is the head of the queue, the dequeue will take O(n) time because it will require the shifting of all elements
"""

#Corner cases
"""
Empty Queue
Queue with one item
Queue with two items
"""