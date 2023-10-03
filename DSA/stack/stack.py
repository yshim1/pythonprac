#Stack

"""
A stack is a DS which contains an ordered set of data. Stacks provide three methods of interaction

Push: adds data to top of the stack
Pop: returns and removes data from top of the stack
Peek: returns data from the top of the stack without removing it

Think of it as a stack of weights, each plate has a weight(data). The first plate you push on the floor is both the bottom and top
Each weight added becomes the top of the stack

Last in, First Out or LIFO stucture

Stacks can be implemented using a linked list as the underlying data structure because it is more efficient than a list or array
"""

"""
Depending on the implementation, the top of the stack is equivalent to the head node of a linked list and the bottom of the stack
is equivalent to the tail node.

A constraint that may be palced on a stack is its size. This is done to limit and quantify the resources the data structure will
take up when it is full

Attempting to push data onto an already full stack will result in a stack overflow. Similarly, if you attempt to pop data from an
empty stack, it will result in a stack underflow

YOU CANNOT TRAVERSE STACK'S NODES

Stacks are an important way of supporting nested or recursive function calls and is used to implement a depth-first search.
Depth-first search can be implemented using recursion or a manual stack
"""

#Time complexity
"""
Peek: O(1)
Push: O(1)
Pop: O(1)
isEmpty: O(1)
Search: O(n)
"""

#Corner Cases
"""
Empty stack: popping from an empty stack
Stack with one item
Stack with two items
"""