# Selection sort is a versus based sorting algorithm. It sorts an array by repeatedly selecting the smallest element from the unsorted portion and swapping it with the first unsorted element. 
# Procedure find the min in the array and replace the min value in the first index and swap the first index element at where you have found the min value 
# Reference take an example array : [ 5 , 4 , 3 , 2 , 1 ] in this array 1 is the min value and we should have to swap the element 5 with 1 
# Now the array becomes [ 1 , 4 , 3 , 2 , 5 ] -> first iteration is completed 
# Now the second iteration we are in the position of element value 4 and index 2 ; we should have to iterate over the array and find second minimum -> Now the second minimum is 2 
# Now we should have swap the element 4 with element 2 by accessing those element indexes 
# Now the array becomes [ 1 , 2 , 3 , 4 , 5 ] the array is sorted 
# 
# Below is the python code for the above approach and explanation below is written with line of code 
#
def selection_sort(A):                              # Creating a function named selection_sort 
    N=len(A)                                        # Storing the length of the array in N variable 
    for i in range(N-1):                            # Iterating or traversing over the array; this is outer loop for every i iteration -> inner loop j will iterate from i+1 to N 
        min_ind=i                                   # We are assuming that the element one index as the minimum value 
        for j in range(i+1,N):                      # Now at the second loop we are iterating the array with i+1 th index to N for finding the minimum value which is going to be or equal to be with the element value index 1 which have already assumed that it is an smaller value 
            if A[j]<A[min_ind]:                     # The above line implies here too where if the iterating j th element is lower than the element we have assumed as smaller 
                min_ind=j                           # Then we are updating the min_ind variable index value to j 
        A[i],A[min_ind]=A[min_ind],A[i]             # Here the swapping is done after the inner loop completes the j iteration i+1 to N of the outer loop 0 to N 
    return A                                        # We are returning the A list with sorted values 

A=[12,12,4,3,56,7,8,5,3,2,3,5,7,8]
print(selection_sort(A))
                                                    # Indexes                                               0   1   2   3   4   5   6   7   8
                                                    # Explanation let us take an example array            [ 6 , 5 , 4 , 3 , 4 , 5 , 8 , 7 , 6 ]
                                                    #
                                                    # Outer loop -> for i in range(N-1) -> Now i = 0        i                                         Now min_ind stores the index of this element i.e 0 -> 0 we get stored in the min_ind                                
                                                    # Inner loop -> for j in range(i+1,N) -> Now j = i + 1      j ---------------------------->       Now j is here now -> if A [j] < A [min_ind]  :   this condition checks that for every j element with i element -> 5 < 6 ; 4 < 6 ; 3 < 6 ; 4 < 6 ; 5 < 6 ; 8 < 6 ; 7 < 6 ; 6 < 6    for this all comparison we are going to take only element from it and swap it i.e 3 with 6 the index value of 3 is 3 which is going to be stored in min_ind variable 
                                                    # After completing the inner loop this condition will work  A[0] , A [3]  =  A [3] , A [0]  ->  3 , 6 
                                                    #
                                                    # Now the array becomes like this -->                 [ 3 , 5 , 4 , 6 , 4 , 5 , 8 , 7 , 6 ] 
                                                    # Outer loop -> for i in range(N-1) ->  Now i =1            i                                     As I said before for every i iteration j would excute from i+1,n
                                                    # Inner loop -> for j in range(i+1,N) -> Now j = i + 1          j ------------------------>       Now j is here now -> if A [j] < A [min_ind]  :  which is comparing all the values of iteration j with iteration i element once, 4 < 5 , 6 < 5 , 4 < 5 , 5 < 5 , 8 < 5 , 7 < 5 , 6 < 5  for all this comparison we are going take the first satisfying element which satisfies the condition which 4 < 5 and the index value of 4 is 2 
                                                    # After completing the inner loop this condition will work  A[1] , A[2] = A[2] , A[1] -> 4 , 5
                                                    #
                                                    # Now the array looks like this -->                   [ 3 , 4 , 5 , 6 , 4 , 5 , 8 , 7 , 6 ] 
                                                    #
