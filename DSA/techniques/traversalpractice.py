x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
xbackwards = []
for i in range(len(x) - 1, -1, -1):
    xbackwards.append(x[i])
print(xbackwards)