""" You are given two integers A and B.
If B-th bit in A is set, make it unset
If B-th bit in A is unset, make it set
Return the updated A value """

def toggle_bit(A: int, B: int) -> int:
    return A ^ (1 << B)
