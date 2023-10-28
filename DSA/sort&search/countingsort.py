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

def countingSort(A, k): # keys from 0 to k-1
    n = len(A)
    count = [0 for x in range(k)] # count of each element in key
    output = [0 for y in range(n)]
    for key in A:
        count[key] += 1
    for i in range(1, k):
        count[i] += count[i-1]
    for key in reversed(A):
        output[count[key]-1] = key
        count[key] = count[key] - 1
    return output

arr = [3,1,4,0,0,3]

import random
arr = countingSort(arr, 5)
print(arr)


n = 20
k = 15
A = []
for i in range(0, n):
    A.append(random.randint(0, k))
print(A)
A = countingSort(A, k)
print(A)
