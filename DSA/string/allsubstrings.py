word = 'kira'


def allsubs(string):
    l, r = 0, 0
    res = []
    while l < len(string):
        for i in range(len(string) - 1, -1, -1):
            if  string[l:i+1] != '':
                res.append(string[l:i+1])
        l+=1
    return res

print(allsubs(word))