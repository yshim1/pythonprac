#Intro
"""
A hashtable/hashmap is a ds that implements an associative array abstract data type, 
a structure that can map keys to values. Uses a hash function on the element to
compute an index/hash code into an array of buckets or slots, from which the desired value
can be found. During lookup, the key is hashed and the resulting hash indiciates where
corresponding value is stored.

Common example of space-time tradeoff. Instead of linearly searching an array everytime
to see if element is present (O(n) time), we can traverse the array once and hash all the
elements into a hash table. Determinging if the element is present is a simple matter of
hashing the element and seeing if it exists in the hash table (O(1) on average).

In the case of hash collisions, there are a number of collision resolution techniques that
can be used

-Seperate chaining - A linked list is used for each value, so that it stores all the collided
items.
-Open addressing - All entry records are stored in the bucket array itself. When a 
new entry has to be inserted, the buckets are examined, starting with the hashed-to slot
and proceeding in some probe sequence, until an unoccupied slot is found.
"""
#Time Complexity
"""
Access: N/A, Accessing is not possible as the hash code is not known
Search: O(1)
Insert: O(1)
Remove: O(1)
This is the avg case
"""
#Space complexity 
"O(n)"

#Sample questions
"Describe an implementation of a least-used cache, and big-O notation of it"
"""A question involving an API's integration with hash map where the buckets of hash map
are made up of linked lists"""
import collections