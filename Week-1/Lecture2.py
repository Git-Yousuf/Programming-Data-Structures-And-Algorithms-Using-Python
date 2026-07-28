'''
Can we do better?

    We scan from 1 to m to compute fm and again from 1 to n to compute fn. 

    Problem: Computer works 3 times. First to compute fm, second to compute fn, 
    and third to compare the two lists to compute cf.

Why not a single scan from 1 to max(m,n)?

    For each i in 1 to max(m,n), add i to fm if i divides 
    m and add i to fn if i divides n

Even better?

    Why compute two lists and then compare them to 
    compute common factors cf? Do it in one shot.

        For each i in 1 to max(m,n), if i divides m and i
        also divides n, then add i to cf

    Actually, any common factor must be less than
    min(m,n)

        For each i in 1 to min(m,n), if i divides m and i
        also divides n, then add i to cf    

        Ex: Can 18 be a factor of 12?
            No.

            Can 17 be factor of 12?
            No.

            Can 15 be factor of 12?
            No.

            So after 12 everything is waste.

i.e, A common factor cannot be greater than the smaller number. !!!

Suppose m = 12 and n = 18

Largest possible common factor would be 12 which is m here.

'''

# A shorter Python program

def gcd(m,n):
    cf = []

    for i in range(1,min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            cf.append(i)

    return(cf[-1])

print(gcd(12,18))

'''

Do we need lists at all?

    We only need the largest common factor Not list. So why store list, Waste of memory.

    1 will always be a common factor

    Each time we find a larger common factor, discard
    the previous one

    Remember the largest common factor seen so far
    and return it.

    Hence No list. Only one variable.

    mrcf — most recent common factor

'''

# No Lists

def gcd(m,n):
    
    for i in range(1,min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            mrcf = i

    return(mrcf)

print(gcd(12,18))

'''

Scan backwards?

    To find the largest common factor, start at the end
    and work backwards

    Let i run from min(m,n) to 1

    First common factor that we find will be gcd!

'''

# No Lists

def gcd(m,n):

    i = min(m,n)

    while i > 0:
        if (m%i) == 0 and (n%i) == 0:
            return(i)
        else:
            i = i-1

'''

A new kind of repetition

    while condition:
        step 1
        step 2

        . . .
        step k

    Don’t know in advance how many times we will
    repeat the steps

    Should be careful to ensure the loop terminates—
    eventually the condition should become false!

'''

'''

Summary:

    With a little thought, we have dramatically
    simplified our naive algorithm

    Though the newer versions are simpler, they still
    take time proportional to the values m and n

    Even this backward scanning algorithm is not the fastest. 
    Worst case, if you call: gcd(99991, 99989) it may still 
    check almost every number from 99989 down to 1.

    A much more efficient approach is possible

'''