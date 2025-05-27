# Problem Description 
# Given an array of integers A, sort the array into wave-like array and return it.
# In other words, arrange the elements into a sequence such that 
# a1 > = a2 < = a3 > = a4 < = a5 
# Note : If multiple answers are possible, return the lexicographically smallest one
#
# Input Format --> The first argument is an integer array A 
# Output Format --> Return an array arranged in the sequence as described 
#
# Example A = [1,2,3,4]
# Output --> [4,1,2,3] 
# Sort the array by using sort function
# Now the array becomes 1,2,3,4
# swap the elements A[i] , A[i + 1] = A[i] , A[i + 1]
# now the element for every iteration becomes like  2  ,    1  ,  4  ,   3 
#                                                  a1  > = a2 < = a3 > = a4
# Below is the python code for the above approach
def wave_array(A):
    A.sort()
    for i in range(0,len(A)-1,2):                    # The step is used move to next index element position after swapping before two elements 
        A[i],A[i+1]=A[i+1],A[i]                      # Swapping of element is happened here 
    return A                                         # Returning the Wave Array 

