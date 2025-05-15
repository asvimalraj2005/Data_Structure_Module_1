# Next Permutation 
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
def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

def reverse(arr, start, end):
    while start < end:
        swap(arr, start, end)
        start += 1
        end -= 1
def NextPermutation(Array):
    N=len(Array)
    i=N-2
    while(i>=0 and Array[i]>=Array[i+1]):
        i=i-1
    if (i<0): 
        reverse(Array,0,N-1)
        return Array
    j=N-1
    while(j>i and Array[j]<=Array[i]): 
        j=j-1
    swap(Array,i,j)
    reverse(Array,i+1,N-1)
    return Array 

array=[5,8,7,9,5,3]
print(NextPermutation(array))
        