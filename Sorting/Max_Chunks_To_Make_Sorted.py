# Problem Statement --> Max Chunks To Make Sorted
# Given an array of integers A of size N that is a permutation of [0,1,2,....,(N-1)], if we split 
# the array into some number of "chunks" (partitions), and individually sort each chunk.
# After concatenating them in order of splitting, the results equals the sorted array.
# What is the most number of chunks we could have made ? 
#
# Example 1 
# Input format : A = [ 1 , 2 , 3 , 4 , 0 ]
# Output format : 1
#
# Example 2 
# Input format : A = [ 2 , 0 , 1 , 3 ]
# Output format : 2 
#
# Explanation 1 for example 1
# A = [ 1 , 2 , 3 , 4 , 0 ]
# The max values at each index are : [1 , 2 , 3 , 4 , 4 ]
# we can only partition after 4 , so no of chunks we can get is 1 
#
# Explanation 2 for example 2 
# A = [ 2 , 0 , 1 , 3 ]
# The max values at each index are : [ 2 , 2 , 2 , 3 ]
# we can partition after index 2 and 3, resulting in 2 chunks 
#
#
# Maximum of A [ 0 - i ] is i        where A[i] is the elements and i is the index , we should have find the max value in the array by carrying towards to the right which equals with the index value 
# then we can take it as a separate chunk 
#
#
# I think indexes of the array is compared with the array values with carrying max so far 
# Indexes               A [ i ]             Max so far             Split into chunks ? 
#   0                       2                   2                       No ( 2 != 0 )
#   1                       0                   2                       No ( 2 != 0 )
#   2                       1                   2                      Yes ( 2 == 2 )               <-- we can split the array into chunks here
#   3                       3                   3                      Yes ( 3 == 3 )               <-- we can split the array into chunks here too 
#
# Below is the python code 
#
def max_chunks_to_sorted(A):
    max_so_far=0                                # We are creating an variable named max_so_far for carrying the max element of the 0 to ith iteration and updating over with it for further iterations 
    chunks=0                                    # Chunks variable is used to count the no of sub list that the original can be splitted in order to sort it after the split 
    for i in range(len(A)):                     # Iterating over the array 
        max_so_far=max(max_so_far,A[i])         # Carrying the max value 
        if max_so_far==i:                       # If the max value from 0 - i th iteration is equals to the index 
            chunks=chunks+1                     # Then we are assuming that here we can able to split the array but in this algorithm we can't but we can count on how many the array can be splitted in chunks 
    return chunks                               # Returning the chunks found in the array 


A = [1,2,3,4,0,5,6]                             # Note : This algorithmic approach is built on pattern wise on the section of permutation where no duplicate elements are not allowed in the list, if any duplicates elements is present inside the array then this algorithm won't work properly 
print(max_chunks_to_sorted(A))


# Well the number representatively whole numbers 0,1,2,3,4,5,6,7,8,9 to infinity without any repetative values in them 
# This numbers are put or created with it inside the list 
# where this could be in any permutation 1 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 0 
#                                        8 , 7 , 6 , 5 , 4 , 3 , 2 , 0 , 1 , 9 
# on the second list we are going to carry 8 valued element from index 0 to the index where it matches with the index 8, if it matches then we are assuming or counting that here a chunk i.e partition could be made to sort the array 