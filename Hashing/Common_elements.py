Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements in both the array.


NOTE:


Each element in the result should appear as many times as it appears in both arrays.
The result can be in any order.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.

        freq_B = {}
        for i in range(len(B)):
            if B[i] in freq_B:
                freq_B[B[i]] += 1
            else:
                freq_B[B[i]] = 1

        lst = []
        for i in range(len(A)):
            if A[i] in freq_B:
                if freq_B[A[i]] != 0:
                    lst.append(A[i])
                    freq_B[A[i]] -= 1
        return lst
