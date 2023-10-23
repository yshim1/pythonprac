def power(n, pow):
    if pow == 0:
        return 1
    if pow == 1:
        return n
    return n * power(n, pow - 1)

print(power(2, 3))
print(power(10, 4))
