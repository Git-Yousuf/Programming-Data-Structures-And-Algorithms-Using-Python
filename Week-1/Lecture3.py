'''

Algorithm for gcd(m,n)

    To find the largest common factor, start at the end
    and work backwards

    Let i run from min(m,n) to 1

    First common factor that we find will be gcd!

'''

'''

Suppose d divides both m and n, and m > n. If m < n, we can swap them. So we can assume m > n.

gcd(m,n) = d # here d is common divisor

here d divides both m and n without a remainder

gcd(20,12) = 4

20 = 5 * 4
12 = 3 * 4

<!-- m=20, n=12 m-n = 20-12 = 8. Here d divdes m, d divides n, and d divides m-n as well. -->

where  m=20, n=12, d=4, a=5, b=3

so we can write 

m = ad
n = bd

minus m and n, we have

m - n = ad - bd = (a-b)d

substitute values and check

20 - 12 = 5*4 - 3*4 = (5-3)*4 = 2*4
8 = 8 i.e LHS = RHS

Example d=4, a=5, b=3

m-n = (a-b)d = (5-3)*4 = 2*4 = 8

Answer (8) which is derived is also divisible by d=4. so m-n (8) is also divisible by d=4.

hence we can say that if d divides m and n, then d also divides m-n as well.

since conclusion, then gcd(m,n) = gcd(n, m-n). # This is the heart of Euclid's Algorithm.

Consider gcd(m,n) with m>n. if n divides m, return n.

Otherwise, compute gcd(n, m-n) and return that value.

'''

# Euclid’s algorithm

def gcd(m,n):
    # Assume m >= n
    if m < n:
        (m,n) = (n,m)

    if (m%n) == 0:
        return(n)
    else:
        diff = m-n
        # diff > n? Possible!
        print("m=",m,"n=",n,"diff=",diff)
        print(max(n,diff),min(n,diff))
    return(gcd(max(n,diff),min(n,diff)))

print(gcd(20,12))

# Euclid’s algorithm, again - Iteration Version

def gcd(m,n):

    if m < n: # Assume m >= n
        (m,n) = (n,m)

    while (m%n) != 0:
        diff = m-n
        # diff > n? Possible!
        (m,n) = (max(n,diff),min(n,diff))

    return(n)

'''

Even better

    Suppose n does not divide m

    Then m = qn + r, where q is the quotient, r is the
    remainder when we divide m by n

    Assume d divides both m and n

    Then m = ad, n = bd

    So ad = q(bd) + r

    It follows that r = cd, so d divides r as well 

    Ex:

    Subtracting 20-12=8 Why subtract only once? Use remainder directly.

    20÷12 Quotient=1 Remainder=8

    Python 20%12 Output 8, Same answer.

    Example 100 and 30

        Old method

        100-30=70

        Still 70>30 Need another subtraction

        70-30=40

        40-30=10

        Three operations.

    New method

        100%30=10

    Only one operation. Much faster.

New Formula

    Instead of gcd(m,n) -> gcd(n,m-n) Use gcd(m,n) -> gcd(n,m%n)

    This is the real Euclid Algorithm.

'''

'''

Consider gcd(m,n) with m > n

If n divides m, return n

Otherwise, let r = m%n

Return gcd(n,r)

'''

# Euclids algorithm

def gcd(m,n):
    if m < n: # Assume m >= n
        (m,n) = (n,m)

    if (m%n) == 0:
        return(n)
    else:
        return(gcd(n,m%n)) # m%n < n, always!
    
# Euclid’s algorithm, revisited # Iteration Version

    def gcd(m,n):
        if m < n: # Assume m >= n
            (m,n) = (n,m)

        while (m%n) != 0:
            (m,n) = (n,m%n) # m%n < n, always!
    return(n)

'''

Efficiency

    Can show that the second version of Euclid’s
    algorithm takes time proportional to the number of
    digits in m

    If m is 1 billion (109), the naive algorithm takes
    billions of steps, but this algorithm takes tens of
    steps

'''

'''

Summary:

    Naive GCD: Find all common factors → Time Complexity: O(n).

    Euclid (Subtraction): Replace gcd(m,n) with gcd(n, m-n) repeatedly.

    Euclid (Modulo): Replace gcd(m,n) with gcd(n, m % n) repeatedly.

'''