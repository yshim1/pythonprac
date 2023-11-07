"""
Counting sort is an integer sorting algorithm for a collection of objects that sorts according to the keys of the object

Steps:
1. Construct a working array C that has size equal to the range of the input array A.
2. Iterate through A, assigning C[x] based on the number of times x appeared in A.
3. Transform C into an array where C[x] refers to the number of values ≤ x by iterating through the array,
assigning to each C[x] the sum of its prior value and all values in C that come before it.
4. Iterate backwards through A, placing each value in to a new sorted array B at the index recorded in C. This is
done for a given A[x] by assigning B[C[A[x]]] to A[x], and decrementing C[A[x]] in case there were duplicate
values in the original unsorted array.
"""
#Time and space
"""
We only use a count array of length O(k) which is the range of values in the input
Time is O(n + k) because we iterate through the count array as well as the input array at least once
"""
#Other info
"""
Stable algorithm that is a non comparison
"""

def countingSort(A, k): # keys from 0 to k-1
    n = len(A)
    count = [0 for x in range(k)] # count of each element in key
    output = [0 for y in range(n)]
    for key in A:
        count[key] += 1
    for i in range(1, k):
        count[i] += count[i-1] #Transform count array into cumulative array that stores number of values <= x
    for key in reversed(A):
        output[count[key]-1] = key
        count[key] = count[key] - 1
    return output

arr = [2,0,2,1,1,0]
k = 3
print(countingSort(arr, k))

# import random
# arr = countingSort(arr, 5)
# print(arr)


# n = 20
# k = 15
# A = []
# for i in range(0, n):
#     A.append(random.randint(0, k))
# print(A)
# A = countingSort(A, k)
# print(A)






# import random
# A = []
# k = 5
# n = 10
# for i in range(0,n):
#     A.append(random.randint(0,k))
# print(A)
# ANEW = [0] * n
# LOC = [0] * (k+1)
# for i in range(0,n):
#     LOC[A[i]] = LOC[A[i]] + 1
# print('Count array: '+str(LOC))
# for i in range(1,k+1):
#     LOC[i] = LOC[i] + LOC[i-1]
# print('Cumulative count array: '+str(LOC))
# for i in range(n-1,-1,-1):
#     ANEW[LOC[A[i]]-1] = A[i]
#     LOC[A[i]] = LOC[A[i]] - 1
#     print('Positioning A['+str(i)+'] in position '+str(LOC[A[i]]-1))
#     print('Result: '+str(ANEW))
# for i in range(0,n):
#     A[i] = ANEW[i]
# print(A)