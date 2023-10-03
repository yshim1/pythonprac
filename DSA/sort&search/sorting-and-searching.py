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
Quicksort: O(nlog(n)) time, O(log(n)) space
Mergesort: O(nlog(n)) time, O(n) space
Heapsort: O(nlog(n)) time, O(1) space
Couting sort: O(n+k) time, O(k) space
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
