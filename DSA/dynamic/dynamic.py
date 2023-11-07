#How do we use memoization to change the big O from 2^n to n. Memoization reduces the amount of function calls done by our usual recursion

"""
Below, the return value comes form the memoization array memo[] which is iteratively filled by a for loop. Memoization is essentially
no re-computation which makes for a more efficient algorithm. 
"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) * fibonacci(n-2)

def fibonacciVal(n): 
    memo = [0] * (n+1)  
    memo[0], memo[1] = 0, 1  
    for i in range(2, n+1):    
        memo[i] = memo[i-1] + memo[i-2]  
    return memo[n]