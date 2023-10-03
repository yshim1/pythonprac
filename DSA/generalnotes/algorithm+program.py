#Algorithms vs Programs:

#Both algorithms and programs are step by step prodecures to solve a problem, so what is the difference?

"""
Algorithms are/can:
- created during design phase
- created by a person with domain knowledge
- be made with any language (engish or math)
- Are hardware and software independent
- Are analyzed to see efficacy

Programs are/can:
- created during implementation phase
- created by programmer
- made in programming language
- hardware and software/OS dependednt
- tested to determing efficacy
"""

#Priori Analysis
"""
- Done over the algorithm, studying it over greater detail
- independent of language
- hardware independent
- efficiacy determined by time and space complexity/function
"""

#Posteriori Testing
"""
- done on program
- analyzed over watch time and bytes
"""

#Characteristics of algorithm
"""
- Must take some input, 0 or more input
- Must have some output, at least 1 output
- Definiteness, statements must be clear and understanable
- Finiteness, duration of code must be finite, algorithm cannot run forever. SQL for example runs until user stops it.
- Effectiveness, algorithm must have effective statements. Don't write more than necessary. Think of it like a recipe
"""

#How to write and analyze algorithm
"""
Criteria:
- Time: how much time is the program taking? Is it fast/efficient or slow? For algorithms you will not get runtime, it is time function!
- Space: how much memory is the program taking? Is it low mem?
- Network consumption: how much data will be transferred over networks?
- Power: how much power is it taking?
- CPU registers: how many registers is the algorithm/program using?
"""

#Algorithm Example
def algorithmexample(a, b):
    temp = a
    a = b
    b = temp

"""
Suppose each simple statement takes 1 unit of time to compute, that means the algorithm will take 3 units of time to finish
This means that the time function or f(n) = 3 which is a fixed value. It is constant meaning it is O(1)

Suppose each variable requires 1 unit of space, that means it will take 3 units of space because there are 3 variables used.
This means the space function is s(n) = 3. This is constant meaning it is O(1)
"""

#Frequency count method:

def sum(arr, n): #Where n is the length of the array
    sum = 0 #One unit of time
    for i in range(n):#i<n is executed n+1 times so 
        sum += arr[i]#This statement is executed n times
        i+=1 #This statement is executed n times
    return sum #executes 1 time
#Total time function is f(n) = 2n + 3 meaning O(n)

"""
Space complexity:
arr -> n space because array has n amount of numbers
n -> 1
sum -> 1
i -> 1

so this means s(n) = n + 3 or O(n)
"""
#Matrices add, assume it is a 3x3 matrix
def add(m1, m2, n):
    c = [[]]
    for i in range(n): #This will take n + 1 times
        for j in range(n): #This will be executed n times due to outer for loop but this for loop will take n + 1 times so n(n+1)
            c[i,j] = m1[i,j] + m2[i+j]#This will be executed n x n time

#Total time is f(n) = 2n^2 + 2n + 1 or O(n^2)
"""
Space complexity:
m1 is n^2
m2 is n^2
c is n^2
n is 1 because it is a scalar variable
i is 1
j is 1

Total is S(n) = 3n^2 + 3 or O(n^2)
"""

#Multiplication of matrices
"""
def multiply(m1, m2, n):

for (i = 0; i < n, i++) Loop is done n+1 times
    for(j = 0, j < n; j++) Loop is done n times for n+1 times (outer loop)
        c[i,j] = 0 Loop is done n times (j) for n times (i)
        for(k = 0; k < n; k++) loop is done from k to n times, j to n times, and i to n times
            c[i,j] = c[i,j]+m1[i,k]*m2[i,k] statement is executed from k to n times in j to n times for i to n times

"""

#Example for loop
arr = [1,2,3,4,5,6]
n = len(arr)
for i in range(1, n, 2): #This is still order of n because it is doing n/2 steps. Loop runs from 0 to n/2
    #print(arr[i])
    pass

#Multiplying/dividing step value in iterator
#Also possible to use while loop
def halved_loop(n):
    while n > 1:
        yield n
        n//=2

for i in halved_loop(10):
    print(i)

#Different nested for loop
for i in range(0, n):
    for j in range(0, i): #This loop will continue until j is equal to i, so will execute to i times
        print(i, j) #Statement breaks when j == i
        

#What if we don't know what n is?
"""
for(i = 1; p <= n; i++)     
p+=i 

The loop will continue until p > n meaning the variable i will continue to increment until p > n
p is the summation of variables from i to unknown value we will call k
i is not repeating to n times. It is a number of times we do not know, let it be k
"""
p = 0
i = 1
while p <= n:
    p+=i
    i+=1
    
"""
Loop will execute for k times. When i is k, p will be added by k
Assume that p > n to stop
p = k(k+1)/2
k**2 = n
k is root(n)
O(root(n))
"""

#What if we don't know what n is part 2
i = i
while i < n:
    print(i)
    i*=2
"""
In this case, we know loop will break when i >= n. i will not go for n times because it is being incremented exponentially

i starts at 1, and goes to 2
then 2^2
then 2^3
all the way to 2^k

i = 2^k, so 
2^k >= n when the loop breaks
k is log2n which is O(logn)

For instance, if n = 256, then the algorithm will be 8 steps. 2^8 is 256
"""

#Another way of thinking about this
"""
Another way we can think of this is that we have a problem of size n. For each step of the algorithm, our original problem
becomes half of its previous size (n/2)...n/16....n/k

When the problem space is reduced (solved completely), it cannot be reduced any further (n becomes equal to 1) after exiting
check condition

When the problem-size is done/algorithm is complete, i is 2^k
n = 2^k or 1=n/2^k
k = loge(n)/loge(2) or logn = kloge^2

Using the formula logx(m)/logx(n) = logn(m)...
k = log2(n)
"""

#Similarly, different for loop
i = n
while i >= i:
    i/=2
"""
What if we started at i = n?, in this case, the problem set is still getting halved when the problem size is reduced 
or the algorithm is finished, that means it will be 1 and i will be n/2^k

n = 2^k or 1=n/2^k
k = loge(n)/loge(2) or logn = kloge^2

Using the formula logx(m)/logx(n) = logn(m)...
k = log2(n)
"""

#Complex problem

"""
p = 0
for (i = 1; i < n; i = i * 2):      This loop is executed logn times
    p++                             p = logn

for(j = 1; j < p; j = j * 2)        The middle of the for loop indiciates this loop will go log(p) times, where p is logn
    stmt                            Because p is incremented in the first for loop, the stmt is executed log(log(n))
"""

"""
for(i = 0; i < n; i++)      This loop is done n times
    for(j = 1; j < n; j *= 2)   This loop is done logn times for each n in the first loop so nlogn
        stmt        This statement is done nlogn times
"""


#Complex While Loop
i = 1
k = 1
while k < n:
    #stmt
    k = k+i
    i += 1

"""
We do not know what n is so we do not know how many times this will execute
i = 1, k = 1
i = 2, k = 2
i = 3, k = 4
i = 4, k = 7
i = 5, k = 11
i = m, k = m(m+1)/2

we know it will stop when k >= n, where n can be the problem size for example (arr length)
so, that means m(m+1)/2 >= n, or m(m+1)/2 = n. m^2 = n, 
m = root(n)
"""

#While and if loop
while m!=n:
    if m>n:
        m-=n
    else:
        n-=m
        
"""
Lets iterate through this

m = 6, n = 3 .... m->3, n = 3 .... loop is executed and 1st if is executed
m = 5, n = 6 .... loop will not be executed
m = 16, n = 2 .... m->14, n = 2 .... m->12, n=2 .... m->10, n = 2 .... m->8, n = 2 until m = 2, n = 2
There will be 7 steps which is roughly m/n = 2 or n/2 times
Minimum time is O(1), Max time is O(n)

for(___; m!=n; ___)
"""

#1 < logn < root(n) < n < nlogn < n^2 < n^3< .... 2^n < 3^n < n^n

"""
logn, n, n^2, 2^n
n values
n = 1
0, 1, 1, 2

n = 2
1, 2, 4, 4

n = 4
2, 4, 16, 16

n = 8
3, 8, 64, 256

"""
