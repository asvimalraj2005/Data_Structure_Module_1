# Problem Statement 
# Given an array of integer A. if i < j and  A [ i ] >  A [ j ],
# then the pair ( i , j ) is called an inversion of A.
# Find the total number of inversions of A modulo ( 10 ^ 9 + 7 )
# Input Format : The only argument given is the integer array A 
# Output Format : Return the number of inversions of A modulo ( 10 ^ 9 + 7 )
# Example explanation 
# Indexes     0   1   2   3 
# A =       [ 3 , 4 , 1 , 2 ]
# O/P --> 4 
# --> The pair ( 0 , 2 ) is an inversion as 0 < 2 and A [ 0 ] > A [ 2 ]
# --> The pair ( 0 , 3 ) is an inversion as 0 < 3 and A [ 0 ] > A [ 3 ] 
# --> The pair ( 1 , 2 ) is an inversion as 1 < 2 and A [ 1 ] > A [ 2 ]
# --> The pair ( 1 , 3 ) is an inversion as 1 < 3 and A [ 1 ] > A [ 3 ]
#
# Problem solution approach
# General common approach is to use a nested loop over the array and check the inversion of an by using the condition A [ i ] > A [ j ] with i < j, and if does satisfies any of the element in the array use cound_variable for counting the pairs 
# 
# Below is the python code 
def InversionCount(A):
    Mod=10**9+7                                                                         # Used to calculate the mod of an another variable 
    count=0                                                                             # Count variable is used to count the inversions which are found inside the array 
    N=len(A)                                                                            # N variable stores the total length of the array 
    for i in range(N):                                                                  # Outer loop runs from 0 to N-1 
        element_i_range=A[i]                                                            # element_i_range is used to store i th  iterating element 
        element_i_index=i                                                               # element_i_index is used to store i th  iterating index 
        for j in range(i+1,N):                                                          # Inner loop runs from i+1 to N 
            element_j_range=A[j]                                                        # element_j_range is used to store j th  iterating element 
            element_j_index=j                                                           # element_j_index is used to store j th  iterating index 
            if element_i_index<element_j_index and element_i_range>element_j_range:     # Using the condition  A [ i ]  >  A [ j ] and  i  <  j 
                count=count+1                                                           # If any of the elements in the array satisfies the condition we are adding one to count for every iteration where the count variable carries the previosly added value with it for the next iteration to not lost the tracked counts   
    return count%Mod                                                                    # Returning the count % Mod  

A = ['3','4','1','2']
print(InversionCount(A))                                                                # Explanation of the outer loop -> 0  1  2  3  4  5 
                                                                                        #                                  i                               to  N 
                                                                                        # Inner loop j                        i+1---------->               to  N 
                                                                                        #
                                                                                        # Iteration one is over     
                                                                                        # 
                                                                                        # Outer loop                          i                            to N 
                                                                                        # Inner loop j                           i+1------->               to N 
                                                                                        # 
                                                                                        # Iteration two is over 
                                                                                        #
                                                                                        # Outer loop                             i                         to N 
                                                                                        # Inner loop j                             i+1----->               to N 