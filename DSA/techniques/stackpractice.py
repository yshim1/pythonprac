s = "()[]{}"
cMap = {"(" : ")", "{" : "}". "[" : "]"}
stack = []
for c in s:
    if c in cMap.keys():
        stack.append(c)
    elif c not in cMap.keys() and stack[0] == 