A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.
def find(mat):
    m, n = len(mat), len(mat[0])
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2

        # Find the row index of the max element in mid column
        max_row = 0
        for i in range(m):
            if mat[i][mid] > mat[max_row][mid]:
                max_row = i

        # Get the left and right neighbor values (use -1 if out of bounds)
        left_val = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
        right_val = mat[max_row][mid + 1] if mid + 1 < n else -1
        current = mat[max_row][mid]

        if current > left_val and current > right_val:
            return [max_row, mid]
        elif left_val > current:
            right = mid - 1
        else:
            left = mid + 1

    return [-1, -1]  # should never reach here due to constraints
