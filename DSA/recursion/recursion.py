#Recursion

"""Recursion is a method of solving a computational problem where the solution depends on
solutions to smaller instances of the same problem

Two parts to recursive functions
1. A base case (cases) defined, which defines when recursion is stopped
2. Breaking down the problem into smaller subproblems and invoking recursive call
Most common example - Fibonacci sequence

Base case: fib(0) = 0 and fib(1) = 1
Recurrence relation: fib(i) = fib(i-1) + fib(i-2) (where i is the integer)"""

def fib(n):
    if n<= 1:
        return n
    return fib(n-1) + fib(n-2)
"""
Many algorithms relevant to coding interviews make heavy use of recursion 
-binary search, merge sort, tree traversal, depth-first search, etc."""

#Why recursion works
"""
In a recursive algorithm, the computer "remembers" every previous state of the problem.
This information is "held" by the computer on the 'activation stack' (i.e., inside of each
functions workspace). Every function has its own workspace per call of the function."""

"""
Some recursive algorithms are very similar to loops. These algorithms are called "tail
recurisve" because the last statement is to "restart" the algorithm. Tail recursive algorithms
can be directly translated into loops."""

#Things to look out for in interviews
"""
Recursion is useful for permutation, because it generates all combinations and tree-based questions.
You should know how to generate all permutaions of a sequence as well as how to handle duplicates.

Recursion implicityly uses a stack. Hence all recursice approaches can be rewritten iteratively using
a stack. Beware in cases where the recursion level goes too deep and causes a stack overflow (default limit
in python is 1000). You may get bonus points for pointing this out to the interviewer. Recursion will never be
O(1) space complexity because stack is involved unless there is tail-call optimization (TCO) (not supported in python).

Number of base cases: in the fibonacci sequence, one of the recursive calls invoke fib(n-2). This indicates that you
should have 2 base cases defined so that your code covers all possible invocations of the function within the input range.
If your recursice function only invokes fn(n-1), then only one base case is needed. 
"""

#Corner cases
"""
n = 0
n = 1
Make sure you have enough base cases to cover all possible invocations of the recursive function
"""

#techniques
"""
In some cases, you may be computing the result for previously computed inputs. For example, fib(5) calles fib(4)
and fib(3) and fib(4) calls fib(3) and fib(2). fib(3) is called twice! If the value for fin(3) is memoized and used
again, this greatly improves the efficiency of the algorithm and the time complexity becomes O(n)
"""

#Call stacks
#https://www.coursera.org/lecture/programming-languages/tail-recursion-YZic1
"""
While a program runs, there is a call stack of function calls that have started but not yet returned
Calling function f pushes an instance of f on the stack
When a call to f finished, it is popped from the stack

These stack-frams store information like the value of local variables and "what is left to do" in the function
Due to recursion, multiple stack-frames may be calls to the same function
"""