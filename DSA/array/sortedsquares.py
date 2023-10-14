#Question
"""
You are given an array of integers in which each subsequent value is not less than the previous value. Write a function that takes
this array as an input and returns a new array with the squares of each number sorted in ascending order.
"""
#Ask questions about edge cases:

#Are all numbers positive
#Are the integers distinct
#Can an empty array of integers be given as input

"""
Test cases:
[1,3,5] -> [1,9,25]
[]
"""

def sortedSquare(arr):
    #Brute Force: T= O(nlogn), S = O(n)
    # new_array = [0] * len(arr)
    # for i in range(len(arr)):
    #     new_array[i] = arr[i]**2
    # new_array.sort()        #nlogn operation
    # return new_array
    new_array = [0] * len(arr)