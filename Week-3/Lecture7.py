'''

How to sort?

    You are a Teaching Assistant for a course

    The instructor gives you a stack of exam answer
    papers with marks, ordered randomly

    Your task is to arrange them in descending order

'''

'''

Strategy 2

    First paper: put in a new stack

    Second paper:
        
        Lower marks than first? Place below first paper

        Higher marks than first? Place above first paper

    Third paper

        Insert into the correct position with respect to first
        two papers

    Do this for each subsequent paper:
    insert into correct position in new sorted stack

'''

'''

Startegy 2 ...

    74 32 89 55 21 64 

    74 32 89 55 21 64
    74
    
    74 32 89 55 21 64
    32 74

    74 32 89 55 21 64
    32 74 89 

    74 32 89 55 21 64
    32 55 74 89
    
    74 32 89 55 21 64
    21 32 55 74 89
    
    74 32 89 55 21 64
    21 32 55 64 74 89 
    
'''

'''

Strategy 2 …

    Insertion Sort

        Start building a sorted sequence with one element
        
        Pick up next unsorted element and insert it into its
        correct place in the already sorted sequence

'''

# Insertion Sort
def InsertionSort(seq):
    for sliceEnd in range(len(seq)):
    # Build longer and longer sorted slices
    # In each iteration seq[0:sliceEnd] already sorted
    # Move first element after sorted slice left
    # till it is in the correct place
        pos = sliceEnd
        while pos > 0 and seq[pos] < seq[pos-1]:
            (seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
            pos = pos-1

'''

Insertion Sort

    74 32 89 55 21 64

    32 74 89 55 21 64

    32 74 89 55 21 64

    32 74 55 89 21 64

    32 55 74 89 21 64 

    32 55 74 21 89 64 

    32 55 21 74 89 64

    32 21 55 74 89 64

    21 32 55 74 89 64

    21 32 55 74 64 89

    21 32 55 64 74 89 

'''

'''

Analysis of Insertion Sort

    Inserting a new value in sorted segment of length
    k requires upto k steps in the worst case

    In each iteration, sorted segment in which to insert
    increased by 1
    
    T(n) = 1 + 2 + … + n-1 = n(n-1)/2 = O(n2)

'''