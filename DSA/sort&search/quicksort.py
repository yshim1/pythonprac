# Function to find the partition position
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low
 
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
 
    # Swap the pivot element with the greater element specified by i
    (array[i], array[high]) = (array[high], array[i])
 
    # Return the position from where partition is done
    return i
 
# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
 
 
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)

import random
A = []
for i in range(0, 15):
    A.append(random.randint(0, 100))
n = len(A)
print('\n')
print(A)
quickSort(A, 0, n - 1)
print('\n')
print(A)

# def quicksort(A, low, high):
#     if low < high:
#         pivot = hoarePartition(A, low, high)
#         quicksort(A, low, pivot)#left subarray
#         quicksort(A, pivot + 1, high)#right subarray

# def lomutoPartition(A, low, high): #Time complexity of this function is O(n) where n = high - low + 1
#     pivot = high #Pivot becomes index of last value
#     pivot_val = A[pivot]#pivot val becomes last element of subarray
#     i = low
#     for j in range(low, high):
#         if A[j] <= pivot_val:
#             A[i], A[j] = A[j], A[i]
#             i = i + 1
#     A[i], A[pivot] = A[pivot], A[i]
#     return A[i]    

# def hoarePartition(A, low, high): #O(n), fewer swaps than lomuto partition
#     pivot_val = A[low]
#     i = low - 1
#     j = high + 1
#     while True:
#         while True:
#             i == 1
#             if A[i] >= pivot_val:
#                 break
#         while True:
#             if A[j] <= pivot_val:
#                 break
#         if i >= j:
#             return j #new pivot
#         A[i], A[j] = A[j], A[i]
# array = [6,1,5,2,7,4]
# quicksort(array, 0, 5)
# import random
# A = []
# for i in range(0,15):
#     A.append(random.randint(0,100))
# n = len(A)
# print(A)
# def quicksort(l,r,indent):
#     if l<r:
#         resultingpivotindex = partition(l,r,indent+2)
#         quicksort(l,resultingpivotindex-1,indent+2)
#         quicksort(resultingpivotindex+1,r,indent+2)
#         print(indent*'_' + 'Recombine: '+str(A[l:r+1]))

# def partition(l,r,indent):
#     print(indent*'_' + 'Subarray: ' + str(A[l:r+1]))
#     # To use a different pivotvalue
#     # swap it with A[r] here.
#     pivotvalue = A[r]
#     t = l
#     for i in range(l,r):
#         if A[i] <= pivotvalue:
#             # temp = A[t]
#             # A[t] = A[i]
#             # A[i] = temp
#             A[t], A[i] = A[i], A[t]
#             t = t + 1
#     A[t], A[r] = A[r], A[t]
#     print(indent*'_' + 'Pivot around final element.')
#     print(indent*'_' + 'Result: ' + str(A[l:r+1]))
#     return(t)

# quicksort(0,n-1,0)
# print(A)