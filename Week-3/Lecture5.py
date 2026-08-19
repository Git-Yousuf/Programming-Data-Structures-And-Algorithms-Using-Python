'''

Efficiency

    Measure time taken by an algorithm as a function
    T(n) with respect to input size n

    Usually report worst case behaviour
        
        Worst case for searching in a sequence is when
        value is not found

        Worst case is easier to calculate than “average”
        case or other more reasonable measures

'''

'''

O( ) notation

    Interested in broad relationship between input size
    and running time

    Is T(n) proportional to log n, n, n log n, n2
    , …, 2n?

    Write T(n) = O(n), T(n) = O(n log n), … to indicate
    this

        Linear scan is O(n) for arrays and lists
        
        Binary search is O(log n) for sorted arrays

'''

'''

Refer Python Week 3 Lecture 5 4th Page.

'''

'''

Efficiency

    Theoretically T(n) = O(nk) is considered efficient

        Polynomial time

    In practice even T(n) = O(n2) has very limited
    effective range

        Inputs larger than size 5000 take very long

'''