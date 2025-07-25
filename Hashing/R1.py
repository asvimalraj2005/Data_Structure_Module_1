You are given an array A of N integers. Return the count of elements with frequncy 1 in the given array.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hashmap = {}
        for ele in A:
            if ele not in hashmap:
                hashmap[ele] = 1
            else:
                hashmap[ele] += 1
        count = 0
        for i in hashmap:
            if hashmap[i] == 1:
                count += 1
        return count
