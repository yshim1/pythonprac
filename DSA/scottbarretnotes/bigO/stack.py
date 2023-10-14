#Implementing stack with LinkedList
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def push(self, value):
        new_node = Node(value) 
        if self.top is None: #Checks if stack is empty
            self.top = new_node     #O(1) because inserting at front of linkedlist is O(1). Requires no shifting
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        
        #Don't forget about stack overflow.
    
    def pop(self):
        #edge case is popping from an empty stack˜
        if self.top:
            removed_node = self.top #pointer to top of stack
            self.top = self.top.next
            removed_node.next = None
            self.height -= 1
            return removed_node
        return None
    
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    

my_stack = Stack(4)
my_stack.print_stack()
print('\n')
my_stack.push(5)
my_stack.print_stack()
print('\n')
my_stack.pop()
my_stack.pop()
my_stack.print_stack()

