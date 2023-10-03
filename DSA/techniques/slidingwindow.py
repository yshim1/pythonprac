# Finding longest increasing subsequence of an array
def slidingWindow(l: list) -> int:
    result, anchor = 0, 0
    for i in range(len(l)): #O(n) loop
        if l[i-1] >= l[i] and i > 0:
            anchor = i
        wlen = i - anchor + 1
        result = max(result, wlen) #wlen is window length
    return result  

def lengthOfLongestSubstring(list):
    anchor, result = 0, 0
    sub = set()
    # for i in range(len(list)):
    for r in range(len(list)):
        while list[i] in sub:
            sub.remove(list[i])
            anchor += 1
        sub.add[list[i]]
        result = max(result,  - anchor + 1)
    return result

l = [1,2,3,2,7]
a = slidingWindow(l)
print(a) 

s = ["dvdf"]
b = lengthOfLongestSubstring(s)
print(b)