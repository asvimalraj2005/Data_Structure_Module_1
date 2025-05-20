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
def FirstIndex(A,B):                                # FirstIndex has two parameters one is for Array A and another one is for B element
    def Helper(Index):                              # Helper function is used to traverse the array with the help of an index pointer
        if Index==len(A):                           # Base case if the Index pointer variable reaches the end of the array then we don't have any element which matches with the element B so we are returning it as zero 
            return 0
        elif A[Index]==B:                           # If the A[Index]==B condition does satisfies then we are returning the index 
            return Index
        return Helper(Index+1)                      # Calling the Helper function again and again recursively 
    return Helper(0)                                # The value which has been calculated in the Helper function will be returned to FirstIndex Function and in the same we are calling the Helper function with 0 value in the parenthesis which states the index 
        

A=['1','2','3','4','5','6','7','8']                 # Array A 
B='5'                                               # B 
print(FirstIndex(A,B))                              # The value which is returned will get printed here 
