#LinkedList vs lists
"""
LinkedLists do not have indexes like lists
LinkedLists are not contiguous in memory like lists

LinkedLists have a variable called head that points to the first element in a list and a tail variable that points to the last node of a list
Each Node has a pointer to the next node
"""

#Big O
"""
Append (to end): If we have a pointer to the last node of the list, then appending is O(1). This means we assume that we have traversed already
The last node points to the inserted node, and the tail pointer will point to the last node

Remove (from end): tail pointer has to move to previous node but that is not easy cause we cannot traverse backwards. We must mov
head node until we get to desired node and set tail to prev. O(1)

Append (to front): set new node pointer to current head node. Change head pointer to inserted node. O(1)

Remove (from front): move head pointer to next node and orphan prev node. O(1)

Insert (in middle): requires iteration through list to insert at desired spot. O(n)

Remove (from middle): requires iteration and adjustment of pointers to orphan desired node O(n)

Search: in worst case, requires traversal of head node through list. O(n)
"""

#Under the hood
"""
A node is made of a value and pointer. A node can be thought of as a dictionary
"""

head = {'value': 11,
        'next':{
            'value': 3,
            'next':{
                'value':5,
                'next': None
                }
            }
        }

# print(head['next']['next']['value']) #prints 5

#LinkedList class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value): #Notice how all the methods that take a value will also create a Node with that value
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:   #checks if list is empty
            self.head = new_node #head and tail point to new node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            print('can\'t pop')
        elif self.head is self.tail:
            self.head = None
        else:
            # temp = self.head
            # while temp.next != self.tail:
            #     temp = temp.next
            # self.tail = temp
            # temp.next = None
            
            #Another way of doing this method is
            pre = self.head
            temp = pre.next
            while temp.next:
                temp = temp.next
                pre = pre.next
            self.tail = pre
            pre.next = None
            self.length -= 1
        return temp #returns node object
    
    def popfirst(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return temp
        else:
            return None
    def get(self, index):
        count = 0
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        while count != index:
            temp = temp.next
            count += 1
        return temp
    
    def set(self, index, value):
        temp = self.get(index) #gets value at said index
        if temp: #checks if temp is not none
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value) #return statement terminates program
        elif index == self.length:
            return self.append(value)
        count = 0
        temp = self.head
        prev = Node(None)
        prev.next = temp
        inserted_node = Node(value)
        while count != index:
            temp = temp.next
            prev = prev.next
            count += 1
        prev.next = inserted_node
        inserted_node.next = temp
        self.length += 1
        # temp = self.get(index - 1)
        # inserted_node.next = temp.next
        # temp.next = inserted_node
        # self.length += 1
        return True
    
    def remove(self, index):
        if index == self.length:
            return self.pop()
        elif index == 0:
            return self.popfirst()
        elif index > self.length:
            return None
        count = 0
        temp = self.head
        prev = Node(None)
        prev.next = temp
        while count != index:
            temp = temp.next
            prev = prev.next
            count += 1
        prev.next = temp.next
    
    def reverse(self): #incomplete method
        if self.head is None:
            return None
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
            
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(5)
my_linked_list.append(9)
my_linked_list.append(7)
# my_linked_list.print_list()
# print(my_linked_list.pop())
my_linked_list.prepend(10)
# my_linked_list.print_list()
my_linked_list.popfirst()
my_linked_list.print_list()

# new_list = LinkedList(4)
# print('\n')
# print(new_list.popfirst())
# print(new_list.popfirst())
# new_list.print_list()

print('\n')

print(my_linked_list.get(2))
print(my_linked_list.get(0))
print(my_linked_list.get(8))
print(my_linked_list.get(-2))

print('\n')

my_linked_list.set(2, 100)
my_linked_list.set(6, 2000)
my_linked_list.print_list()
# new_list = LinkedList(4)
# print(new_list.get(0))

# my_linked_list.insert(0, -7)
print('\n')
my_linked_list.print_list()
# my_linked_list.remove(2)
# my_linked_list.remove(0)
# my_linked_list.remove(10)
# my_linked_list.remove(my_linked_list.length)
print('\n')

new_list = LinkedList(4)
new_list.append(3)
new_list.append(100)
new_list.append(8)
new_list.append(7)
new_list.append(90)
new_list.print_list()

new_list.remove(2)
print('\n')
new_list.print_list()

