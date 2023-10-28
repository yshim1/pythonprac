#Heap
"""
Max heap is a complete bt in such that the parent node is more or equal than its children. This also means that duplicates are allowed,
root is the max value

Min Heap is a complete bt in such that the parent node is less than or equal to its children. This also means that duplicates are allowed,
root is the min value
"""

#Insert
heap = [50, 30, 20, 15, 10, 8, 16]
heap = [50, 30, 20, 15, 10, 8, 16, 60]
readjustedHeap = [60, 50, 20, 30, 10, 8, 16, 15]

"""
What if we wanted to insert 60 (largest element)? Do we just insert at the root? 

We must add it to the end of the heap because heaps are complete binary trees. This means we must use the first availeble node on 
the last row to make sure we keep this complete binary tree condition. Then what about the condition of it being a MAX heap. We
must readjust the elemtents. We must compare 60 with its parents/ancestors which are 15, 30, and 50. 

What is the time complexity of insertion?
O(log(n)) because we only compare the inserted value to its ancestors which is 3 (its height). We know that the height of a complete binary
tree is log(n) of its total nodes. In the best case, insertion is O(1)
"""

#Deletion
heap = [50, 30, 20, 15, 10, 8, 16]
heap = [16, 30, 20, 15, 10, 8]
readustedHeap = [30, 10, 20, 15, 10, 8]
"""
It is important to note that in a max heap, only the root element can be removed. Imagine it as a stack. 
How do we delete the root while maintaining the conditions of a complete binary tree (all nodes on bottom are filled from left to right
meaning there are no missing elements between elements in an array). This means that the last element must be the root and a readjustment
of the array/heap will be made.

To readjust, we compare 16 (new root) to its children (30 and 20). This causes 30 to become the root, 16 to be a left child, 20 to be
a left child. We then compare 16 (the new left child) to its children to see if we need to readjust further.

Time complexity:
Depends on the height so the maximum is O(log(n))
"""

#HeapSort
"""
Based of our deletion method. Heapsort is an implementation of deletion but instead of completely throwing away the removed max value,
we append it to the end of the heap/array. This will cause all elements to be sorted in ascending order
"""