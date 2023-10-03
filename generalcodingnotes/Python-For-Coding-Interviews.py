#Python is Dynamically type

n = 0
print ('n = ', n)
n = "abc"
print('n =', n)
#Variables types are determined at runtime

#Multiple Assignments
n, m = 0, "abc"

#Incrementing
n = n+1
n +=1
#cant do n++

#None is Null

#If statements dont require parentheses or curly braces
n = 1
if n >2:
    n -= 1
elif n == 2:
    print(n)

#Parentheses needed for multi-line conditions.
#No such thing as &&, ||
n, m = 1, 2
if ((n>2 and 
      n !=m) or n == m):
    n += 1

#For loops. Looping from i = 0 to i = 4
for i in range(5):
    print(i)
#i is incremented implicitly

#Looping from 2 to 5:
for i in range (2,6):
    print(i)

#Looping from 5 to 2 backwards. The last number is decrement
for i in range (5, 1, -1):
    print(i)

#Division is decimal by default
print(5/2)
#returns 2.5

#Double slash rounds down. Most languages round towards 0
print(5//2)
#returns 2

#negative numbers will round down
print(-3//2)

#A workaround for rounding towards zero is to use decimal devision adn then convert to int
print((int(-3//2)))


#modding is similar to most languages except for negative values
print(-10 % 3)
#returns 2

import math
from re import M
print(math.fmod(-10, 3))
"""python returns a number having the same sign as the denominator. Python applies the """
#returns -1

#math helpers
print(math.floor(3/2)) #rounds down
print(math.ceil(3/2)) #rounds up
print(math.sqrt(2)) 
print(math.pow(2,3)) #2 to the power of 3


#Max / Min Int
float("inf")
float("-inf")
#Python numbers are infinite so they never overflow

print(math.pow(2,200)) #returns 1.6e+60
#Still less than float("inf")

#Arrays (called lists in python) Most common next to hashmaps
arr = [1,2,3]

#Can be used as a stack
arr.append(4) #adds 4 to end
arr.pop()
arr.insert(1,7) #inserts it at index 1
#Inserting is a big O(n) operation

#These are constant time operations
arr[0] = 0
arr[3] = 0

#initialize arr of size n with default value of 1
n = 5 
arr = [1] * n

#This will read the last value
arr[-1]

#Sublists (aka slicing) This will prnit index 1 to index 3 but not including it [2,3]
arr = [1,2,3,4]
print(arr[1:3])

#unpacking
a,b,c = [1,2,3]
#will assign a to 1, b to 2, etc.
#Number of variables on left has to match right

#looping through arrays
#Using index
nums = [1,2,3] 
for i in range (len(nums)):
    print(nums[i])
#Without index
for n in nums:
    print(n)
#With index and value
for i, n in enumerate(nums):
    print(i,n)
#i is the index and n is the number

#Loop through multiple arrays simultaneously with unpacking
nums1 = [1,3,5]
nums2 = [2,4,6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
    #Takes both arrays and combines them into pairs

#Reverse
nums = [1,2,3]
nums.reverse() #Just reverses the order
    
#Sorting
arr = [5,4,7,3,8]
arr.sort()
print(arr)

arr.sort(reverse = True)
print(arr)

#If sorting string array, then it will sort by alphabetical order

#Custom sort (by length of string)
arr.sort(key=lambda x: len(x))
#lambda is a nameless function
#x is the each value in array, len(x) is the key used to sort

#List comprehension
arr = [i for i in range(5)] #iterating for i in range(5). Adding the first i value to array
arr = [i+i for i in range(5)]

#2-D lists
arr = [[0] * 4 for i in range(4)]

#This won't work
arr = [0 * 4] * 4
print(arr)

#Strings are immutable but similar to arrays
s = "abc"
s+= "def" #creates a new string, this is an n time operation. Becomes "abcdef"

#Valid numeric strings can be converted
print(int("123") + int("123")) #returns 246
#Numbers can be converted to strings
print(str(123) + str(123)) #returns 123123

print(ord("a")) #returns the ASCII value of a char

#Combine a list of strings(with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))
 
#Queues (double ended queue by default)
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft() #Removes the first element
print(queue)

queue.appendleft(1) #Adds back to beginning of queue
print(queue)

#Hashset
#Can be searched in constant time and insert in constant time
#No duplicates in a set
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

print(1 in mySet) #searches for certain element in set without having to build function
#Removal is in constant time
mySet.remove(2)

#converting list to set
print(set([1,2,3]))

#set comprehension
mySet = {i for i in range(5)} #Going through every value in the range of i 
#and taking that value and adding it to set. Manually initializes via loop

#HashMap (aka dict) *Likely to be single most common data structure used*
#Cannot have duplicate keys
myMap = {}
myMap["alice"] = 88
print(len(myMap)) #returns the number of keys that exist in the hashmap

myMap["alice"] = 80 #alters value at key
print("alice" in myMap) #can check if key exists in hashmap (constant time)
myMap.pop("alice") #removes value

myMap = {"alice":90, "bob": 70}

#Dict comprehension
myMap = {i : 2*i for i in range (3)}

#Looping through map
myMap = {"alice" : 90, "bob": 70}
for key in myMap: #iterating through keys
    print(key, myMap[key])

for val in myMap.values(): #iterating through values
    print(val)

for key, val in myMap.items(): #unpacking
    print(key,val)
    
#tuples are like arrays but immutable
tup = (1,2,3)
print(tup[1])
print(tup[-1]) #indexable but cant modify

#Mainly use tuples as key for hash map/set
myMap = {(1,2):3}
#Can also be done with sets
mySet = set()
mySet.add((1,2)) #tuples are used to search the set
print((1,2) in mySet)

#Lists cannot be keys for hashset/map because they are not hashable (because mutable)

#Heaps
import heapq
#Under the hood are arrays
#Good for finding min and max for a set of values

minHeap = [] #initialized like an array/list
heapq.heappush(minHeap, 3)
#by default heaps are min heaps
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

#minimum value is always at index 0

while len(minHeap):
    print(heapq.heappop(minHeap))
    
#No max heaps by default, work around, work around
#is to use min heap and multiple by -1 when push/pop
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

#Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))
    
#Build heap from initial values
arr = [1,2,3,4,5]
heapq.heapify(arr) #Done in linear time
while arr:
    print(heapq.heappop(arr))
    
#functions
def myFunc(n,m):
    return n * M

#Nested functions have access to outer variables *useful in recursion*
def outer(a, b):
    c = 'c'
    
    def inner():
        return a + b + c
    return inner()

#Can modify objects but not reassign unless using non local keyword
def double(arr, val):
    def helper():
        #Modifying array works
        for i , n in enumerate(arr):
            arr[i] *= 2
        #Will only modify val in the helper scope
        #val *= 2
        
        #this will modify val outside helper scope
        nonlocal val
        val *= 2
        
    helper()
    print(arr, val)
    nums = [1,2]
    val = 3
    double(nums, val)
    
        
#Class
class MyClass:
    #constructor
    def __init__(self, nums): #self passed into every method of a class
        #Create member variables
        self.nums = nums #self.nums is member variable
        self.size = len(nums)
        
    #self keyword always passed. give access to member variable. 
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength()