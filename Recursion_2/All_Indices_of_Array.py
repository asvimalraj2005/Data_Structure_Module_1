# Problem Statement 
# All Indices of Array 
# Given an array of integers A with N elements and a target integer B, the taks is to find all the indices at which B occurs in the array 
# Note : The problem encourages recursive logic for learning  purposes. Although the online judge doesn't enforce recursion. It's recommended to use 
# recursive solutions to align with the question's spirit
# Input Format : First Argument in an Array of Integers A. Second Argument is the Target B
# Return the sorted array of Indices 
# Input A = [ 8 , 7 , 5 , 6 , 5 , 5 ]
# B = 5 
# O/P : [ 2 , 4 , 5 ]
# Below is the python code for the above problem statements 
def allIndices(A,B):                                    # An array and an index is provided here 
    def helper(index):                                  # Helper function is used for indexing purpose   
        if index==len(A):                               # Inside the index function, Base case : when the recursion reaches past the last index, it returns an empty list 
            return []
        rest=helper(index+1)                            # Recursively call the helper function for the next index 
        if A[index]==B:                                 # If the current element matches with the B element 
            return [index]+rest                         # [index]  contains the index where the element with the index is getting matched with B and rest is the result of the recursive call 
        else:
            return rest                                 
    return helper(0)                                    # Start the recursion from index 0 

A=['1','2','3','4','5','6']
B=5
print(allIndices(A,B))
