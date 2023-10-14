#Intro
"""Arrays hold values of the same data type at adjacent memory locations. In python, an 
array is known as a list. Also, in python, size is dynamic meaning you do not need to 
have a size defined beforehand when creating an array.
"""

#Advantages
"""
-Store multiple elements of the same type with one single variable name
-Accessing elements is fast as long as you have the index, as opposed to linked lists
where you have to traverse from head.
"""

#Disadvantages
"""
-Addition and removal of elements into/from the middle of an array is slow because 
remaining elements need to be shifted to accomadate new/misssing element. NOT THE SAME AS
REMOVING FROM END OF ARRAY.
-For certain languages where array size is fixed, it cannot alter its size after initial-
ization. If an insertion causes the total number of elements to exceed the size, a new
array has to be allocated and the existing elements have to be copied over. The act of 
creating a new array and transferring elements over takes O(n) time.
"""

#Common Terms

#-Subarray: a range of contiguous values within an array. Example
arr = [2,3,6,1,5,4] 
subarr = [3,6,1]

#Subsequence: a sequence that can be derived from array by deleting some or no elements
# without changing the order of remaining elements
arr2 = [2,3,6,1,5,4]
subseq = [3,2,5]

#Time Complexity
"""
Access: O(1). Given an index, there is no need to search through array
Search: O(n). Might need to traverse entire array
Search (Sorted Array): O(log(n)). Binary search, starting at middle element.
Insert: O(n). Requires shifting all subsequent elements to right by one which takes O(n)
Insert at end: O(1). Special case of insertion where no other element needs to be shifted (amortized aka on average)
Remove: O(n). Removal would require shifting all subsequent elements to the left by one
which takes O(n)
Copy O(n) time and space: traverse and create new
Remove at end: O(1). Special case of removal where no other element needs to be shifted
"""

#Things to look out for
"""
-Clarify if there are duplicates in the array. Do duplicates affect the answer? Does it
make the question simpler or harder.
-Usually, slicing and concatenating arrays would take O(n) time. Use start and end indices
to demarcate a subarray/range where possible.
"""

#Corner Cases
"""
-Empty sequence
-Sequence with 1 or 2 elements
-Sequence with repeated elements
-Duplicated values in the sequence
"""

#Techniques
"""
Sliding Window: This technique applies to many subarray/substring problems. In a sliding
window, the two pointers move in same direction and never overtake each other. This ensures
that each value is only visited at most twice. Time complexity is O(n).
https://leetcode.com/problems/minimum-window-substring/solutions/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems/

Two pointers: This techique is a more general version of sliding window where the pointers
can cross each other and can be on different arrays. When you are given 2 arrays to process
it is common to have one index per array (pointer) to traverse/compare the both of them,
incrementing one of the pointers when relevant.

Traversing from the right: this technique is just traversing the array from the right instead
of from conventional left.

Sorting the array:
Is the array sorted or partially sorted? If so, some kind of binary search should be possible.
This means interviewer is looking for a solution that is faster than O(n)
Can you sort the array? Sometimes sorting the array first might simplify the problem. This
would not work if order of array elements need to be preserved.

Precomputation:
For questions where summation or multiplication of subarray is involved, precomputation using
hashing or a prefix/suffix sum/product might be useful

Index as hash key:
If you are given a sequence and the interview asks for O(1) space, it might be possible
to use the arary itself as a hash table. For example, if the arrayy only has values from
1 to N, where N is the length of the array, negate the value at the index (minus one)
to indicate the presence of that number.

Traversing the array more than once:
This might be obvious, but traversing the array twice/thrice (as long as fewer than n times)
is still O(n). Sometimes traversing the array more than once can help you solve the problem
while keeping time complexity to O(n)
"""

import array as myarray
abc = myarray.array('i', [2, 4, 6])
print(abc)