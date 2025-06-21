# Given an array of integers A of size N and an integer B.
# In a single operation, any one element of the array can be increased by 1. You are allowed to do at most B such operations.
# Find the number with the maximum number of occurrences and return an array C of size 2, where C[0] is the number of occurrences, and C[1] is the number with maximum occurrence.
# If there are several such numbers, your task is to find the minimum one.
class Solution:
    # @param A : list of integers
    # @param B : integer (number of operations)
    # @return a list [max_frequency, number_with_max_frequency]
    def maxFrequency(self, A, B):
        A.sort()
        l = 0
        total = 0
        max_freq = 0
        number = 0

        for r in range(len(A)):
            total += A[r]
            # Total operations needed to make all elements in window equal to A[r]
            while (A[r] * (r - l + 1)) - total > B:
                total -= A[l]
                l += 1
            # Update max frequency and number
            freq = r - l + 1
            if freq > max_freq:
                max_freq = freq
                number = A[r]

        return [max_freq, number]
