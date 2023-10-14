def test(n): #T(n)
    if n > 0: #1
        i = 0 #1
        while i < n: #n + 1
            print(n) #n
            i+=1     #n
        test(n-1)    #T(n-1)

test(3)

"""
What is the time function?
MUST USE SUBSTITUTION METHOD

T(n) = T(n-1) + 3n + 3 where n > 0 or...

T(n) = T(n-1) + n for n > 0
T(n) = c or 1 where c is a constant for n = 0

T(n-1) = T(n-2) + n - 1 ...substitute this for n > 0

T(n) = T(n-2) + (n-1) + n   #2nd equation after substitution
T(n-2) = T(n-3) + n-2       #Substitute again

T(n) = T(n-3) + (n-2) + (n-1) + n  #3rd equation, now we go to k steps

T(n) = T(n-k) + (n-(k-1)) + (n-(k-2)) + (n-1) + n       4th equation
Assume n-k = 0 therfore n = k

T(n) = T(n-n) + (n-n+1) + (n-n+2) + (n-1) + n
T(n) = T(0) + 1 + 2 + 3 + (n-1) + n
T(n) = 1+ n(n+1)/2
THUS FINALLY
Theta(n^2) is the asymptotic notation
"""