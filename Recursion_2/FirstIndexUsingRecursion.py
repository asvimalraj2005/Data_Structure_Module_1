# Problem Statement
# You are given an array A of size N. Write a recursive function that returns the fist index at which 
# an integer B is found in the array
# Note : if B is not found anywhere in the array then return -1 
# Input Format : The function contains two arguments. The first argument is the array A.
# Output Format : Return the Index of B from the list in integer format if B is present in the array, else return -1 
# Input : A = [ -3 , 5 , 6 , 2 ]
#         B = 6 
# Output : 2 
# Example Explanation 
# At index 0 we have -3 
# At index 1 we have 5 
# At index 2 we have 6 which equal to B 
# Problem Solution Approach is to use an helper function and an index pointer which increments by 1 for every recursion recursively and return only the first occurence
# Below is the python code 
def FirstIndex(A,B):
    def Helper(Index):
        if Index==len(A):
            return 0
        elif A[Index]==B:
            return Index
    return Helper(0)
        

A=['1','2','3','4','5','6','7','8']
B='5'
print(FirstIndex(A,B))
