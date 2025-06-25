Given a matrix of integers A of size N x M in which each row is sorted.


Find and return the overall median of matrix A.

NOTE: No extra memory is allowed.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.

import bisect

def find_matrix_median(A):
    N = len(A)
    M = len(A[0])
    
    low = min(row[0] for row in A)
    high = max(row[-1] for row in A)
    
    while low < high:
        mid = (low + high) // 2
        count = 0
        for row in A:
            # Count of elements <= mid using bisect
            count += bisect.bisect_right(row, mid)
        
        if count < (N * M + 1) // 2:
            low = mid + 1
        else:
            high = mid
            
    return low
