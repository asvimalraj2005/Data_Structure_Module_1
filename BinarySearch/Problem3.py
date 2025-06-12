# Array 3 Pointers
# Problem Description
# You are given 3 sorted arrays A, B and C.
# Find i, j, k such that : max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
# Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])).
# Problem Constraints
# 1 <= len(A), len(B), len(c) <= 106
# 0 <= A[i], B[i], C[i] <= 107
# Input Format
# First argument is an integer array A.
# Second argument is an integer array B.
# Third argument is an integer array C.
# Output Format
# Return an single integer denoting the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])).
# Example Input
# Input 1:
# A = [1, 4, 10]
# B = [2, 15, 20]
# C = [10, 12]
# Input 2:
#  A = [3, 5, 6]
#  B = [2]
#  C = [3, 4]
# Example Output
# Output 1:
# 5
# Output 2:
#  1
# Example Explanation
# Explanation 1:
# With 10 from A, 15 from B and 10 from C.
# Explanation 2:
# With 3 from A, 2 from B and 3 from C.
# Below is the code for the above problem
import sys

class Solution:
    def minimize(self, A, B, C):
        p1, p2, p3 = 0, 0, 0
        ans = sys.maxsize

        while p1 < len(A) and p2 < len(B) and p3 < len(C):
            a,b,c= A[p1], B[p2], C[p3]
            current_max=max(abs(a - b), abs(b - c), abs(c - a))
            ans=min(ans,current_max)
            min_val=min(a,b,c)
            if a==min_val:
                p1+=1
            elif b==min_val:
                p2+=1
            else:
                p3+=1

        return ans
