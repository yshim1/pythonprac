def sumOfList(list):
    if len(list) == 1:
        return list[0]
    return list[0] + sumOfList(list[1:])

list = [2,4,5,6,7]
print(sumOfList(list))