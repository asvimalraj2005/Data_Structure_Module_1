# The problem is to find the first natural missing number 
# Example 1 : arr[5] : [3,-1,1,2,7]         -> ans = 4
# Example 2 : arr[7] : [9,2,6,4,-8,1,3]     -> ans = 5
# Example 3 : arr[6] : [1,0,-5,-6,4,2]      -> ans = 3
# Range of answer --> [ 1 , (N+1) ]
# Bruteforce --> For all no in 1 to (N+1), check if it is present in the array or not 
#                                                         present --> iterate the array Time Complexity = O(N^2) SC=O(1)
#                                                         a) Store the elements in a set 
#                                                         b) Check element in set in Time Complexity O(1)
# Solution --> Check if 1 ---> N is present in array
# Check --> Update the A[] with, index indicating if the element is present 
# 1 ---> N       0 ---> (N-1)
# A[i]  <------->  (i-1) index 
# Keep the elements ar their correct position 
#
## 1 ---> N        0 ----> N-1 
# Correct position mean for any poistion A[i] we should swap it with (i-1) index 

#                               0 , 1 , 2 , 3 , 4 , 5 , 6 , 7     
# Example arr[] ---> arr[] -> [ 4 , 2 , 7 , 6 , 9 , 1 , 5 , 3 ]                 i=0
#                               6           4                      swapped      A[i]=4 and 4-1=3 which is the index where the first element is going get swapped
#                               1                   6              swapped      A[i]=6 and 6-1=5 which is the index for the element 6 to swapped with the index 5                                    
#                                       5               7          Not swapped  A[i]=1 and 1-1=0 which the outbound condition                      
#                                                                  i=1
#                                                                  Not swapped A[1]=2 which is already at the right position; 1-1=0
#                                                                  i=2
#                                                                  Swapped A[2]=7 ; 7-1=6 index position for the element 7 and the index 6 element will be placed in index 2 position 
#                                                                  i=2
#                                                                  Swapped A[2]=5 which is not a correct position; so we are creating a new index position 5-1=4, now the element 5 will get swapped to index 4 position and index 4 position element will come to index 2 position 
#                                                                  And so on 
# The end array after the swap 1,2,3,4,5,6,7,9 Ans=8
# Below is the python code 


def swap(arr, i, j):                                    # This function used to swap the array elements 
    arr[i], arr[j] = arr[j], arr[i]                     # Swapping the elements           

def firstnaturalmissingnumber(Array):
    i=0                                                 # Initialising the loop variable i=0
    N=len(Array)                                        # N is stores the length of the variable 
    while(i<N):                                         # Until i meets the length of the array it will gets executed 
        if(Array[i]==i+1):                              # Checking if the current element is equal to correct position or not 
            i=i+1                                       # If it in correct position we are incrementing i=i+1
        elif (1<=Array[i] and Array[i]<=N):             # If Array[i] is greater than 1 and less than N 
            swap(Array,i,(Array[i]-1))                  # We are swapping the positions
        else:                                           # After the swap
            i=i+1                                       # We are incrementing i=i+1
                                                        # After the process of exchanging elements between the index positions 
    for i in range(N-1):                                # Executing a loop until the length-1 of the array                           
        if Array[i]!=i+1:                               # If the current element is not equal to next index position we are returning i+1(index position) if same we are moving next position 
            return i+1
    return N+1                                          # After everything get's over every element is present inside the array then we are going to return len+1 element 


array=[1,2,9,8,7,6,5,4]
print(firstnaturalmissingnumber(array))
