arr = [1,2,3,4,5,6,7,8,9]
l = 0
h = len(arr) - 1

#What if we want to find 3
#ITERATIVE METHOD
def binarySearch(arr, target):
    l = 0
    h = len(arr) - 1
    while l <= h: #Edge case is if the element is in the middle of l and h. This means we will have to search once more when l and h are equal
        midpoint = (l+h)//2
        if arr[midpoint] > target:
            h = midpoint - 1
        elif arr[midpoint] < target:
            l = midpoint + 1
        else:
            return midpoint
    return 'Not Found'
        
print(binarySearch(arr, 3))
print(binarySearch(arr, 8))
print(binarySearch(arr, 100)) #Returns NONE
#What if the target is not in the array?

#RECURSIVE METHOD
def binary_search_recursive(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False
    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binary_search_recursive(arr, elem, start, mid-1)
    # elem > arr[mid]
    return binary_search_recursive(arr, elem, mid+1, end)