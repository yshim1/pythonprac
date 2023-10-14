class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None: #checks if queue is empty
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node #Assuming front of queue is at the head of linkedlist (left)
            self.last = new_node
        self.length += 1
    
    def dequeue(self):  #edge case is popping from empty queue
        if self.first is None:
            return None
        curr = self.first
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            curr.next = None
        self.length -= 1
        
            
        
    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

my_queue = Queue(4)
my_queue.enqueue(5)
my_queue.print_queue()