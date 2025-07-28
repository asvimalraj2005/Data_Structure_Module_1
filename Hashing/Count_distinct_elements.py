Count distinct elementslete Solution is Penalty free now
Problem Description
Given an array A of N integers, return the number of unique elements in the array.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return len(set(A))
