"""
Useful when the data distribution is known
"""

#Runtime complexity
"""
Avg case: O(n) time complexity, O(n) space complexity
"""

#Steps
"""
1. Scatter: distribute keys to buckets
2. Sort keys within buckets
3. Gather sorted keys (in order)
"""

def bucketSort(A): # All keys fall between [0, 1)
    num_buckets = len(a)
    buckets = [[] for x in range(num_buckets)]
    for key in A:
        buckets[int(num_buckets * key)].append(key)
    for bucket in buckets:
        insertionSort(bucket)
    return [x for bucket in buckets for x in bucket] # Gather step