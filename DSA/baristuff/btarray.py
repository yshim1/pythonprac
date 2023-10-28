#Binary Tree representation

"""
The array representation of a binary tree is as so:

If a node is at index i and index are 0-based, 
the left child is at 2i + 1
the right child is at 2i + 2
the parent is at i-1//2
"""
bt1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
bt2 = ['A', 'B', 'C', 'D', 'E']
bt3 = ['A', 'B', 'C', None, None, 'D', 'E']
"""
In bt1, A is the root, B is the left child, C is the right child, D is the left child of B, D is the right child of B...
In bt3, A is the root, B is the left leaf child, C is the right child, and D and E are children of C. Notice how we use None, 
this is because B Node is a leaf
"""

#Full binary tree
"""
A full binary tree is a binary tree in which it has the maximum number of nodes, meaning that each node of the binary tree has 2 nodes.
The maximum number of nodes can be calculated by doing:

2^(h+1) - 1
"""

#Complete binary tree
"""
If you represent a binary tree with an array, then there are no missing elements in between the elements of the array.
The same thing as saying a tree is full up to level h-1 while the last level of elements are filled from left to right
"""