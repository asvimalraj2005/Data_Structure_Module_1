# Bubble sort is the basic sorting algorithm that repeatedly swap the adjacent element in an array 
# The bubble sort places the first largest element in the last position of the array 
# Second largest element will be placed in the second last position in the array which N-2
# Third largest element will be placed in the third last position in the array which is N-3 
# Below is python code for the above solutional approach where we use nested for loop for the traversing and swapping purpose
#
def BubbleSort(A):                              # Creating the function named BubbleSort and passing the array A
    N=len(A)                                    # Storing the length of the array into the variable named N 
    for i in range(N):                          # Initiating the outer loop from 0 to N 
        swapped=False                           # Boolean variable named swapped is used here to break out from the inner loop after the swapping of the element is done 
        for j in range(0,N-i-1):                # Initiating the inner loop from 0 to N-i-1 -> this N-i-1 for every iteration i index we can able to calculate the last index of the array, this loop will run 0 to N-i-1 for every i iteration 
            if A[j]>A[j+1]:                     # By using this we are checking whether the current element is greater than the next element or not 
                A[j],A[j+1]=A[j+1],A[j]         # If the above condition satisfies then this line will get executed and then we are swapping the current element with the next element 
                swapped=True                    # And we are breaking out of the loop by changing the boolean value of swapped = True  if the A[j]>A[j+1] does not satisfies the condition 
        if swapped==False:                      # If swapped is still false we are breaking out of the loop and moving to the next i th iteration
            break                               # Break is used to exit the for loop 
    return A                                    # We are returning the A sorted Array 

A=[8,7,6,5,4,4,5,6,4,3]
print(BubbleSort(A))
                                                # Below is explanation 
                                                # Indexes                  0   1   2   3   4   5   6   7   8   9 
                                                # let us take an example [ 8 , 7 , 6 , 5 , 4 , 4 , 5 , 6 , 4 , 3 ]            N = len ( A ) -> 10
                                                # for i in range(N)        i
                                                #                          swapped=False
                                                # for j in range(0,N-i-1) 
                                                # the condition 0,N-i-1 says that 0 to 10-0-1 which is index 9 now we are traversing from 0 to 8 inclusively 
                                                # if A [ j ] > A [ j + 1 ] :  this condition checks the current element is greater than or not , if it is greater than we are swapping the elements 
                                                # A [ j ] , A [ j + 1 ] = A [ j + 1] , A [ j ] swaps the two element 
                                                # after swapping still the swapped=True it indicates that the array is still not sorted 
                                                # So there should be i iterations for the array to get sorted 
                                                # After that we are returning the array A 
    