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
def allIndices(A,B):
    def helper(index):
        if index==len(A):
            return []
        rest=helper(index+1)
        if A[index]==B:
            return [index]+rest
        else:
            return rest
    return helper(0)        