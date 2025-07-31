Given two integers A and B, find the greatest possible positive integer M, such that A % M = B % M.

def greatest_M(A, B):
    if A == B:
        return float('inf')
    if A > B:
        return A - B
    else:
        return B - A

