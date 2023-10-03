def reverse(dict):
    newdict = {}
    for key, value in dict.items():
        if value in newdict:
            newdict[value].append(key)
        else:
            newdict[value] = [key]
    return newdict

x = {'apple': 'fruit', 'tulip':'flower', 'banana':'fruit', 'cucumber':'vegetable', 'radish':'vegetable' }

x1 = reverse(x)
print(x1)