"MY IMPLEMENTATION: O(n) time? O(n) space?"

class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {'(':')', '{':'}', '[':']'} #parenthesis map that maps opening to closing
        
        slist = []

        #We know s must start with an opening

        #Different conditions we want to look for...
        #We want to continue if it is a stack of opening parenthesis,
        #if it is not a stack of opening parenthesis, then we want to check if the closing matches the open

        for c in s:
            if c in pmap.keys():    #Add opening bracket to list
                slist.append(c)
            elif c in pmap.values() and len(slist) == 0:
                return False
            else:
                if len(slist) > 0 and c != pmap[slist.pop()]:
                    return False
        return len(slist) == 0 
    
#NEETCODE SOLUTION
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', '}': '{', ']':'['}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:   #basically means it wont match or stack is empty
                    return False 
            else:
                stack.append(c)
        return len(stack) == 0
