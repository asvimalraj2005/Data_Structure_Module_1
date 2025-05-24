# Problem Statement
# Given an array A of N integers, return the number of unique elements in the array 
# Input Format : First argument A is an array of integers.
# Output Format : Return an integer which denotes the no of unique elements present inside the list 
#
# Example 1 A = [ 3 , 4 , 3 , 6 , 6 ]
# Output      =  3            
#
# Explanation ---> Distinct elements in the array are 3 , 4 , 6 
#
# Problem solution approach 
# Use dictionary function to convert the given list to a dictionary set where duplicate elements are removed only the non-duplicate elements are stored and return the len of the collection set 
# Below is the python code for the above approach 
def DistinctElements(A):
    Ans_ = set ( A )
    return len( Ans_ )       

    # return Ans_                             #  <------------ If you want to return the founded unique elements in the list 

A=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5]
print(DistinctElements(A))


# This is one way of hashing approach but in depth there are different coding types where real hashing code is implemented 
# like usage of several functions within a class and adding elements through hash functions 
