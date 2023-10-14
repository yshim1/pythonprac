"""
O is worst case (upper bound)
Omega is best case (lower bound)
Theta is Average case 
"""
#Big O code
def print_items(n):
    for i in range(n): #prints 0 - 9
        print(i)
print_items(10)

#The number of operations is proportional to data input size

#Dropping constants
def print_items(n):
    for i in range(n): #prints 0 - 9
        print(i)
    for j in range(n):
        print(j)
print_items(10)
#The time xomplexity of this program is technically 2n, but constants are dropped so it is O(n)

#O(n^2)
def print_items(n):
    for i in range(n): 
        for j in range(n):
            print(i, j)     #Essentially prints 0-99 or another way of saying it is it prints 0-9 for 9x times (n * n)
print_items(10)


#Dropping non dominants
def print_items(n):
    for i in range(n): 
        for j in range(n):
            print(i, j)     #Essentially prints 0-99 or another way of saying it is it prints 0-9 for 9x times (n * n)
            
    for k in range(n):
        print(k)
print_items(10)
"""
Output is O(n^2 + n). Imagine n getting larger (i.e. n = 100). Then n^2 = 10,000 and n = 100. The + n is neglible essentially so
O(n^2)
"""

#O(1)
def add_items(n):
    return n + n
#This function is completely independent of input size. The number of operations will be constant as n increases

#O(log(n))
arr = [1,2,3,4,5,6,7,8] #list of 8 elements
"""
if we did a binary search on this list, we would take maximum 3 steps or comparison checks.

The size of the array is 8 but we only do 3 comparisons meaning time complexity is O(log(n))

log2(8) -> divide 8 by 2 and you will get 3

What about a very large size of data?
log2(1,073,741,824) = 31. This is the power of logs
"""

#O(nlogn): This is the most efficient string sort algorithm. Mergesort and Quicksort use these


#Different inputs for n

def print_items(a, b):
    for i in range(a):      #This will be O(a)
        print(i)
    
    for j in range(b):      #This will be O(b)
        print(j)
# The function has a time complexity of O(n + m)

#Time complexity for Lists

li = [1,2,3,4,5,6,7]
li.pop(0) #Remove first element
li.insert(0, 0)
"""
What if we want to remove 7 (end of list) or add at the end of list?
We know it requires no shifting of elements and the array is indexed meaning we can access all elements so it is O(1). This is known as pop

What if we want to remove 1 (beginning of list) or add at the beginning of list?
We know that this will require a shifting of elements from left to right, we cannot simply remove from the front so it is O(n)

What if we want to remove 4 (middle of list) or add to the middle of list?
This will also require O(n) because it will require a shift of elements

What if we want to search for an element?
We know that the worst case is that the element is at the end of the list and the best case is that the element is at the front of the list
so knowing the worst case, we have to traverse the entire list which is O(n)
"""


#As n becomes larger
"""
Assume n = 1000
O(1): 1
O(log(n)) ~= 10        (Divide and conquer)         (good category)
O(n) = 1000             (linear/proportional)       (fair category)
O(n^2) = 1,000,000      (loop within a loop)        

BONUS:
O(nlogn): sort

"""
