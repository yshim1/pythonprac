#intro

"""
Sorting is the act of rearranging elements in a sequence in order, either in numerical or lexicographical order, and either ascending or descending

A lot of basic algorithms run in O(n^2), these should not be used in interviews. In algorithm interviews, you're unlikely to need to implement any of the
sorting algorithms from scratch. Instead you would need to sort the input using your language's default sorting function so that you can use binary searches.

On a sorted array of elements, by leveraging on its sorted property, you can binary search.

"""
#Side note
#In python, the default sorting algorithm is called timsort
"""
Worst-case performance: O(nlogn)
Best-case performance: O(n)
Average performance: O(nlogn)
Worst-case space complexity: O(n)
"""
#Time Complexity
"""
Bubble Sort: O(n^2) Time, O(1) space
Insertion Sort: O(n^2) Time, O(1) space
Selection Sort: O(n^2) Time, O(1) space
Quicksort: O(nlog(n)) time (worst case is n^2), O(log(n)) space, inplace sort, unstable sort
Mergesort: O(nlog(n)) time, O(n) space

Heapsort: O(nlog(n)) time, O(1) space, inplace sort, unstable sort

Couting sort: O(n+k) time, O(k) space, assumes keys are integers in a fixed range, not comparison sort, stable sort
For n items with integer keys in range of 0 to k-1

Radix sort: O(nk) time, O(n+k) space"""
#Corner case
"""
Empty sequence
Sequence with one elemtn
Sequence with two elements
Sequence containing duplicate elements.
"""

#Techinques
"""
Sorted inputs: When a sequence is in sorted order, binary search should be one of the first things in your mind
Sorting an input that has limited range: Couting sort is a non comparison based sort you can use on number where you
know the range of values before hand.
"""

#Classifications of Sorting Algorithms
"""
There are many ways to classigy a sorting algorithm
-time complexity
-space complexity: amount of memory algo needs to sort its input
    an inplace algo operates directly on input and changes it. Generally O(1)
    out of place algo copies input and makes sorting changes on copied version
    
-stability: stable algos preserve the relative order of elements when faced with an equal key (on the property by which the
dataset is being sortd). In unstable algos, if two items are the same value, there is no guarantee that the relative order of elements
will be the same order as before


-internal vs external:
    if all the items that need to be sorted are in the main memory/RAM, the algo is an internal sort
    if the records to be sorted cannot be stored in main mem and the sorted data occurs outside of the main memory, such as on disk
    the algo is external sort
    
-recursive vs nonrecursive: some algos do their sorting by divide and conquer. Its worth noting that most algos dont have
to be implemented recursively

comparison vs non comparison sort: any algo that compares two items or a pair at a time in the process of sorting through
a larger dataset is referred to as a comparison sort. The subset of algorithms use some type of comparator to determine
which of any two elements should be sorted first.
"""