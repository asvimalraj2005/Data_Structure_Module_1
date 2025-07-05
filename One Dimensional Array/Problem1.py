
You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.





Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.

If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.


class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        n = len(A)
        L = 1
        R = 1
        max_L = 1
        max_R = 1
        ans = -999999
        curr_sum = 0

        if A.count('0') == 0:
            return []
        for i in range(len(A)):
            if A[i] == '0':
                curr_sum += 1
                if curr_sum > ans:
                    ans = curr_sum
                                       
                    R = i+1
                    max_L = L
                    max_R = R
               
            if A[i] == '1':
                curr_sum -= 1
                if curr_sum < 0:
                    curr_sum = 0
                    L = i+2

        return [max_L, max_R]

                
