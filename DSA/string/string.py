#Intro
"""
String: a sequence of characters. Similar to arrays.

Common data structures for looking up strings:
-Trie/Prefix Tree, https://en.wikipedia.org/wiki/Trie
-Suffix Tree, https://en.wikipedia.org/wiki/Suffix_tree

Common String algorithms:
-Rabin Karp: efficient for searching of substring using rolling hash,
https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
-KMP: efficient for searching of substring
https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm

"""

#Time complexity
"""
Access: O(1)
Search: O(n)
Insert: O(n)
Remove: O(n)
"""

#Operations involving another string
"""
-Find substing (length m): O(n * m): most naive case. There are more efficient string searching
algorithms such as KMP
-Concatenating strings: O(n + m)
-Slice O(m)
Split (by token): O(n + m)
Strip (remove leading and trailing white spaces): O(n)
"""

#Corner cases
"""
Empty string
String with 1 or 2 characters
String with repeated characters
String with only distinct characters
"""

#Common Techniques
"""
Counting characters: most common way of doing this is a hashmap. Python does have a 
built in counter class. A common mistake is to say that space complexity for counter
is O(n). A counter for latin characters is O(1) bc upper bound is the range of characters
which is usually fixed constant of 26. If input is just lower case latin.
"""

#String of unique characters:
f = open("/Users/yamlak/Documents/Coding-Notes/leetcodeproblems/DSA_notes/bitmasksample.py", "r")
print(f.read())
"""
To count characters, using a 26-bit bitmask to indicate which lower case latin characters
are in the string
"""

"""
Anagram: An anagram is word switch or word play. It is the result of rearranging the letters
of a word or phrase to produce a new word or phrase, while only using original letters.
In interviews, we are only bothered with words without spaces in them
Some approaches include...
-Sorting both strings: takes O(n * log(n)) time and O(log(n)) space
- Map each character to a prime number and multiply each mapped number together, anagrams
should have same multiple. Takes O(n) time and O(1) space.
-Frequence counting of characters: O(n) time O(1) space"""

"""
Palindrome: a word, phrase, number that reads same backwards as forward
Approaches...
-reverse the string and it should be equal to itself.
-Have two pointers at the start and end of the string. Move pointers inward till they meet
At every point, the characters at both pointers should match
"""

#Extra notes
"""
-Order of characters matters so hash tables are not helpful. 
-When a question is about counting the number of palindromes, a common trick is to
have two pointers that move outward away from the middle.
-Palindromes can be even or odd length. For each middle pivot, you need to check it 
twice -once that includes the character and once without.
-For substrings, you can terminate early when there is no match
-For subsequences, use dynamic programming as there are overlapping subproblems
"""


#Sample Questions
"""Describe an implementation of a least-used cache, and big-O notation of it?
A question involving an API's integration with hash map where the buckets of hash map are made up of linked lists."""
d = dict([('yam', 21), ('yon', 21)])
print(d)