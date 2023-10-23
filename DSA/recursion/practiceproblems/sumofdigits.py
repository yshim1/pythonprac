def sumOfDigits(n):
    if n == 0:
        return 0
    return int(n % 10) + sumOfDigits(int(n / 10))

print(sumOfDigits(142))
print(142 % 10)
print(2 % 10)