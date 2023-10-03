#Using Node class, we can build a linked list
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Create your LinkedList class below:
class LinkedList:
  def __init__(self, value=None):   #instantiate linkedlist with head node as new node containing value
    self.head_node = Node(value)
    
  def get_head_node(self):      #head node method that helps us peek at the first node in the list
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
  
  def stringify_list(self):
    s = ""
    curr = self.get_head_node()
    while curr:
      s += str(curr.get_value())
      s += '\n'
      curr = curr.get_next_node()
    return s
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:	#while current node exists
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None		#Breaks the loop, 
        else:
          current_node = next_node

#A linkedlist is terminated by a node with a pointer to none

#Swapping nodes
"""
node1: the node that matches val1
node1_prev: node1‘s previous node
node2: the node that matches val2
node2_prev: node2‘s previous node
Given an input of a linked list, val1, and val2, the general steps for doing so is as follows:

1.Iterate through the list looking for the node that matches val1 to be swapped (node1), keeping track of the node’s previous node as you iterate (node1_prev)
2.Repeat step 1 looking for the node that matches val2 (giving you node2 and node2_prev)
3.If node1_prev is None, node1 was the head of the list, so set the list’s head to node2
4.Otherwise, set node1_prev‘s next node to node2
5.If node2_prev is None, set the list’s head to node1
6.Otherwise, set node2_prev‘s next node to node1
7.Set node1‘s next node to node2‘s next node
8.Set node2‘s next node to node1‘s next node
"""

"""
get(i): O(1)
search(v): best case O(1), worst case O(n)
insert(i, v): best case O(1) where no shifting is required, worst case O(n)
remove: best case O(1) where no shifting is required, worst case O(n)
"""