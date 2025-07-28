Given an integer array A of size N, find the first repeating element in it.
We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.
If there is no repeating element, return -1.
class Solution:
# @param A : list of integers
# @return an integer
    def solve(self, A):
      repeatingElements = {}
      for i in range(len(A)):
      if repeatingElements.get(A[i]) == None:
        repeatingElements[A[i]] = 1
      else:
        repeatingElements[A[i]] += 1


      for i in range(len(A)):
      if repeatingElements.get(A[i]) <= 1:
        continue
      else:
        return A[i]
      return -1

