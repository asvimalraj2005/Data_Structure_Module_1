# You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return the of count of distinct numbers in all windows of size B.
# Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.
# NOTE: if B > N, return an empty array.
def distinct_numbers_in_window(A, B):
    N=len(A)
    if B>N:
        return []

    result=[]
    for i in range(N-B+1):
        window=A[i:i+B]
        distinct_count=len(set(window))
        result.append(distinct_count)

    return result
