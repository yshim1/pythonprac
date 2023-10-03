#Tree
"""
Hierarchial structure with set of connected nodes. Each node can be connected to many children,
but must be connected to one parent, expect for root

A tree is a undirected and connected acyclic graph. No cycles or loops. Each node
can be like the root node of its own subtree, making recursion a useful technique for tree
traversal

Common Terms
Neighbor - parent or child of a node
Ancestor - a node reachable by traversing its parent chain
Descendant - a node in the node's subtree
Degree - number of children of a node
Distance - number of edges along the shortest path between two nodes
Level/Depth - number of edges along the unique path between a node and the root node
Width - number of nodes in a level
Height - levels counting up from leaf node

Binary Tree terms

Complete binary tree - a binary tree in which every level, except possibly the last, is 
completely filled, and all nodes in the last level are as far left as possible.

Balanced Binary Tree - a binary tree structure in which the left and right subtrees of 
every node differ in height by no more than 1
"""