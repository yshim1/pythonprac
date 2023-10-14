#Let's analyze this recursive function

def test(n):
    if n > 0: #Base case
        print(n)
        test(n-1) #Recursive call until base case is false

test(3)
"""
The above code will continue until n == 0. It will print n and call test(n-1). How many times is it printing? 3 times or n times
How many times is it calling test? 4 times or 3 + 1 or n+1 calls

Time function
f(n) = n + 1 or O(n)


Assume that T(n) describes the time function for test(n). What is the T(n) of the entire function? Let's analyze
T(n) = 1 + T(n-1) when n>0, where 1 is the time taken for the print statement and T(n-1) is the time taken for test(n-1)
T(n) = 1 when n == 0

Substitution Method For Solving Recurrence Relation
T(n) = T(n-1) + 1
T(n-1) = T(n-2) + 1

T(n) = (T(n-2) + 1) + 1 or T(n) = T(n-2) + 2

Continue for k times...
T(n) = T(n-k) + k

Assume n-k = 0 therefore n = k
T(n) = T(n-n) + n
T(n) = T(0) + n
T(n) = 1 + n
Theta(n)
"""