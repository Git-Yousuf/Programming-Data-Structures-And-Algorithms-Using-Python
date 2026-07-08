# Algorithm - how to systematically perform a task
# Programming Languages are used to describe the steps
# Step means degrees of details. Eg: "Arrange the chairs" vs "Make 8 rows with 10 chairs in each row"

# Valid Algorithm:
# 1. Finite presentation of the steps
# 2. Terminates after a finite number of steps
# 3. 

# GCD - Greatest Common Division

# First Python Program - Computing gcd
def gcd(m,n):
    # List out the factors of m
    
    # Note:
    # 1. Factors of m must be between 1 and m
    # 2. If it divides m without a remainder, add it to list of factors
    # 3. Likewise for n
    
    fm=[]
    for i in range(1,m+1):
        if (m%i)==0:
            fm.append(i)
            
    # List out the factors of n
    
    fn=[]
    for j in range(1,n+1):
        if (n%j)==0:
            fn.append(j)
     
     # Report the largest number that appears on both lists  
          
    cf=[]
    for f in fm:
        if f in fn:
            cf.append(f)
    return(cf[-1])

print(gcd(12,18))
    
# Algorithm for gcd(m,n)
# Use fm, fn for list of factors of m, n, respectively
# For each i from 1 to m, add i to fm if i divides m
# For each j from 1 to n, add j to fn if j divides n
# Use cf for list of common factors
# For each f in fm, add f to cf if f also appears in fn
# Return largest (rightmost) value in cf

# Important Poimts
#1. Use names to remember intermediate values - m, n, fm, fn, cf, i, j, f

#2. Values can be single items or collections
#       - m, n, i, j, f are single numbers
#       - fm, fn, cf are lists of numbers

#3. Assign values to names: Explicitly, fn = [], and implicitly, for f in cf:

#4. Update them, fn.append(i)

#5. Program is a sequence of steps

#6. Some steps are repeated - Do the same thing for each item in a list

#7. Some steps are executed conditionally - Do something if a value meets some requirement