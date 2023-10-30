"""
Merge sort is a divide and conquer algorithm. It divides the input list of length n in half successively until there are
n lists of size 1. Then the pairs of lists are merged together with the smaller element first amoung the pair of lists being
added in each step. Through successive merging and through comparison of first elements, the sorted list is built. 
"""

#Time and Space complexity
"""
The above recurrence can be solved either using recurrence tree method or master method. It falls in case II of master method
and solution of the recurrence is Theta(nlogn). Time complexity of Merge Sort is Theta(nlogn) in all 3 cases (worst, avg, best)
as merge sort always divides the array in 2 halves and takes linear time to merge two halves.

Auxillary Space: O(n)
"""

"""
In typical implementation, the algorithm paradigm is divide and conquer, it is not sorted in place, and it is a stable algorithm
"""

import random
def merge(X, Y): # Takes 2 subarrays
 " merge two sorted lists "
 p1 = p2 = 0
 out = [] #Not sorted in place
 while p1 < len(X) and p2 < len(Y):
     if X[p1] < Y[p2]:
         out.append(X[p1]) # Only append if x is less than Y
         p1 += 1
     else:
         out.append(Y[p2]) # if y is less than or equal to X then append Y
         p2 += 1
 out += X[p1:] or Y[p2:] # Appends remainder which is typically last element(s) leftover when for loop condition exits
 return out

def mergeSort(A):
 if len(A) <= 1: #If array is empty or length1, just return original list
     return A
 #mid = l + (r-1)//2
 mid = len(A)//2
 return merge(mergeSort(A[:mid]), mergeSort(A[mid:])) # returns merged subarrays. Notice mergeSort will call upon further divisions until
# len is 1

# if __name__ == '__main__':
# Generate 20 random numbers and sort them
A = [random.randint(1, 100) for i in range(20)]
print('This is the original random list')
print(A)
print('This is the sorted list')
print(mergeSort(A))

B = [random.randint(0, 100) for x in range(2)]
print('This is the original random list')
print(B)
print('This is the sorted list')
print(mergeSort(B))