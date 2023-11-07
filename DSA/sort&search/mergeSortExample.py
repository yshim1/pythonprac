# def merge (X, Y):
#     # Takes 2 lists as parameters
#     p1, p2 = 0, 0
#     #Two pointers
#     output = []
#     #initialize output variable that we will return
#     while p1 < len(X) and p2 < len(Y):
#         # Loop through both arrays/lists and compare values
#         if X[p1] < Y[p2]:
#             output.append(X[p1])
#             p1 += 1
#         else:
#             output.append(Y[p2])
#             p2 += 1
#     output += X[p1:] or Y[p2:]
#     return output

# def mergeSort(A):
#     #base case is if length of array is 1 or 0 cause there is nothing to sort
#     if len(A) <= 1:
#         return A
#     # break down array repeatedly by using midpoint
#     mid  = len(A)//2
#     return merge(mergeSort(A[:mid]), mergeSort(A[mid:]))

from mergesort import mergeSort

import random
l1 = [random.randint(0, 100) for x in range(20)]
print('This is original list')
print(l1)
print('This is sorted list')
print(mergeSort(l1))