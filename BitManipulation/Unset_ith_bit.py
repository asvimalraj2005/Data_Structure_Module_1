"""Problem Description

You are given two integers A and B.
If B-th bit in A is set, make it unset.
If B-th bit in A is unset, leave as it is.
Return the updated A value.

Note:
The bit position is 0-indexed, which means that the least significant bit (LSB) has index 0.
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return A & ~(1 << B)

""" Left shifting B times using << and changing 1 to 0 or 0 to 1 by using ~(not) operator after using & operator""" 


