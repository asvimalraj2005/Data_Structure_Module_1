# Merge sort is divide and conquer algorithm 
# It's known for it's efficiency and stability 
# First step it divides the array into two halves until the divided array length becomes one 
# Second step is recursively sort the array until every single component of the whole array merged together
# Third step is return the sorted array 
# Below is the code for the above approach 
#       
def mergesort(A,left,mid,right):      # (6)
    
    N1=mid-left+1                     # N1 stores the value where the loop should stop in range (1)   -> First left half
    N2=right-mid                      # N2 stores the value where the loop should stop in range (2)   -> Second right half 
    
    L=[0]*N1                          # Creating an empty array where the array firstly initialised with zeroes and after that it is will get filled with the values which is present inside the array A for every recursive call in the merge_Sort function 
    R=[0]*N2                          # Creating an empty array where the array firstly initialised with zeroes and after that it is will get filled with the values which is present inside the array A for every recursive call in the merge_Sort function 
    
    for i in range(N1):               # N1 Range
        L[i]=A[left+i]                # Temporary array which is used to store the left half of the array, sub array maybe ain't still clearly understood but will 
        
    for j in range(N2):               # N2 Range
        R[j]=A[mid+1+j]               # Temporary array which is used to store the right half of the array 
        
    i=0                               # (3) Indexes variables used to iterate over the elements in the array L and R ; if L element is less than R then it is stored in the A 
    j=0                               # (4) if element R is less than element L then it is going to be stored in array A 
    K=left                            # (5) index for A[] where the merged result is stored
    
    while i < N1 and j < N2 :         # While loop initialisation with the i and j pointers (3) and (4)
        if L[i]<=R[j]:                # Comparing is done here
            A[K]=L[i]                 # Incrementing the i by one after comparing the L array element with R and adding in A if it is lesser than R 
            i=i+1                    
        else:
            A[K]=R[j]                 # Otherwise this condition will work
            j=j+1
        K=K+1                         # For every i and j , k will be incremented by 1 for the index position for the A array 
        
    while i < N1 :                    # For the non-calculated elements on L this loop will work 
        A[K]=L[i]
        i=i+1
        K=K+1
    
    while j < N2 :                    # For the non-calculated elements on R this loop will work 
        A[K]=R[j]
        j=j+1
        K=K+1

def merge_sort(A,left,right):         # Merge function is divide the array until the array length becomes one 
    if left < right :                 # left < right we are returning the values of list with lenght 1 on the stack to the mergesort (6)
        mid = ( left + right ) // 2
        
        merge_sort(A,left,mid)        # Calling this function recursively to divide the left array until it reaches the length with 1 -> [1,2,3] -> [1,2] [3] -> [1] [2] [3]
        merge_sort(A,mid+1,right)     # Same applies for this too 
        mergesort(A,left,mid,right)   # (6)
    

A=[12,11,13,5,6,7]
merge_sort(A,0,len(A)-1)
print(A)
    
        
        
        