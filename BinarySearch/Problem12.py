You are given a 2-D matrix C of size A × B.
You need to build a new 1-D array of size A by taking one element from each row of the 2-D matrix in such a way that the cost of the newly built array is minimized.

The cost of an array is the minimum possible value of the absolute difference between any two adjacent elements of the array.

So if the newly built array is X, the element picked from row 1 will become X[1], element picked from row 2 will become X[2], and so on.

Determine the minimum cost of the newly built array.


  def is_possible(C, D):
    A, B = len(C), len(C[0])
    dp = [True] * B  

    for i in range(1, A):
        new_dp = [False] * B
        for j in range(B):  
            for k in range(B):
                if dp[k] and abs(C[i][j] - C[i-1][k]) >= D:
                    new_dp[j] = True
                    break
        dp = new_dp
        if not any(dp):
            return False
    return True

def min_cost(C):
    low, high = 0, max(max(row) for row in C)
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if is_possible(C, mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

