# Next Permutation problem statement 
# Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N
# If such arrangement is not possible, it must be rearranged as the lowest possible order i.e, sorted in ascending order 
# Note: The replacement must be in-place,do not allocate extra memory 
# Take an 1 D array as an example [ 1 , 2 , 3 ]         -> Think Array as an integer
#                                 [ 1 , 3 , 2 ]         -> To find just greater number travel right to left and find first no in downtrend
#                                 [ 2 , 1 , 3 ]         -> Swap it with just greater on right and arrange all elements on right in ascending order 
#                                 [ 2 , 3 , 1 ]
#                                 [ 3 , 1 , 2 ]
#                                 [ 3 , 2 , 1 ]
# Below is the python code for the above implementation 
def swap(arr, i, j):                                    # Swap function used to swap the elements in range
        arr[i], arr[j] = arr[j], arr[i] 

def reverse(arr, start, end):                           # Reverse function used to reverse the element in range
    while start < end:                                  # Two pointer approach
        swap(arr, start, end)
        start += 1
        end -= 1
def NextPermutation(Array):                             # Function takes the array as an parameter 
    N=len(Array)                                        # Storing the array length into N
    i=N-2                                               # Now i stores the N-2 which is the last before element of the array 
    while(i>=0 and Array[i]>=Array[i+1]):               # Running a while loop where i should be greater than 0 and Array[i] should be greater than or equal to Next element in the array 
        i=i-1                                           # Decrementing the i by 1 
    if (i<0):                                           # Checking with if condition whether the i variable is smaller than 0 or not 
        reverse(Array,0,N-1)                            # Then reversing them 
        return Array                                    # Returning it over here
    j=N-1                                               # Now initiating new variable named j 
    while(j>i and Array[j]<=Array[i]):                  # Checking where j<i and Array[j]<=Array[i]
        j=j-1                                           # Decrementing j by 1
    swap(Array,i,j)                                     # Swapping the array element
    reverse(Array,i+1,N-1)                              # Reversing the array withing the range
    return Array                                        # Returning the array with the least permutation

array=[5,8,7,9,5,3]
print(NextPermutation(array))



# Meaning of Next Permutation function 
# We are going to find the first permutation of the given array elements which is smallest in lexicographical order 
# 5,8,7,9,5,3
# Next ---> 5,8,9,3,5,7
# Last ---> 9,8,7,5,5,3
# We are moving from the current one to next minimum largest not to maximum largest directly 
        
