#Linked List
"""
Linear Collection of data elements. Order is not given by physical
placement in memory as opposed to arrays. Each element contains an
address of the next element. DS consisting of a collection of nodes 
which together represent a sequence. In most basic form, each node 
contains data, and a reference to the next node
"""

#Advantages
"""
Inserting and deleting a node in a list (given its location) is O(1).
In arrays the following elements will have to be shifted
"""

#Disadvantages
"""
Access time is linear because directly accessing elements by its
position in the list is not possible unlike arrays (indexing). 
You have to traverse from the start
"""

#Types of Linked Lists
"""
Singly linked list
A linked list where each node points to the next node and the last node
points to null

Doubly Linked list
A linked list where each node has two pointers, next which points to the
next node and prev which points to the previos node.

Circular linked list
A singly linked list where the last node points back to the first node. 
There is a cicular doubly linked list variant where the prev pointer
of the first node points to the last node and the next pointer of the last
and the next poniter of the last node points to the first node"""

#Time complexity Operations
"""
Access O(n)
Search O(n)
Insert O(1): Assumes you have traversed to the insertion position
Remove O(1) Assumes you have traversed to the node to be removed
"""

#Common Routines
"""
Be familiar with these routnies because many linked list questions make
use of one or more of these routines in the solution

1. Counting number of nodes in linked list
2. Reversing a linked list in-place
3. Finding the middle node of the linked list using two pointers (fast/slow)
4. Merging two linked lists together
"""
#Corner cases
"""
1. Empty linked list (head is null)
2. Single Node
3. Two node
4. Linked list has cycles Tip: Clarify beforehand with the interviewer whether there can 
be a cycle in the list. Usually the answer is no and you don't have to handle it in the 
code
"""

#Techniques
"""
Adding dummy node at head or tail might help to handle edge cases where operations
have to be performed at the head or tail. Be sure to remove them at the end of operation

Two pointers
-Common for linked list. Approach is used for many classic linked list problems
Getting the kth from the last node - Have two pointers, where one is k nodes
ahead of the other. When the node ahead reaches the end, the other node is k node behind

-Detecting cycles - have two pointers, where one pointer increments twice as much as 
the other, if the two pointers meet, means that there is a cycle

-Getting the middle node: have two pointers where one pointer increments twice as much as
the other. When the faster node reaches the end of the list, the slower will be at the mid
"""
#Using space
"""
Many linked list problems can be easily solved by creating a new linked list and adding 
nodes to the new linked list with the final result. However, this takes up extra space and 
makes the question much less challenging. The interviewer will usually request that you
modify the linked list in-place and the solve the problem without additional storage. 
You can borrow ideas from the Reverse a Linked List problem.
"""

#Elegant modification operations
"""
As mentioned earlier, a linked list's non-sequential nature of memory allows for efficient modification of its contents. 
Unlike arrays where you can only modify the value at a position, for linked lists you can also modify the next pointer 
in addition to the value.

Here are some common operations and how they can be achieved easily:

Truncate a list - Set the next pointer to null at the last element
Swapping values of nodes - Just like arrays, just swap the value of the two nodes, 
there's no need to swap the next pointer
Combining two lists - attach the head of the second list to the tail of the first list"""
