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
Leaf- Node with no children
Interior Node- node with children
Level: 1 + num edges between root and node. Root of tree is level one
Height: maximum depth of subtree node and farthest leaf node


Binary Tree terms

Complete binary tree - a binary tree in which every level, except possibly the last, is 
completely filled, and all nodes in the last level are as far left as possible.

Balanced Binary Tree - a binary tree structure in which the left and right subtrees of 
every node differ in height by no more than 1
"""

#Criteria for a tree
"""
1. MUST BE ACYCLIC
2 MUST BE CONNECTED, for any given node in the graph, every node is reachable. All nodes are reachable through one path in the graph
"""

#Binary (Search) tree
"""
Binary tree is a tree that each node in it has a maximum of two children. A binary search tree is a binary tree which its elements positioned in special order
In each BST all values in left sub tree are less than values in right sub tree
"""

#Time complexity of BST
"""
Access: O(log(n))
Search: O(log(n))
Insert: O(log(n))
Remove: O(log(n))
"""

#Note, the space complexity of traversing balenced trees is O(h) where h is the height. Traversing very skewed trees is O(n) because
#it is essentially a linked list


#Traversal
"""
In-order traversal: left -> root -> right

Pre-order traversal: Root -> left -> right

Post-order traversal: left -> right -> root

Note that in-order traversal of a binary tree is insufficient to uniquely serialize a tree. Pre-order or post-order is also required
"""

#Corner cases
"""
Empty tree
Single Node
Two Nodes
Very skewed trees (like a linked list)
"""

#Common routines
"""
Insert value
Delete value
Count number of nodes in a tree
Whether a value is in the tree
Calculate the height of a tree
Binary search tree
    =Determine if it is a bst
    -Get max val
    -Get min val
"""

#Techinques
""""
Recursion is most common approach for traversing trees. When you notice that the subtree problem can be used to solve the entire problem
try recursion. Always remember check for base case, which is usually where the node is null. 
-Sometimes it is possible that your recursive function needs to return 2 values

Traversing by level:
When you are asked to traverse a tree by level, use breath-first search

Summation of nodes:
If the question involves the summation of nodes along the way, be sure to check whether nodes can be negative
"""

#Note
"""
Simplest traversals use dfs
Most common dfs are inorder, preorder, postorder

Inorder: process each node in between visiting left subtree and right subtree
"""

def inordertraverse(u):
    if u:
        inordertraverse(u.left)
        print(u.key)
        inordertraverse(u.right)
        
def preorder(u):
    if u is not None:
        print(u.key)
        preorder(u.left)
        preorder(u.right)

def postorder(u):
    if u is not None:
        postorder(u.left)
        postorder(u.right)
        print(u.key)

#Traversals are O(n)

#min/maximum:
# while u.left:
#     u = u.left
# return u.left

#max
def max(u):
    while u.right:
        u = u.right
    return u

#search
# while u and key != u.key:
#     if key < u.key:
#         u = u.left
#     else:
#         u = u.right
# return u
# Complexity is O(h) where h is tree height

# Inorder predecessor
def predecessor(u):
    if u.left:
        return(u.left)
    else:
        par = u.parent
        while par and u != par.right:
            u = par
            par = par.parent
    return par

#Inorder Predecessor: Element immediately before node in the inorder traversal ordering
def predecessor(u):
    if u.left:
        return max(u.left)
    else:
        par = u.parent
        while par and u!=par.right:
            u = par
            par = par.parent
        return par

#Binary search tree insertion: Time complexity is O(h)
def insert(bst, v): #where v is node
    u = bst.root
    par = None
    while u:
        par = u
        u = u.left if v.key < u.key else u.right
    v.parent = par
    if not par:
        bst.root = v
    elif v.key < par.key:
        par.left = v
    else:
        par.right = v

class Node:
 def __init__(self, val):
    self.l_child = None
    self.r_child = None
    self.data = val

#Insertion method
def insert(root, node):
 if root is None:
    root = node
 else:
    if root.data > node.data:
        if root.l_child is None:
            root.l_child = node
        else:
            insert(root.l_child, node)
    else:
        if root.r_child is None:
            root.r_child = node
        else:
            insert(root.r_child, node)